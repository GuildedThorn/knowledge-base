---
summary: "A library for efficient billion-scale vector similarity search with quantization and GPU acceleration."
status: active
tags: [reference, engineering, ai-ml, ann, vector-search]
private: false
---

# FAISS Similarity Search Library

## Purpose

A library for efficient billion-scale vector similarity search with quantization and GPU acceleration.

## Core Model

- Developed at Meta AI, FAISS indexes dense vectors and answers k-nearest-neighbor and range queries under L2 or inner-product metrics.
- Index types are composable: `Flat` (exhaustive), `IVF` (inverted-file coarse partitioning), `HNSW` (graph), and `PQ`/`OPQ` (compression).
- An index factory string (e.g. `IVF4096,PQ64`) declaratively assembles coarse quantizer plus encoding for a target scale.
- Training a quantizer on a representative sample precedes adding vectors for IVF and PQ variants.

## How It Works

- IVF clusters the space with k-means into Voronoi cells; queries probe only `nprobe` nearest cells, trading recall for speed.
- Product quantization splits each vector into subvectors, encoding each against its own codebook to shrink memory drastically.
- Asymmetric distance computation compares a full-precision query against PQ-compressed database codes via precomputed lookup tables.
- GPU indexes replicate or shard data across devices, achieving order-of-magnitude throughput gains over CPU for large batches.

## Engineering Notes

- Billion-scale search combines IVF for candidate pruning with PQ for memory-bounded storage on a single machine.
- Recall is tuned by `nprobe`, PQ code length, and coarse centroid count; more probes and longer codes raise accuracy.
- Exact `Flat` indexes serve as a ground-truth baseline for measuring approximate-index recall.

## Sources

- Billion-scale Similarity Search with GPUs - https://arxiv.org/abs/1702.08734
- FAISS repository - https://github.com/facebookresearch/faiss

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
