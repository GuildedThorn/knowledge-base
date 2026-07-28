---
summary: "A compute-style geometry pipeline of task and mesh shaders that replaces fixed vertex/geometry stages for GPU-driven rendering."
status: active
tags: [reference, engineering, graphics, mesh-shader, meshlet]
private: false
---

# Mesh Shaders

## Purpose

A compute-style geometry pipeline of task and mesh shaders that replaces fixed vertex/geometry stages for GPU-driven rendering.

## How It Works

- Mesh shaders replace the input-assembler, vertex, hull, domain, and geometry stages with two programmable, compute-like stages: the task (amplification) shader and the mesh shader.
- The optional task shader runs first, decides how many mesh shader workgroups to launch, and can cull or amplify work before any vertices are processed.
- The mesh shader runs as a cooperative workgroup that outputs a small indexed primitive batch directly, writing vertices and primitive connectivity into on-chip output arrays.
- There is no fixed-function index buffer or vertex fetch; the shader author controls how geometry is generated and laid out.

## Meshlets and GPU-Driven Culling

- Geometry is preprocessed into meshlets, compact clusters of typically 64-128 vertices and up to a few hundred triangles bounded by API limits.
- Each meshlet carries bounds and a normal cone, so the task shader can do per-cluster frustum, occlusion, and backface-cone culling before rasterization.
- This moves visibility decisions to the GPU, cutting draw-call overhead and letting scenes with millions of triangles be culled at fine granularity.
- Mesh shaders integrate with amplification for LOD selection, choosing meshlet detail per cluster without CPU round-trips.
- Support is exposed via D3D12, Vulkan (VK_EXT_mesh_shader), and Metal on modern GPUs.

## Sources

- NVIDIA: Introduction to Turing Mesh Shaders - https://developer.nvidia.com/blog/introduction-turing-mesh-shaders/
- DirectX-Specs: Mesh Shader - https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
