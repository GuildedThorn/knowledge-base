---
summary: "How GPUs run threads in lockstep warps/wavefronts, and how branch divergence throttles throughput."
status: active
tags: [reference, engineering, graphics, simt, warp]
private: false
---

# GPU SIMT Execution Model and Warps

## Purpose

How GPUs run threads in lockstep warps/wavefronts, and how branch divergence throttles throughput.

## Core Model

- SIMT (Single Instruction, Multiple Threads) groups threads into warps of 32 (NVIDIA) or wavefronts of 32/64 (AMD) that share one instruction fetch and issue unit.
- Every thread in a warp executes the same instruction at the same time on its own registers and data; the hardware amortizes scheduling and fetch cost across the group.
- Each thread has its own program counter and register state (per the Tesla architecture, Lindholm et al. 2008), so threads can follow independent control flow at a performance cost.
- The Volta architecture added independent per-thread program counters, relaxing some lockstep constraints while keeping warp-level scheduling.

## Key Ideas

- Branch divergence: when threads in a warp take different sides of a conditional, the warp serially executes each taken path with the inactive lanes masked off, so a fully divergent if/else can halve throughput.
- Reconvergence at the post-branch point restores full-width execution; keeping branch granularity aligned to warp size avoids divergence.
- Memory divergence (scattered addresses within a warp) similarly reduces effective bandwidth.

## Engineering Notes

- Latency hiding: the SM keeps many warps resident and switches to a ready warp whenever the current one stalls on memory, so high occupancy hides multi-hundred-cycle latencies without caches.
- Occupancy is bounded by registers-per-thread and shared memory per block; over-allocating either caps resident warps and exposes latency.

## Sources

- CUDA C++ Programming Guide: SIMT Architecture - https://docs.nvidia.com/cuda/cuda-c-programming-guide/
- Lindholm et al., NVIDIA Tesla: A Unified Graphics and Computing Architecture (2008) - https://ieeexplore.ieee.org/document/4523358

---
## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
