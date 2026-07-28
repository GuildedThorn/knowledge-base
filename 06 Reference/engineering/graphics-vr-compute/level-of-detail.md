---
summary: "Selecting mesh, shading, or texture detail based on distance and screen coverage to bound rendering cost."
status: active
tags: [reference, engineering, graphics, lod, simplification]
private: false
---

# Level of Detail (LOD)

## Purpose

Selecting mesh, shading, or texture detail based on distance and screen coverage to bound rendering cost.

## Core Model

- LOD reduces the geometric or shading complexity of objects that contribute few pixels, keeping frame cost roughly proportional to visible detail.
- Discrete LOD precomputes several fixed-resolution meshes and swaps between them; simplest to author and cheapest at runtime.
- Continuous LOD encodes a spectrum of detail (e.g. progressive meshes) and extracts a mesh at the needed resolution per frame.
- Hierarchical/view-dependent LOD refines different regions of one large object independently, essential for terrain and huge meshes.

## Selection and Artifacts

- Selection metrics include distance to camera, projected screen-space size/error, and eccentricity; screen-space error bounds the pixel deviation of a simplified mesh.
- Popping is the visible snap when a discrete LOD switches; it is the main quality cost of the discrete approach.
- Geomorphing interpolates vertex positions across the transition to hide popping; alpha/dithered blending fades between levels instead.
- Texture mipmapping is the LOD analog for surface detail, selecting resolution by screen-space texel density.
- Overly aggressive LOD saves GPU time but introduces silhouette and shading errors; the budget is a quality-versus-throughput tradeoff.

## Sources

- Luebke et al., Level of Detail for 3D Graphics - https://lodbook.com/
- Real-Time Rendering (book) - https://www.realtimerendering.com/

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
