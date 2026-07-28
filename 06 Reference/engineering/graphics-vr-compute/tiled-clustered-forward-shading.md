---
summary: "Culling lights into screen tiles or view-frustum clusters so forward rendering scales to thousands of lights."
status: active
tags: [reference, engineering, graphics, forward-plus, light-culling]
private: false
---

# Tiled and Clustered Forward Shading (Forward+)

## Purpose

Culling lights into screen tiles or view-frustum clusters so forward rendering scales to thousands of lights.

## How It Works

- A depth pre-pass establishes per-pixel depth, then a compute pass bins lights against screen-space tiles (Forward+) using each tile's min/max depth to bound a sub-frustum.
- Each tile stores a compact list of lights whose volumes intersect it; the shading pass iterates only that list per pixel.
- Clustered variants subdivide the view frustum in 3D (x, y, and a depth slice), producing view-independent clusters that avoid depth-discontinuity over-inclusion.
- Depth slices are usually distributed exponentially so cluster size tracks perspective foreshortening.

## Key Ideas

- Culling is decoupled from shading and runs on the GPU, so light assignment cost is largely independent of geometry.
- Because it stays forward, it keeps native MSAA and handles transparent surfaces, unlike classic deferred shading.
- Clustered light lists can be reused for both forward and deferred passes, and remain valid across the whole frame.

## Tradeoffs

- Tiled Forward+ suffers when a tile spans large depth ranges, inflating its light list; clustered binning mitigates this.
- Storing and traversing per-tile/cluster light lists adds memory and indirection versus a single global loop.

## Sources

- Harada et al., Forward+: Bringing Deferred Lighting to the Next Level (EG 2012) - https://diglib.eg.org/handle/10.2312/conf.EG2012.short.005-008
- Olsson et al., Clustered Deferred and Forward Shading - https://efficientshading.com/2012/01/01/clustered-deferred-and-forward-shading/

---
## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
