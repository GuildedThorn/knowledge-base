---
summary: "GPU ray-tracing pipelines with acceleration structures and shader stages exposed by DXR and Vulkan Ray Tracing."
status: active
tags: [reference, engineering, graphics, dxr, raytracing]
private: false
---

# Hardware-Accelerated Ray Tracing (DXR / Vulkan RT)

## Purpose

GPU ray-tracing pipelines with acceleration structures and shader stages exposed by DXR and Vulkan Ray Tracing.

## Acceleration Structures

- Geometry is organized into a two-level hierarchy: bottom-level acceleration structures (BLAS) hold triangle/AABB primitives; a top-level structure (TLAS) holds instances referencing BLAS with transforms.
- The driver builds and manages these opaque structures; the app requests builds, updates (refits), and compaction to reclaim memory.
- Fixed-function hardware (RT cores) traverses the structure and performs ray-box and ray-triangle intersection, freeing shader cores.
- Splitting static geometry (build once) from dynamic instances (rebuild TLAS per frame) is the standard cost tradeoff.

## Pipeline and Shaders

- A ray-tracing pipeline defines shader stages: ray generation, closest-hit, any-hit, miss, and intersection (for custom procedural primitives).
- `TraceRay`/`traceRayEXT` launches a ray from a ray-gen shader; the runtime dispatches hit or miss shaders based on traversal results, and shaders may recurse.
- The shader binding table (SBT) is a GPU buffer indexing which hit/miss shaders and their records apply to each geometry and ray type.
- DXR (Direct3D 12) and Vulkan Ray Tracing (VK_KHR_ray_tracing_pipeline) expose the same conceptual model with different API surfaces.

## Sources

- DirectX Raytracing (DXR) Spec - https://microsoft.github.io/DirectX-Specs/d3d/Raytracing.html
- Ray Tracing in Vulkan (Khronos) - https://www.khronos.org/blog/ray-tracing-in-vulkan
- Ray Tracing Gems - https://link.springer.com/book/10.1007/978-1-4842-4427-2

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
