---
summary: "Shaders are small parallel programs that run across vertices, fragments, compute invocations, or other GPU stages."
status: active
tags: [reference, engineering, graphics, shaders]
private: false
---

# Shaders and GPU Programming

## Purpose

Shaders are small parallel programs that run across vertices, fragments, compute invocations, or other GPU stages.

## Core Model

- Shader languages and APIs expose data through uniforms, push constants, buffers, textures, samplers, and varyings.
- SIMT/SIMD execution makes divergence and memory access patterns visible performance concerns.
- Precision, color space, derivative availability, and coordinate conventions affect correctness.

## Engineering Notes

- Keep shader inputs explicit and inspect compiled variants when performance matters.
- Prefer branchless/math-friendly forms only when profiling supports it; readability still matters.
- Use debug visualizations for normals, roughness, UVs, depth, motion vectors, and LOD.

## Sources

- The Book of Shaders - https://thebookofshaders.com/
- Vulkan shader docs - https://docs.vulkan.org/guide/latest/shader_memory_layout.html
- Godot shading language - https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
