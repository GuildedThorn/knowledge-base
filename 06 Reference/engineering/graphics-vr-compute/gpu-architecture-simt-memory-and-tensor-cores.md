---
summary: "GPU performance depends on SIMT execution, occupancy, memory hierarchy, bandwidth, synchronization, and specialized matrix/tensor hardware."
status: active
tags: [reference, engineering, graphics, gpu, compute, performance]
private: false
---

# GPU Architecture: SIMT, Memory, and Tensor Cores

## Purpose

GPU architecture knowledge explains why rendering, compute shaders, and AI inference bottleneck on occupancy, memory access, synchronization, and specialized matrix units.

## Core Model

- GPUs execute many lightweight threads grouped into warps/wavefronts under SIMT-style execution.
- Throughput comes from hiding latency with massive parallelism.
- Memory hierarchy typically includes registers, shared/local memory, L1/L2 caches, texture caches, and high-bandwidth device memory.
- Divergent control flow reduces efficiency when lanes in a warp take different paths.
- Tensor/matrix cores accelerate dense matrix operations used heavily in AI workloads.

## Engineering Notes

- Coalesced memory access matters; random access patterns waste bandwidth.
- Occupancy is useful only when the kernel has enough independent work and is not limited by another bottleneck.
- Synchronization and atomics can serialize otherwise parallel workloads.
- Graphics and ML optimization both reduce to data movement, locality, and parallel work shape.

## Sources

- NVIDIA Ampere architecture whitepaper page - https://www.nvidia.com/en-us/geforce/news/rtx-30-series-ampere-architecture-whitepaper-download/
- NVIDIA CUDA C++ Programming Guide - https://docs.nvidia.com/cuda/cuda-c-programming-guide/
- AMD GPUOpen Radeon GPU Profiler - https://gpuopen.com/rgp/

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Rendering Pipeline and GPU Model](kb://06-reference-engineering-graphics-vr-compute-rendering-pipeline-gpu-model)
- [Compute Shaders and GPGPU](kb://06-reference-engineering-graphics-vr-compute-compute-shaders-and-gpgpu)
