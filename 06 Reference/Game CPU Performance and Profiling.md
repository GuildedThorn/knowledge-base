---
summary: CPU-side game performance — profiling methodology, Godot's built-in tools, C#/.NET GC behavior, marshalling overhead, multithreading, physics tuning.
status: active
tags: [reference, gamedev, godot, performance]
private: false
---

## Purpose

CPU-side performance discipline for Godot 4 (C#/.NET): profiling methodology, allocation/GC behavior, multithreading, and common bottleneck patterns. Complements [Godot Engine Architecture and Patterns](kb://06-reference-godot-engine-architecture-and-patterns); rendering/GPU cost is a separate note. Compiled 2026-07-24.

## Profiling Methodology — Measure, Don't Guess

- **Sampling vs instrumenting profilers**: sampling interrupts at intervals and records the call stack (low overhead, can miss short spikes — Tracy, `dotnet-trace`). Instrumenting inserts timing probes at function entry/exit (exact counts and self/total time, but overhead scales with call frequency) — Godot's built-in Profiler is instrumenting. Use instrumenting to find *which system* is slow, then a sampling profiler or targeted `Stopwatch` calls to find the exact hot line.
- **Frame budgets**: 60fps = 16.6ms/frame; 90fps (VR floor) = 11.1ms — VR is unforgiving because dropped frames cause reprojection artifacts/nausea, not just judder (see [VR Performance Optimization](kb://06-reference-vr-performance-optimization)).
- **CPU-bound vs GPU-bound**: (1) halve render resolution/shader complexity while keeping logic identical — frame time drops proportionally = GPU-bound, barely moves = CPU-bound; (2) disable vsync and uncap fps — if fps rockets up, GPU/vsync was the ceiling, if it stays flat, CPU is. Godot's Monitors tab often makes this unnecessary — compare CPU "Process/Physics Process Time" against `RenderingServer`'s reported GPU frame time directly.

## Godot 4 Built-in Profiling Tools

- **Debugger → Profiler**: instrumenting, function-level timing (works for GDScript and C# — a huge stack of `Variant`-marshalling frames on the C# side tells you the interop boundary is the problem, not game logic).
- **Monitors tab**: live graphs for object/node counts, orphan nodes, draw calls, physics active-object counts, and Process/Physics-Process/Idle time split — the fastest way to answer "is frame time growing from node-count bloat or a specific subsystem."
- **RenderingServer breakdown**: separates CPU-side render *preparation* (culling, draw-call submission — this is CPU work) from actual GPU execution time — a lot of "rendering cost" people blame on the GPU is really CPU work building command buffers.
- **4.6**: tighter integration with the external **Tracy** profiler for GDScript (higher-fidelity, lower-overhead than the built-in instrumenting profiler) and a new **ObjectDB Profiler** snapshotting the live Object database to catch leaked node references/runaway `RefCounted` growth across frames. Reach for Tracy over the built-in profiler beyond basic triage.

## C#/.NET GC Behavior

Godot 4+ uses CoreCLR — the real .NET generational GC (Gen0/1/2). Small allocations every `_Process`/`_PhysicsProcess` accumulate Gen0 garbage; once the budget fills, a collection runs synchronously mid-frame — the classic GC hitch (a 3ms frame suddenly taking 15ms).

- **DATAS** (Dynamic Adaptation To Application Sizes): opt-in in .NET 8, default in .NET 9, default GC mode in .NET 10 — dynamically sizes the heap from live Gen2/LOH data instead of always maintaining a large heap, trading ~2-3% throughput for >80% smaller working set. Matters because the game shares the machine with a display compositor/VR runtime — a smaller resident set means fewer page faults competing for frame budget.
- **Workstation vs Server GC**: Godot C# defaults to Workstation GC. Server GC (`<ServerGarbageCollection>true</ServerGarbageCollection>`) uses per-core heaps and can shorten pauses for CPU-heavy multithreaded work, but only pays off on multi-core machines and raises baseline memory — test both, don't assume it's a free win for a client (clearer win for a dedicated server build).
- **Struct vs class**: structs avoid heap allocation/Gen0 pressure for small frequently-created data (a per-frame raycast result) — but large structs passed by value cost their own copy overhead, and boxing into `object`/`Variant` erases the benefit. Prefer `readonly struct` for small immutable hot-loop types; keep anything with references or >~16-24 bytes as a class.
- **LINQ/boxing in hot loops**: LINQ iterator/closure allocations and `IEnumerable` boxing of value-type enumerators are a top avoidable Gen0 source in `_Process`. Replace `.Where().Select()` chains with manual `for` loops over arrays/`List<T>` in per-frame code.
- **Object pooling**: the standard fix once allocation is proven the bottleneck (via profiler, not guessed) — the C#-specific angle beyond Godot-node pooling is that pooling also avoids the *managed* allocation, not just engine-object instantiation cost, which is the larger win for GC pause avoidance.

## Marshalling Overhead (C# ↔ Godot Core)

Every non-primitive C#→engine call crosses **Variant marshalling** — cheap once, adds up fast in loops (iterating a `Godot.Collections.Array`/`Dictionary` element-by-element in a hot loop is markedly slower than a native `List<T>`/`Dictionary<K,V>`, converted once outside the loop). `GetNode()`/`FindChild()` do a string-path scene-tree lookup plus a marshalled return — never call inside `_Process`/`_PhysicsProcess`; cache the reference in `_Ready()` (or use `[Export]` node references, resolved once at scene load). Prefer signals connected once over per-frame polling through the interop boundary; prefer cached field access over repeated `Call("method_name", args)` (pays a string-hash lookup + Variant marshal per argument).

## Multithreading

Main thread owns rendering submission and most Node/SceneTree state. `WorkerThreadPool` (`AddTask`/`AddGroupTask`) is Godot's built-in job system for background CPU work (procedural gen, pathfinding, asset preprocessing) that doesn't touch Node state directly. .NET `Task`/`async` layers on top for I/O-bound or CPU-bound background work — `Task.Run` for CPU-bound, real `async`/`await` for I/O so a thread-pool thread isn't blocked waiting on a stream.

**Thread safety gotcha**: most Node/SceneTree API calls are **not thread-safe** — `AddChild`, mutating a `Transform`, touching `RenderingServer` from a worker thread corrupts state or throws Godot's "main thread only" errors. Do heavy computation off-thread; marshal only the final "apply to scene" step back via `CallDeferred()` (or `Callable.From(() => ...).CallDeferred()` for C# closures).

## Physics Optimization

- **Fixed timestep tuning**: `Engine.PhysicsTicksPerSecond` (default 60) is decoupled from render fps — running physics at 30-50Hz under a 90/120fps VR render target (with `Engine.PhysicsJitterFix` smoothing interpolation) saves real CPU if gameplay doesn't need full-rate physics.
- **Collision shape complexity**: prefer primitives (box/sphere/capsule) over `ConcavePolygonShape3D`/trimesh — concave collision is dramatically more expensive per broad+narrow-phase check. Use convex decomposition for complex static geometry.
- **Spatial partitioning**: the physics server already does BVH-based broad-phase culling internally (Godot Physics and Jolt both). Build your own spatial hash/grid for high-volume *non-physics* proximity queries (AI perception, AoE checks against thousands of entities) rather than spamming `Area3D` overlap signals or per-entity `PhysicsDirectSpaceState3D` queries — each also pays the marshalling cost above if issued from C# in a loop.
- Keep physics-affecting logic strictly in `_PhysicsProcess`; movement code in `_Process` causes frame-rate-dependent physics and effectively multiplies CPU cost under variable render fps.

## Common Bottleneck Checklist

- Thousands of live `Node`s each carrying per-frame dispatch overhead even when empty — consolidate repeated simple objects (bullets, foliage) into `MultiMeshInstance3D` + a plain data array instead of one Node per instance.
- Deep scene-tree nesting slows signal propagation and relative-path traversal — flatten where transforms don't need the grouping; cache long paths at `_Ready()`.
- Polling (`if health <= 0` every `_Process`) instead of firing a signal on the actual state change — the single most common "why is my idle scene burning 20% CPU" cause.
- String concatenation/interpolation every frame (debug labels, format-string logging) pressures Gen0 — cache formatted strings, update only on change.
- Any `GetNode`/`FindChild`/dictionary-string-key lookup performed every frame instead of once at `_Ready()`/on-change — the Profiler's call-count column makes these stand out immediately since count scales with frame count.

## Related

- [Godot Engine Architecture and Patterns](kb://06-reference-godot-engine-architecture-and-patterns)
- [GPU and Rendering Optimization](kb://06-reference-gpu-and-rendering-optimization)
- [VR Performance Optimization](kb://06-reference-vr-performance-optimization)
- [Reference Map](kb://01-maps-reference-map)
