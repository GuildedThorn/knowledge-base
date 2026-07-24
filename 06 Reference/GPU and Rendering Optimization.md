---
summary: Draw-call cost, batching, MultiMesh limits, culling, overdraw/fill-rate, shader cost, texture compression — the general rendering optimization layer under any specific feature.
status: active
tags: [reference, gamedev, godot, performance, rendering]
private: false
---

## Purpose

The draw-call/batching/culling/shader/texture layer that sits under any specific rendering feature — doesn't repeat the cube-sphere/terrain-LOD specifics in [High-Fidelity Planet Rendering](kb://06-reference-high-fidelity-planet-rendering-godot) or [Terrain Rendering Optimization](kb://06-reference-terrain-rendering-optimization), or the ORM channel packing in [3D Model Creation for Games](kb://06-reference-3d-model-creation-for-games). Compiled 2026-07-24.

## Draw Call Cost and Batching

Each draw call carries CPU-side overhead independent of triangle count — state changes, driver validation, command submission — which is why draw-call count is a first-class budget even on scenes with modest polygon counts. **Static batching** combines meshes sharing a material at build/import time (cheap at runtime, batched objects can't move independently). **Dynamic batching** combines eligible small meshes per-frame on the CPU (flexible, adds per-frame cost, only pays off for small/simple meshes).

**Godot 4's actual behavior — 2D vs 3D differ genuinely**: 2D has real automatic batching (Compatibility/GLES3 since 4.0, extended to Forward+/Mobile Vulkan in 4.4 — though Vulkan draw calls are already cheap enough that the payoff is smaller than under OpenGL). **3D does not automatically batch arbitrary meshes** — real-time merging of thousands of triangles every frame is too expensive to do transparently, so Godot leaves it to the developer: pre-combine static meshes at import, or use instancing for repeated geometry. Each distinct material/surface costs a separate draw call — atlasing textures and merging materials directly cuts count. Shadow-casting lights compound this: each re-renders casters into its own shadow map, so several shadow lights can make a scene draw-call-bound even with few visible objects.

## GPU Instancing / MultiMesh

`MultiMeshInstance3D` — already used throughout vr-brain (planets, rocks, asteroid belt) — renders many copies of one mesh+material in one draw call, driven by a per-instance transform buffer. Real limits worth knowing: per-instance custom data is capped at **8 floats per instance** (two `vec4`s), a real ceiling for shaders wanting heavy per-instance variation (an open feature request for more channels hasn't landed). All instances in one MultiMesh **must share mesh and material** — divergent visuals need separate MultiMesh buckets or texture-array/atlas tricks within that float budget. Wins specifically for many copies of *identical* geometry+material — doesn't help heterogeneous unique-mesh scenes, where static pre-merging or draw-call budgeting still matters.

## Culling

**Frustum culling** is automatic everywhere, effectively free.

**Occlusion culling (Godot 4)**: rasterizes user-placed `OccluderInstance3D` geometry into a low-res buffer **on the CPU** (via Embree), then tests each occludee's AABB against it — this has a genuine CPU cost of its own; complex occluder meshes can make the CPU-side raster pass the bottleneck. Build deliberately simplified occluder proxies, not full-res meshes. Net win in interiors/cities/canyon layouts with lots of mutual occlusion; can cost more than it saves in open scenes — measure, don't enable by default.

**Visibility ranges (HLOD)**: every `GeometryInstance3D` exposes `visibility_range_begin`/`_end` (+ fade margins) — "show from 0-80m, swap to a cheap merged proxy from 80m." Unlike simple LOD swap, a single coarse mesh can replace many small ones at distance, cutting draw calls *and* triangle count together. This is the general-purpose, non-terrain HLOD mechanism (terrain LOD is covered separately).

## Overdraw and Fill-Rate

Overdraw = shading the same pixel more than once (stacked transparent layers, or unsorted opaque geometry). Disproportionately costly on **tile-based mobile/VR GPUs** and doubly so in VR, where stereo rendering doubles the fill-rate cost of every overdrawn pixel. Mitigations: sort opaque front-to-back so depth test rejects occluded fragments before the expensive fragment shader runs (opaque depth-prepass concept); minimize/shrink overlapping transparent particle systems; cap particle count and screen-space size as an explicit budget; avoid near-full-screen transparent effects on VR/mobile targets.

## Shader Complexity and Cost

Vertex shaders run per-vertex; fragment shaders run per-pixel (per-sample under MSAA) — at VR resolution, pixel count vastly exceeds vertex count, so **fragment cost is usually the real bottleneck**. Moving computation from fragment to vertex stage is a standard lever.

**Branching**: GPUs execute in SIMD groups (warps/wavefronts) covering many pixels at once — if threads within a group diverge at a branch, hardware executes *both* branches for the whole group, masking off inactive lanes. A per-pixel-data-driven branch can cost as much as running both branches on every pixel in a divergent group; branches uniform across a draw call (shader-parameter-driven, not per-pixel) are cheap.

**Texture samples per fragment**: each `texture()` call is a memory fetch (potential cache miss) multiplied by every covered pixel — stacking albedo/normal/ORM/detail/noise reads per fragment adds up fast, especially at 2x VR resolution.

**Shader baking (4.4+/4.5)**: before 4.4, pipeline compilation happened reactively as objects entered view, causing first-encounter stutter. 4.4 introduced ubershaders (a precompiled fallback with runtime specialization constants — the optimized per-feature pipeline compiles in the background instead of blocking the frame) plus load-time precompilation detecting needed pipelines from scene content — substantially fixed traversal stutter in 4.5 (reports cite up to ~20x faster pipeline load in some cases). Web/HTML5 export still suffers most since this mitigation isn't fully available there.

## Texture Memory and Compression

GPU compression formats stay compressed in VRAM (unlike JPEG/PNG, which decompress to full size on load), cutting both memory footprint and bandwidth. **Desktop**: BC7/BPTC for high-quality SDR, BC6H for HDR, BC5 for two-channel (normal maps), BC1/DXT1 for simpler cases — Godot's importer picks BPTC with High Quality import enabled, S3TC otherwise. **Mobile/standalone VR**: ASTC — matters specifically for standalone headsets since Adreno/Mali-class mobile GPUs natively support it with better quality-per-bit than older ETC2, while desktop BPTC/BC7 generally aren't supported on that hardware at all; Godot uses ASTC on mobile with High Quality import, ETC2 otherwise. Re-importing note: compression format changes don't retroactively affect already-imported textures.

**Mipmapping**: costs ~33% extra memory (geometric series overhead of the full mip chain) but avoids minification aliasing/shimmer and — more important for performance — lets the GPU sample a smaller, cache-friendlier mip for distant geometry instead of thrashing the texture cache on full-res texels for a handful of visible pixels.

**Texture streaming**: load only the mip level appropriate to an object's current screen size/distance instead of keeping every texture full-res resident, trading some load-time popping for a much smaller resident VRAM footprint — matters most on memory-constrained platforms (standalone VR, mobile).

## VR Rendering Cost Multiplier

Stereo rendering roughly doubles per-frame cost (shading twice, once per eye). Godot mitigates the CPU side via **multiview/single-pass stereo rendering**: instead of two full separate render passes, Godot 4's Vulkan renderer allocates an extra array layer on render targets and renders both eyes together using Vulkan's multiview extension, with a `ViewIndex` shader variable selecting per-eye matrices — the CPU issues the scene once, GPU/driver handles per-eye duplication. Godot has also added foveated rendering via `VK_EXT_fragment_density_map`/Meta's `XR_FB_foveation_vulkan`, rendering peripheral regions at reduced shading rate. Device support is uneven (works well on Quest 3, crashed on earlier Snapdragon XR2 Gen1 devices before being routed through the vendor extension path). Full detail in [VR Performance Optimization](kb://06-reference-vr-performance-optimization).

## Current Godot Rendering Developments (2025-2026)

- **4.5**: shader baker/ubershader stutter fixes; Vulkan Mobile renderer gains Fragment Density Map foveated rendering for standalone VR.
- **4.6**: further Vulkan pipeline optimization — descriptor set caching (reuses sets more aggressively, reported 10-20% CPU render-thread time cut in draw-call-heavy scenes), render pass merging (merges adjacent compatible passes), more aggressive indirect draw batching for static meshes sharing materials, buffer sub-allocation reducing memory fragmentation, full SSR rewrite for temporally stable reflections. Reported (third-party benchmark, not official engine numbers) ~20-33% fps improvement across tested hardware tiers.

## Related

- [High-Fidelity Planet Rendering (Godot)](kb://06-reference-high-fidelity-planet-rendering-godot)
- [Terrain Rendering Optimization](kb://06-reference-terrain-rendering-optimization)
- [3D Model Creation for Games](kb://06-reference-3d-model-creation-for-games)
- [Game CPU Performance and Profiling](kb://06-reference-game-cpu-performance-and-profiling)
- [VR Performance Optimization](kb://06-reference-vr-performance-optimization)
- [Reference Map](kb://01-maps-reference-map)
