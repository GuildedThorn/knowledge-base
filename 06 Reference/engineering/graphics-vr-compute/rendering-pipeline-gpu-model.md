---
summary: "Modern GPUs transform scene data into pixels through programmable shader stages, fixed-function rasterization, memory hierarchies, and synchronization."
status: active
tags: [reference, engineering, graphics, gpu]
private: false
---

# Rendering Pipeline and GPU Model

## Purpose

Modern GPUs transform scene data into pixels through programmable shader stages, fixed-function rasterization, memory hierarchies, and synchronization.

## Core Model

- The graphics pipeline typically includes vertex processing, primitive assembly, rasterization, fragment/pixel shading, depth/stencil, blending, and presentation.
- GPU performance depends on parallel occupancy, memory bandwidth, cache locality, divergence, overdraw, and synchronization.
- APIs such as Vulkan, Direct3D, Metal, and WebGPU expose different control levels over the same hardware themes.

## Engineering Notes

- Profile before optimizing; CPU submission, GPU execution, and presentation can bottleneck independently.
- Minimize state changes, overdraw, synchronization stalls, and avoid per-frame allocation.
- Use GPU captures to inspect actual passes, barriers, resource lifetimes, and shader cost.

## Sources

- Vulkan Guide - https://docs.vulkan.org/guide/latest/index.html
- NVIDIA GPU Performance Background - https://developer.nvidia.com/blog/tag/gpu-performance/
- Godot rendering docs - https://docs.godotengine.org/en/stable/tutorials/rendering/index.html

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
