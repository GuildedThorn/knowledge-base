---
summary: "Approximating contact shadowing by sampling the depth buffer around each pixel to darken occluded creases."
status: active
tags: [reference, engineering, graphics, ao, screen-space]
private: false
---

# Screen-Space Ambient Occlusion (SSAO)

## Purpose

Approximating contact shadowing by sampling the depth buffer around each pixel to darken occluded creases.

## How It Works

- For each pixel, SSAO reconstructs view-space position and normal from the depth buffer (and normal buffer) rather than using scene geometry.
- It scatters sample points in a hemisphere oriented around the surface normal and tests each against stored depth to estimate how occluded the point is.
- The occlusion factor darkens ambient/indirect lighting in creases, corners, and contact regions that uniform ambient light would miss.
- A range check rejects samples whose depth difference is too large, preventing distant surfaces from casting false occlusion.

## Engineering Notes

- Sample kernels are rotated per-pixel by a small tiled noise texture to trade banding for high-frequency noise, then a blur pass removes that noise.
- The technique is view-dependent and misses occluders outside the screen or behind nearer surfaces, since it only sees the depth buffer.
- HBAO integrates a horizon-based occlusion estimate along depth, and GTAO adds a physically grounded ground-truth cosine-weighted formulation for better accuracy.
- Cost scales with samples per pixel and blur radius, so quality is commonly dialed by sample count.

## Sources

- LearnOpenGL: SSAO - https://learnopengl.com/Advanced-Lighting/SSAO
- Mittring, Finding Next Gen: CryEngine 2 (SIGGRAPH 2007) - https://dl.acm.org/doi/10.1145/1281500.1281671

---
## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
