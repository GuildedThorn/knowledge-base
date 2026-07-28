---
summary: "Tree acceleration structures over primitives that give logarithmic ray-scene intersection for ray tracing."
status: active
tags: [reference, engineering, graphics, bvh, acceleration]
private: false
---

# Bounding Volume Hierarchies (BVH)

## Purpose

Tree acceleration structures over primitives that give logarithmic ray-scene intersection for ray tracing.

## Structure

- A BVH is a tree whose nodes bound subsets of scene primitives, most commonly with axis-aligned bounding boxes (AABBs); leaves hold a few primitives.
- A ray tests a node's box first; on a miss the entire subtree is skipped, reducing intersection tests from linear to roughly logarithmic in scene size.
- Unlike spatial partitions (kd-tree, grid), a BVH partitions objects, so each primitive appears in exactly one leaf and boxes may overlap.
- It is the dominant acceleration structure in production and underlies hardware ray tracing's BLAS/TLAS.

## Construction and Updates

- Quality builds use the Surface Area Heuristic (SAH), splitting to minimize expected traversal cost estimated from child surface areas and primitive counts.
- Fast builders bin candidate split planes or use Morton-code (LBVH) sorting for near-real-time construction on the GPU.
- Deep, tight trees traverse faster but cost more to build; shallow trees build fast but test more primitives per leaf.
- For animated scenes, refitting recomputes node bounds while keeping topology (cheap) until deformation degrades quality enough to warrant a rebuild.

## Sources

- PBRT: Bounding Volume Hierarchies - https://www.pbr-book.org/3ed-2018/Primitives_and_Intersection_Acceleration/Bounding_Volume_Hierarchies
- Wald et al., State of the Art in Ray Tracing Animated Scenes - https://onlinelibrary.wiley.com/doi/10.1111/j.1467-8659.2008.01313.x

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
