---
summary: "Splitting the view frustum into depth ranges with per-cascade shadow maps for uniform directional-light shadow quality."
status: active
tags: [reference, engineering, graphics, shadows, csm]
private: false
---

# Cascaded Shadow Maps

## Purpose

Splitting the view frustum into depth ranges with per-cascade shadow maps for uniform directional-light shadow quality.

## Core Model

- A single directional-light shadow map spread over the whole view frustum wastes resolution far away and starves it near the camera.
- CSM partitions the view frustum into several depth slices (cascades) and renders a separate shadow map fitted tightly to each slice.
- Split distances often blend a logarithmic and a uniform distribution (practical/parallel-split scheme) to balance near detail and far coverage.
- Each cascade uses its own light-space orthographic projection sized to just enclose that slice's frustum corners.

## How It Works

- During shading, the pixel's view-space depth selects which cascade to sample; blending across the cascade boundary hides the seam.
- Snapping each cascade's projection to texel-sized increments prevents shadow edges shimmering as the camera moves.

## Engineering Notes

- Peter-panning (detached shadows) comes from excessive depth bias; normal-offset or slope-scaled bias reduces both acne and peter-panning.
- Filtering such as PCF or variance/exponential shadow maps softens the hard aliased edges each cascade produces.
- Typical setups use 3-4 cascades; more improves quality but multiplies shadow-render cost.

## Sources

- Microsoft: Cascaded Shadow Maps - https://learn.microsoft.com/en-us/windows/win32/dxtecharts/cascaded-shadow-maps
- GPU Gems 3, Ch. 10: Parallel-Split Shadow Maps - https://developer.nvidia.com/gpugems/gpugems3/part-ii-light-and-shadows/chapter-10-parallel-split-shadow-maps-programmable-gpus

---
## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
