---
summary: RGP's Linux/AMDVLK problem, RenderDoc as the practical RADV-native choice, radeontop, and RADV_DEBUG env vars — the real toolchain for AMD GPU debugging on Linux.
status: active
tags: [reference, gamedev, godot, performance, gpu, amd, linux]
private: false
---

## Purpose

The vendor-tooling layer under [GPU and Rendering Optimization](kb://06-reference-gpu-and-rendering-optimization) and [Game CPU Performance and Profiling](kb://06-reference-game-cpu-performance-and-profiling) — where time actually goes on the RX 6700XT specifically, on NixOS/RADV, not Windows. Compiled 2026-07-24.

## Radeon GPU Profiler (RGP) — Not Practical on This Stack

RGP is AMD's dedicated low-level GPU profiler (part of the free Radeon Developer Tool Suite): per-shader-stage timing, wavefront occupancy/utilization, barrier/sync stalls, instruction-level detail, via API interception through the Radeon Developer Panel (RDP). RGP itself does ship Linux builds — it's not purely a Windows tool.

**The real catch**: RDP's Vulkan capture mechanism was built against **AMDVLK**, AMD's closed Vulkan driver, officially killed in Q2 2025. AMD's current Linux driver packages (25.20-series+) dropped AMDVLK and ship **RADV** (Mesa's open driver) by default — so RDP no longer supports capturing from Vulkan apps on current default Linux setups. RADV has its own trace mechanism (`MESA_VK_TRACE_*` env vars) producing a capture file that opens in the RGP *viewer* with reduced feature support, but the full RDP-orchestrated workflow requires deliberately staying on an older AMDVLK-bundling driver package — not realistic for NixOS. **Conclusion: RGP is not a practical everyday tool on a stock RADV setup** — it's a Windows/AMDVLK-oriented workflow that has fallen out of step with where Linux Vulkan actually is now.

## RenderDoc — The Practical Choice on Linux/RADV

Free, open-source, **Linux-native** frame-capture graphics debugger (also Windows, Android), Vulkan up to 1.4, D3D11/12, OpenGL/GLES. No AMDVLK dependency — hooks the Vulkan loader directly, works with RADV out of the box.

Core capabilities: step through every draw call/dispatch in a captured frame; inspect resource state/textures/buffers at each pipeline stage; step through shader instructions; **pixel history** (every draw that touched a given pixel and how each contributed to its final color — the tool for "why is this pixel wrong/black/overdrawn").

**Compute shaders**: explicit support for Vulkan compute shader capture and debugging (dispatch inspection, buffer/image bindings, step-through), including headless capture of compute-only work — directly relevant to [GPU Compute Shaders in Godot](kb://06-reference-gpu-compute-shaders-in-godot).

**AMD/RADV compatibility**: Mesa contributors (Feral Interactive) added `VK_AMD_shader_info` to RADV specifically to improve shader statistics/disassembly reporting inside RenderDoc — an actively maintained, first-class combination, not an afterthought.

**Capturing a Godot frame**: no special export flags needed — RenderDoc's "Launch Application" (File → Launch Application / Ctrl+N) works directly against the Godot binary: set Executable Path to the Godot binary, Working Directory to the project folder, pass `--path <project_path>` to run the project directly without an exported build. Default capture hotkey **F12**/Print Screen. Godot has no first-party "press a hotkey to trigger a RenderDoc capture" binding — the community **Godot-RenderDoc-Launcher** plugin (Asset Library) adds an in-editor button to automate the launch step. Known open issues around RenderDoc + the GL-compatibility renderer and `create_local_rendering_device()` crashing on some RenderDoc versions — stick to the Vulkan (Forward+/Mobile) renderer for capture.

## AMD Linux-Native Tooling (Below Full Frame Capture)

**`radeontop`**: a `top`-style real-time monitor — overall GPU busy %, per-block utilization (graphics/texture/compute-shader-clock/DMA), VRAM/GTT usage, temperature, from the terminal with no capture overhead. Packaged in nixpkgs (`radeontop`) — one-line `environment.systemPackages` addition. The right first move before reaching for a frame debugger: run it during a session to confirm the GPU is actually pegged (vs. CPU-bound submission, vs. Monado/compositor overhead) before spending time in RenderDoc. `amdgpu_top` (newer Rust rewrite, also in nixpkgs) gives more granular per-IP-block stats than classic `radeontop` — worth it for RDNA2+ cards like the 6700XT.

**`RADV_DEBUG` env vars** (Mesa's RADV driver, comma-separated flags, no external tool needed):
- `info` — dump GPU/driver info at startup
- `hang` — enable GPU hang detection; on a hang, dumps a full report (command streams, shader state) to `~/radv_dumps_<pid>_<time>` — the go-to flag for VR-session freezes/resets
- `shaders`/`shaderstats`/`spirv`/`metashaders` — dump compiled ISA, stats, source SPIR-V, internal meta-shaders
- `syncshaders`/`fullsync` — force full GPU sync after every draw/dispatch, useful to isolate a hang/corruption to a specific call vs. a race
- `nocache` — disable the on-disk shader cache, ruling out stale-cache bugs after driver/shader changes
- `zerovram` — zero-init VRAM allocations, catching uninitialized-memory bugs

`RADV_PERFTEST` exposes opt-in perf experiments (`cswave32`/`gewave32`/`pswave32` forcing wave32 on compute/geometry/pixel stages) useful for A/B testing wavefront-width effects on RDNA2. No separate `AMD_VULKAN_ICD` variable in current Mesa — driver selection on a RADV-only system is automatic via the Vulkan ICD manifest.

**Rest of GPUOpen on Linux**: Radeon Memory Visualizer (RMV) and Radeon Raytracing Analyzer (RRA) both ship current Linux builds and are open source, but inherit the same RDP/AMDVLK capture-layer friction as RGP — treat as secondary/optional.

## Recommended Toolchain for This Stack

Given RADV (not AMDVLK) is the only realistic driver here:

1. **`radeontop`/`amdgpu_top`** — first-pass "is the GPU even the bottleneck" check, always-on, safe during a live WiVRn session.
2. **RenderDoc** — for anything needing an actual frame breakdown: draw-call-level timing/ordering, texture/buffer inspection, pixel history, compute dispatch debugging. The direct Linux-native substitute for what RGP gives on Windows — minus the wavefront-occupancy/hardware-counter depth RGP provides; more a correctness/structure debugger than a hardware-counter profiler, but it's the tool that actually works on this driver.
3. **`RADV_DEBUG=hang`** — the standing diagnostic for VR-session GPU hangs/resets, since those are hard to catch in RenderDoc's single-frame model.
4. RMV — optional/secondary, useful if VRAM pressure specifically becomes a suspect (12GB on the 6700XT, unlikely to be the first bottleneck).

Godot's built-in `RenderingServer` statistics are already covered in [Game CPU Performance and Profiling](kb://06-reference-game-cpu-performance-and-profiling) — cross-reference there rather than duplicating.

## Related

- [GPU and Rendering Optimization](kb://06-reference-gpu-and-rendering-optimization)
- [Game CPU Performance and Profiling](kb://06-reference-game-cpu-performance-and-profiling)
- [GPU Compute Shaders in Godot](kb://06-reference-gpu-compute-shaders-in-godot)
- [VR Performance Optimization](kb://06-reference-vr-performance-optimization)
- [Host nixos](kb://02-systems-nixos-host-nixos)
- [Reference Map](kb://01-maps-reference-map)
