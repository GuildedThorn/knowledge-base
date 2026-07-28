---
summary: "Structuring global-memory access patterns and using on-chip shared memory to sustain GPU memory bandwidth."
status: active
tags: [reference, engineering, graphics, coalescing, shared-memory]
private: false
---

# GPU Memory Coalescing and Shared Memory

## Purpose

Structuring global-memory access patterns and using on-chip shared memory to sustain GPU memory bandwidth.

## Core Model

- Global memory is serviced in aligned transactions (typically 32-, 64-, or 128-byte segments); the hardware coalesces the addresses a warp requests into the minimum number of transactions.
- Coalesced access: when consecutive threads read consecutive, aligned addresses, one warp's loads collapse into a few transactions and bandwidth approaches peak.
- Strided, misaligned, or scattered access forces many partial transactions per warp, wasting most of each fetched segment and multiplying effective latency.
- Structure-of-arrays layouts coalesce better than array-of-structures for per-thread element access.

## How It Works

- Shared memory is fast on-chip SRAM, private to a thread block, used as a software-managed cache to stage data reused across threads.
- Tiling: threads cooperatively load a tile of global data into shared memory once, synchronize with a barrier, then compute from shared memory many times, cutting global traffic (the classic tiled matrix-multiply pattern).
- Bank conflicts: shared memory is split into banks (32 on NVIDIA); if multiple threads in a warp hit different addresses in the same bank, accesses serialize. Padding arrays or reindexing avoids conflicts.

## Engineering Notes

- Broadcast (all threads read one address) and conflict-free strides are the fast shared-memory cases.
- Align data structures to transaction size and prefer 128-byte-aligned base pointers for coalesced global loads.

## Sources

- CUDA C++ Best Practices Guide - https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/
- CUDA C++ Programming Guide - https://docs.nvidia.com/cuda/cuda-c-programming-guide/

---
## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
