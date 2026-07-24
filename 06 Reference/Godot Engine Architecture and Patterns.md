---
summary: General Godot 4 engine architecture — scene tree vs ECS, signals, autoloads, Resources, GDScript vs C#, groups, performance patterns, gameplay state machines.
status: active
tags: [reference, gamedev, godot]
private: false
---

## Purpose

vr-brain's existing notes ([High-Fidelity Planet Rendering](kb://06-reference-high-fidelity-planet-rendering-godot), [Terrain Rendering Optimization](kb://06-reference-terrain-rendering-optimization)) are rendering-specific. This note is the general Godot 4 engine architecture layer — scene composition, events, data, and language choice — not rendering. Compiled 2026-07-24.

## Scene Tree / Node Architecture vs ECS

Godot composes games from a **tree of nodes**; a saved subtree is a **scene**. A node bundles data *and* logic together (traditional OOP/composition), unlike a strict ECS engine (Unity DOTS, Bevy) that splits entities/components/systems apart.

- **Scene instancing = "prefab"**: build a scene once, instance it anywhere; editing the source propagates to all instances.
- **Scene inheritance**: an inherited scene shares a parent's whole tree/scripts and lets you override/add nodes — good for variants (`Enemy.tscn` → `EnemyBoss.tscn`) without duplicating structure.
- **Why not ECS**: Godot favors composition-over-inheritance and readability over cache-friendly linear iteration over homogeneous component data. Adopting true ECS means building a parallel system alongside the node tree, since physics/rendering expect nodes.
- **When it matters**: thousands-to-millions of homogeneous, tightly-updated objects (particle swarms, bullet hell, large crowds) are ECS/DOTS territory. Scene-graph-shaped problems (a handful to a few hundred heterogeneous objects — UI, characters, world objects) are simpler as nodes; the performance gap doesn't matter there.

## Signals (Observer Pattern)

A node emits a signal; any number of listeners connect without the emitter knowing who's listening — connect via the editor or `signal_name.connect(callable)`. Use a signal when the sender shouldn't need to know its listeners, multiple systems must react to one event, or a listener might not exist; use a direct call when you need a return value or there's exactly one always-present receiver.

**Signal spaghetti** — deeply nested `get_node("../../..")` wiring or dozens of ad-hoc connections — is fixed with a global **Event Bus**: an autoloaded script declaring all cross-system signals, so distant nodes emit/connect through it instead of hunting for direct references.

## Autoloads / Singletons

Scripts/scenes registered in Project Settings → Autoload, instantiated once at startup, globally accessible by name. Legitimate uses: genuinely-global game state, audio bus managers, save/load, the event bus above, scene-transition managers.

**Anti-pattern warning** (strong community consensus): the single most overused Godot feature. Failure modes: one autoload per subsystem until the autoload list *is* the architecture and nothing refactors in isolation, or a single autoload accumulating unrelated state into a "junk drawer." Never create circular autoload dependencies (hangs on splash screen); don't autoload non-global UI.

## The Resource System

A `Resource` is a serializable, reference-counted data container that does **not** live in the scene tree — no transform, no `_process`, just fields — saved as `.tres` (text) or `.res` (binary). Contrast with `Node` (scene-tree-resident, carries behavior). Custom: `extends Resource`, `class_name ItemData`, `@export` fields; multiple nodes can reference the same resource instance, making it natural for shared/immutable definitional data — item defs, enemy stats, dialogue, ability configs.

**Canonical inventory pattern**: items are `ItemData` resources (blueprint); an `Inventory` stores references + quantity, not "item nodes"; UI reads resource fields directly — cleanly separating data (resources) / logic (manager) / presentation (scene). Serialization is free — persist the `.tres`/`.res` directly, no custom save code needed for the data itself.

## GDScript vs C#

GDScript is bytecode-interpreted, **not JIT** (a common misconception) — Godot 4.6 added bytecode-level optimizations but not a JIT; **typed GDScript** (`var speed: float = 5.0`) has produced better bytecode since 4.0. C# runs on .NET (Mono/CoreCLR) with a real JIT and generally wins for CPU-heavy work: procedural generation with millions of iterations, custom pathfinding/spatial algorithms, physics beyond the built-in engine, bulk load-time data processing, large multiplayer server logic.

