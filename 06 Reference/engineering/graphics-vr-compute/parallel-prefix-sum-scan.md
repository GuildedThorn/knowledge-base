---
summary: "The work-efficient parallel scan primitive underlying sorting, compaction, and stream processing on GPUs."
status: active
tags: [reference, engineering, graphics, scan, parallel-primitive]
private: false
---

# Parallel Prefix Sum (Scan)

## Purpose

The work-efficient parallel scan primitive underlying sorting, compaction, and stream processing on GPUs.

## Core Model

- Scan applies an associative binary operator across an array, producing all partial reductions in one pass.
- Inclusive scan includes each element's own value in its output; exclusive scan excludes it, so output[i] is the reduction of elements before i (identity at index 0).
- Any associative operator works (add, max, min, logical OR), which is what lets the computation be reassociated across parallel threads.
- Segmented scan carries per-element head flags so independent sub-arrays are scanned in one launch, the basis for sparse and irregular workloads.

## Algorithms and Work Efficiency

- Hillis-Steele (naive) does log(n) passes but O(n log n) total work, wasting operations though it has low step depth.
- Blelloch (work-efficient) uses an up-sweep reduction then a down-sweep, doing O(n) work in 2 log(n) steps.
- On GPUs the Blelloch tree maps to shared memory per block; padding indices avoids shared-memory bank conflicts.
- Large arrays scan hierarchically: scan blocks, scan the block sums, then add each block's offset back.
- Scan is the engine of stream compaction, radix sort, histogram, sparse matrix ops, and allocation of variable output.

## Sources

- Blelloch, Prefix Sums and Their Applications - https://www.cs.cmu.edu/~guyb/papers/Ble93.pdf
- GPU Gems 3, Ch. 39: Parallel Prefix Sum (Scan) with CUDA - https://developer.nvidia.com/gpugems/gpugems3/part-vi-gpu-computing/chapter-39-parallel-prefix-sum-scan-cuda

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
