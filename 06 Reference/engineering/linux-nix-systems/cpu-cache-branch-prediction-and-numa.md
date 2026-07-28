---
summary: "CPU performance depends heavily on cache locality, branch predictability, memory ordering, vectorization, and NUMA placement."
status: active
tags: [reference, engineering, systems, cpu, performance]
private: false
---

# CPU Cache, Branch Prediction, and NUMA

## Purpose

CPU performance work requires understanding the memory hierarchy and front-end execution behavior, not just algorithmic complexity.

## Core Model

- Caches hide main-memory latency when data has temporal or spatial locality.
- Branch predictors guess control flow so instruction pipelines stay full.
- Mispredictions flush speculative work and create latency.
- NUMA systems have non-uniform access costs depending on CPU socket and memory placement.
- SIMD/vector units increase throughput when data layout and operations are compatible.

## Engineering Notes

- Data layout can dominate object-oriented abstraction cost in hot paths.
- Avoid pointer chasing in tight loops when arrays or struct-of-arrays layouts work.
- Branchless code helps only when it reduces misprediction or vectorizes cleanly.
- Pinning, memory locality, and allocator behavior matter on multi-socket systems.
- Measure with perf/PMU counters before rewriting code.

## Sources

- Intel 64 and IA-32 Architectures Optimization Reference Manual - https://www.intel.com/content/www/us/en/developer/articles/technical/intel64-and-ia32-architectures-optimization.html
- Intel Software Developer Manuals - https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Linux Scheduler, cgroups, and Priority](kb://06-reference-engineering-linux-nix-systems-linux-scheduler-cgroups-and-priority)
- [GPU Architecture: SIMT, Memory, and Tensor Cores](kb://06-reference-engineering-graphics-vr-compute-gpu-architecture-simt-memory-and-tensor-cores)
