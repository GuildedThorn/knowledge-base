---
summary: "Decoupling geometry from lighting by writing a G-buffer, then shading in screen space to scale to many lights."
status: active
tags: [reference, engineering, graphics, gbuffer, lighting]
private: false
---

# Deferred Shading

## Purpose

Decoupling geometry from lighting by writing a G-buffer, then shading in screen space to scale to many lights.

## Core Model

- A geometry pass rasterizes the scene once, writing per-pixel surface attributes into a G-buffer instead of computing lighting inline.
- Typical G-buffer targets hold world/view-space position (or reconstructed depth), packed normals, albedo, and material params like roughness/metalness.
- A second lighting pass reads the G-buffer per screen pixel and accumulates each light's contribution, decoupling shading cost from geometric complexity.
- Cost scales with pixels times lights rather than triangles times lights, so hundreds or thousands of lights become tractable.

## Engineering Notes

- Light volumes (spheres, cones) or tiled culling restrict shading to pixels a light can actually reach, cutting wasted work.
- Reconstructing position from depth plus the inverse projection avoids storing a full position target, shrinking bandwidth.

## Tradeoffs

- Fat G-buffers are bandwidth-heavy; memory traffic, not ALU, is often the bottleneck, motivating attribute packing.
- Hardware MSAA is awkward because edges must be resolved per-sample against material data; many engines fall back to post-process AA.
- Transparency does not fit the single-surface-per-pixel model and is usually handled by a separate forward pass.

## Sources

- GPU Gems 2, Ch. 9: Deferred Shading in S.T.A.L.K.E.R. - https://developer.nvidia.com/gpugems/gpugems2/part-ii-shading-lighting-and-shadows/chapter-9-deferred-shading-stalker
- LearnOpenGL: Deferred Shading - https://learnopengl.com/Advanced-Lighting/Deferred-Shading

---
## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
