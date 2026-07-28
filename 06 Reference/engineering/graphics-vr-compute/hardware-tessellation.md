---
summary: "GPU fixed-function subdivision of patches with hull/domain shaders for adaptive, displacement-driven surface detail."
status: active
tags: [reference, engineering, graphics, tessellation, patches]
private: false
---

# Hardware Tessellation

## Purpose

GPU fixed-function subdivision of patches with hull/domain shaders for adaptive, displacement-driven surface detail.

## Pipeline Stages

- Tessellation inserts three stages between the vertex and geometry stages, operating on patch primitives (control-point sets) rather than triangles.
- The hull shader (D3D) / tessellation control shader (GL) runs per control point and, in its patch-constant phase, outputs the tessellation factors for the patch edges and interior.
- The fixed-function tessellator subdivides the patch domain (quad, triangle, or isoline) into a mesh of barycentric/UV sample points according to those factors.
- The domain shader / tessellation evaluation shader runs per generated vertex, evaluating the patch's surface equation (e.g. Bezier or B-spline basis) to place the final vertex.

## Factors, LOD, and Displacement

- Edge tessellation factors control subdivision density per edge; matching factors on shared edges between patches prevents cracks.
- Factors can be computed per-frame from screen-space projected edge length or distance, giving continuous, adaptive LOD without swapping meshes.
- Displacement mapping is the primary payload: the domain shader offsets each new vertex along its normal by a sampled height map, turning a coarse base mesh into high-frequency detail.
- Culling and factor-clamping in the hull shader avoid tessellating off-screen or sub-pixel patches, controlling the throughput cost.
- Very high factors can produce sub-pixel triangles that waste rasterization; mesh shaders are now often preferred for extreme geometry amplification.

## Sources

- Microsoft: Tessellation Overview - https://learn.microsoft.com/en-us/windows/win32/direct3d11/direct3d-11-advanced-stages-tessellation
- Khronos OpenGL Wiki: Tessellation - https://www.khronos.org/opengl/wiki/Tessellation

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
