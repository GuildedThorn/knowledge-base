---
summary: "NVIDIA's GPGPU model of kernels, grids, blocks, and threads with an explicit memory hierarchy."
status: active
tags: [reference, engineering, graphics, cuda, gpgpu]
private: false
---

# The CUDA Programming Model

## Purpose

NVIDIA's GPGPU model of kernels, grids, blocks, and threads with an explicit memory hierarchy.

## Core Model

- A kernel is a function marked `__global__` that launches as many parallel threads; the host configures the launch with `<<<grid, block>>>` execution configuration.
- Threads are organized into thread blocks, and blocks into a grid, each addressable in up to three dimensions via `threadIdx`, `blockIdx`, and `blockDim`.
- Threads within a block run on one streaming multiprocessor, can synchronize with `__syncthreads()`, and share fast shared memory; blocks are independent and may run in any order across SMs.
- Blocks are scheduled as warps (groups of 32 threads), which is the actual hardware execution granularity.

## How It Works

- Memory hierarchy is explicit: per-thread registers and local memory, per-block shared memory, and grid-wide global, constant, and texture memory. Data must be copied between host and device (or use unified/managed memory).
- Streams are ordered queues of operations; independent streams overlap kernel execution with host-device transfers and with each other for concurrency.
- Synchronization: `cudaDeviceSynchronize` and stream/event APIs coordinate host and device; events also time GPU work.

## Engineering Notes

- Choose block sizes as multiples of 32 to fill warps; grid size covers the problem with `ceil(N / blockSize)` and a bounds check in the kernel.
- Occupancy and memory-access patterns, not raw thread count, usually govern performance.

## Sources

- CUDA C++ Programming Guide - https://docs.nvidia.com/cuda/cuda-c-programming-guide/
- CUDA Toolkit Documentation - https://docs.nvidia.com/cuda/

---
## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
