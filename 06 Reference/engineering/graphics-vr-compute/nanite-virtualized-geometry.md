---
summary: "Unreal Engine's cluster-based system that streams and renders film-quality mesh detail with GPU-driven culling."
status: active
tags: [reference, engineering, graphics, nanite, virtualized-geometry]
private: false
---

# Nanite Virtualized Geometry

## Purpose

Unreal Engine's cluster-based system that streams and renders film-quality mesh detail with GPU-driven culling.

## Cluster Hierarchy and LOD

- Nanite preprocesses meshes into clusters of about 128 triangles, then builds a hierarchical DAG where parent clusters are simplified merges of their children.
- At render time the GPU walks this hierarchy and selects, per view, the cluster cut whose screen-space error falls below a pixel threshold, giving continuous LOD without discrete pop.
- Because simplification is done per cluster group and locked at group boundaries, adjacent clusters at different LODs meet without cracks.
- Visibility is fully GPU-driven: hierarchical frustum and occlusion culling (using a two-pass HZB from the previous frame's depth) reject clusters before rasterization.

## Rasterization and Streaming

- Nanite rasterizes into a visibility buffer that stores per-pixel cluster and triangle IDs rather than shading directly, decoupling geometry cost from material cost.
- Small triangles (roughly pixel-sized) are drawn by a custom compute-based software rasterizer using 64-bit atomics, which beats hardware rasterizers on tiny primitives; larger triangles fall back to hardware rasterization.
- Material shading runs in a deferred pass over the visibility buffer, so overdraw and shading are evaluated once per visible pixel.
- Geometry is virtualized and streamed on demand from disk at cluster granularity, so only the detail needed for the current views resides in memory.
- Classic strengths and limits: excels at dense static opaque meshes; historically excluded skinned, translucent, or heavily world-position-offset geometry, though later Unreal versions expanded coverage.

## Sources

- Karis et al., Nanite: A Deep Dive (SIGGRAPH 2021) - https://advances.realtimerendering.com/s2021/
- Unreal Engine: Nanite Virtualized Geometry - https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
