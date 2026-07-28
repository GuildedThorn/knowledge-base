---
summary: "An IO-aware exact attention algorithm that tiles computation to reduce memory reads/writes and enable longer contexts."
status: active
tags: [reference, engineering, ai-ml, attention, kernels]
private: false
---

# FlashAttention

## Purpose

An IO-aware exact attention algorithm that tiles computation to reduce memory reads/writes and enable longer contexts.

## How It Works

- Standard attention materializes the full N-by-N score matrix in GPU high-bandwidth memory (HBM), making it memory-bandwidth bound.
- FlashAttention tiles queries, keys, and values into blocks that fit in fast on-chip SRAM and fuses the whole attention computation into one kernel.
- It never writes the full attention matrix to HBM, using an online (streaming) softmax that updates running max and sum statistics per block.
- The result is mathematically exact attention, not an approximation, with far fewer HBM reads and writes.

## Engineering Notes

- Avoiding the O(N^2) memory materialization gives near-linear memory in sequence length, enabling longer contexts and larger batches.
- FlashAttention-2 improves GPU utilization with better work partitioning across warps and reduced non-matmul operations.
- For the backward pass, softmax and intermediate stats are recomputed from stored statistics rather than reloaded, trading cheap FLOPs for scarce memory bandwidth.

## Tradeoffs

- Gains are largest when attention is memory-bound; benefits shrink for very short sequences.
- Requires hardware-specific kernels, so support varies by GPU architecture and precision.

## Sources

- FlashAttention: Fast and Memory-Efficient Exact Attention - https://arxiv.org/abs/2205.14135
- FlashAttention-2 - https://arxiv.org/abs/2307.08691

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