**Interop**: a project can mix GDScript and C# nodes; public methods/vars are reachable across the boundary. A GDScript class **cannot** inherit a C# class or vice versa — cross-language sharing goes through composition or signals, not inheritance. Every C#↔engine collection op crosses an interop/marshalling boundary with measurable overhead in hot loops. Practical split: GDScript for iteration-heavy scripting/UI/glue (hot-reload, editor integration); C# for performance-critical systems — matches vr-brain's existing all-C# choice, with targeted GDScript for editor-tool scripts being a legitimate (not anti-) pattern.

## Groups

A lightweight tag system managed by `SceneTree` — a node joins any number of named groups with no hard reference existing between nodes (`add_to_group("enemies")`; Godot 4.3+ adds **Global Groups**, predefined project-wide tags). Query with `get_tree().get_nodes_in_group("enemies")`; broadcast with `get_tree().call_group("enemies", "take_damage", 10)` — the idiomatic alternative to threading references through autoloads for "find all X" queries.

## Performance Patterns

- **Object pooling**: instancing/freeing nodes at runtime is comparatively expensive (allocation, tree entry/exit, `_ready` overhead). For high-churn spawns (bullets, hit VFX, debris), pre-instance a pool and toggle `set_process(false)`/`visible = false` rather than `queue_free()`+re-instance. Pooled-but-in-tree nodes still receive `_process`/signals unless explicitly disabled — reset state on reuse, guard stale signal connections.
- **`_process` vs `_physics_process` vs signals-only**: `_physics_process` at fixed tick for movement/collision/deterministic timing; `_process` per rendered frame for purely visual updates (animation blending, camera smoothing, UI). Never poll for "did X change" every frame when a signal can notify on the actual transition. Never do rendering/animation work in `_physics_process` — visible jitter when rates diverge.
- **MultiMesh** — already used throughout vr-brain (planets, rocks, asteroid belt) — draws many identical instances in one draw call; the standard tool for large uniform object counts.

## State Machines for Gameplay Logic

Three idiomatic tiers, in order of complexity:

1. **Enum + match/switch** in `_physics_process` — fine for 3–6 simple states with no per-state variables or enter/exit setup.
2. **Node-based states** — each state its own node/scene (`PatrolState`, `ChaseState`, `AttackState`, `StunnedState`) as children of a `StateMachine` node, each implementing `enter()`/`exit()`/`physics_update()`. The most common idiomatic Godot pattern — inspectable live in the remote scene tree, each state's logic isolated.
3. **`AnimationTree` state machine** — visual graph driving animation transitions directly; state = animation state, not general gameplay/AI logic (see [Character and Object Animation Development](kb://06-reference-character-and-object-animation-development)).

## Current Godot 4.x Developments (2025–2026)

- **4.4** (Mar 2025): Jolt Physics ships built-in (not default yet); real-time scene editing while running; enhanced XR support.
- **4.5** (Sep 2025): stencil buffer, screen-reader accessibility, script backtracing, shader baking (cuts load-time stutter), Wayland native sub-windows, SDL3 gamepad driver, WASM SIMD; GDExtension gained main-loop callback registration (startup/shutdown hooks).
- **4.6** (Jan 2026): **Jolt Physics becomes default for new projects**; Vulkan optimizations; foveated rendering on mobile (relevant to OpenXR/VR perf); LibGodot for embedding the engine as a library; full SSR rewrite; "Modern" editor theme.
- **4.7** (Jun 2026, latest at research time): `AreaLight3D`, HDR output, `Control` offset transforms, Android export polish, further XR improvements.
- **GDExtension** (replaced GDNative from Godot 3): compiles native code (C++, Rust via godot-rust) directly against the engine's binary API without a full engine recompile, and can register classes as first-class engine types — the 4.5 main-loop-callback addition is the most relevant recent architecture change for native tooling/plugins.

## Related

- [High-Fidelity Planet Rendering (Godot)](kb://06-reference-high-fidelity-planet-rendering-godot)
- [Terrain Rendering Optimization](kb://06-reference-terrain-rendering-optimization)
- [Character and Object Animation Development](kb://06-reference-character-and-object-animation-development)
- [3D Model Creation for Games](kb://06-reference-3d-model-creation-for-games)
- [vr-brain - Architecture](kb://07-projects-vr-brain-vr-brain-architecture)
- [Reference Map](kb://01-maps-reference-map)
