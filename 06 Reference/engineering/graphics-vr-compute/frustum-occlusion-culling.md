---
summary: "Rejecting geometry outside the view frustum or hidden behind other objects before it reaches the rasterizer."
status: active
tags: [reference, engineering, graphics, culling, visibility]
private: false
---

# Frustum and Occlusion Culling

## Purpose

Rejecting geometry outside the view frustum or hidden behind other objects before it reaches the rasterizer.

## Core Model

- The view frustum is defined by six planes (left, right, top, bottom, near, far) extracted from the combined view-projection matrix.
- Frustum culling tests each object's bounding volume against those planes; a volume fully outside any plane is rejected.
- Axis-aligned bounding boxes (AABBs) and bounding spheres are the common test primitives, trading tightness for cheap intersection math.
- Optimized plane-AABB tests use the "n-vertex" (nearest corner along the plane normal) to decide inclusion with a single dot product per plane.

## How It Works

- Occlusion culling removes objects hidden behind nearer opaque geometry, which frustum tests cannot detect.
- Hierarchical Z-buffer (Hi-Z) builds a mip pyramid of depth and tests a bounding volume against the coarsest level that covers it.
- GPU-driven culling runs frustum and Hi-Z tests in compute shaders, emitting draw arguments via indirect draw to avoid CPU round-trips.
- Hardware occlusion queries and predication let draws be conditionally skipped based on prior frame or depth-only pre-pass visibility.

## Engineering Notes

- Spatial hierarchies (BVH, octree, loose grids) let whole subtrees be culled with one test, cutting per-object work.
- Temporal reprojection of last frame's depth reduces false occlusion at the cost of one-frame latency in visibility.
- Overly conservative bounds cause popping; too-tight bounds raise per-object cost, so balance against scene density.

## Sources

- Assarsson & Moller, Optimized View Frustum Culling Algorithms - https://www.cse.chalmers.se/~uffe/vfc.pdf
- Real-Time Rendering (book) - https://www.realtimerendering.com/

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
