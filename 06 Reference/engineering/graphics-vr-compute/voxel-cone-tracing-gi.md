---
summary: "Approximating dynamic indirect illumination by voxelizing the scene and cone-tracing radiance through a sparse octree."
status: active
tags: [reference, engineering, graphics, global-illumination, voxel]
private: false
---

# Voxel Cone Tracing Global Illumination

## Purpose

Approximating dynamic indirect illumination by voxelizing the scene and cone-tracing radiance through a sparse octree.

## How It Works

- The scene is voxelized each frame (or when geometry changes) into a volume storing per-voxel albedo, opacity, and injected direct radiance.
- Voxels are mip-mapped so coarser levels average finer radiance, letting a wide gather sample fewer, larger voxels at distance.
- Indirect light at a shading point is gathered by tracing several diffuse cones over the hemisphere plus a tighter specular cone along the reflection direction.
- Each cone marches through the volume, accumulating pre-filtered radiance at a mip level chosen to match the cone's growing footprint, front-to-back with alpha.

## Storage and Tradeoffs

- Storage uses a sparse voxel octree (SVO) or a clipmap/cascaded grid to cover large scenes without a dense full-resolution volume.
- The technique gives fully dynamic diffuse and glossy GI without precomputed light maps, updating as lights and geometry move.
- Costs are high memory bandwidth, revoxelization overhead for dynamic geometry, and light leaking or blockiness from the voxel approximation.
- NVIDIA's VXGI productized the approach; it has largely been superseded by hardware ray tracing and probe/SDF-based GI for new engines.

## Sources

- Crassin et al., Interactive Indirect Illumination Using Voxel Cone Tracing (2011) - https://research.nvidia.com/publication/2011-09_interactive-indirect-illumination-using-voxel-cone-tracing
- NVIDIA VXGI - https://archive.docs.nvidia.com/gameworks/content/gameworkslibrary/visualfx/vxgi.htm

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
