---
summary: "Compute shaders run general-purpose parallel work on the GPU, useful for simulation, culling, image processing, particles, and data transforms."
status: active
tags: [reference, engineering, graphics, compute]
private: false
---

# Compute Shaders and GPGPU

## Purpose

Compute shaders run general-purpose parallel work on the GPU, useful for simulation, culling, image processing, particles, and data transforms.

## Core Model

- Compute dispatches workgroups made of invocations that coordinate through shared memory and barriers.
- Memory layout, coalescing, atomics, and synchronization decide performance and correctness.
- Compute can reduce CPU-GPU round trips when data stays resident on the GPU.

## Engineering Notes

- Use compute when parallelism and data residency justify GPU complexity.
- Design workgroup size around hardware occupancy and memory access shape.
- Avoid readback in frame loops; CPU waits on GPU data destroy parallelism.

## Sources

- Vulkan compute shader tutorial - https://docs.vulkan.org/tutorial/latest/11_Compute_Shader.html
- Godot compute shaders - https://docs.godotengine.org/en/stable/tutorials/shaders/compute_shaders.html
- GPU Gems archive - https://developer.nvidia.com/gpugems/gpugems/contributors

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
