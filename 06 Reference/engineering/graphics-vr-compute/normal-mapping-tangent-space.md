---
summary: "Perturbing surface normals from a texture in per-vertex tangent space to add detail without extra geometry."
status: active
tags: [reference, engineering, graphics, normal-map, tangent-space]
private: false
---

# Normal Mapping and Tangent Space

## Purpose

Perturbing surface normals from a texture in per-vertex tangent space to add detail without extra geometry.

## How It Works

- A normal map stores per-texel unit normals encoded in RGB; the shader reads them to perturb the interpolated surface normal used in lighting.
- Normals are stored in tangent space (relative to the surface), so a single map works regardless of the mesh's world orientation.
- Tangent-space normals cluster around +Z, giving the map its characteristic bluish tint; each channel maps [0,1] texel values to [-1,1] vector components.
- The technique adds shading detail without extra triangles, but the silhouette stays flat since geometry is unchanged.

## TBN Frame

- The tangent-bitangent-normal (TBN) matrix transforms between tangent and world/view space; it is built from the vertex normal plus a tangent derived from UV gradients.
- Tangent and bitangent come from solving the edge/UV equations per triangle, then averaging and orthonormalizing (Gram-Schmidt) per vertex.
- Baking tools and the runtime must share a tangent convention; the MikkTSpace standard exists so bakers and engines compute identical frames.
- Convention mismatches (green-channel Y sign, handedness) cause inverted or seam-lit surfaces at UV boundaries.

## Sources

- LearnOpenGL: Normal Mapping - https://learnopengl.com/Advanced-Lighting/Normal-Mapping
- Blinn, Simulation of Wrinkled Surfaces (1978) - https://dl.acm.org/doi/10.1145/965139.507101
- MikkTSpace tangent standard - http://www.mikktspace.com/

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
