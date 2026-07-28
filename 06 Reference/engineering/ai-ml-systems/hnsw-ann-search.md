---
summary: "A hierarchical navigable small-world graph enabling fast, high-recall approximate nearest-neighbor vector search."
status: active
tags: [reference, engineering, ai-ml, ann, indexing]
private: false
---

# HNSW Approximate Nearest Neighbor Search

## Purpose

A hierarchical navigable small-world graph enabling fast, high-recall approximate nearest-neighbor vector search.

## Core Model

- Builds a multi-layer proximity graph; upper layers are sparse long-range links, the bottom layer holds every element.
- Layer assignment for each node is drawn from an exponentially decaying distribution, giving a logarithmic tower of "express lanes."
- Search descends from a single entry point at the top layer, greedily hopping toward the query, then refines at lower layers.
- The structure generalizes navigable small-world graphs by adding the skip-list-style hierarchy, cutting search from polynomial toward logarithmic complexity.

## How It Works

- Greedy routing at each layer moves to the neighbor closest to the query until no neighbor improves distance, then drops down a layer.
- The bottom-layer search keeps a dynamic candidate list of size `ef`; larger `ef` raises recall at the cost of more distance computations.
- `M` sets the number of bidirectional links per node; higher `M` improves recall and connectivity but increases memory and build time.
- Backtracking via the candidate heap lets the search escape local minima that pure greedy descent would get stuck in.

## Tradeoffs

- Recall, latency, and memory are tuned through `ef` (query time), `efConstruction` (build time), and `M` (graph degree).
- Insertion is incremental and supports online index growth, but deletions are awkward and usually handled by tombstoning.
- Memory footprint scales with `M` and vector count, making it heavier than compressed indexes like IVF-PQ.

## Sources

- Efficient and Robust ANN Search using HNSW Graphs - https://arxiv.org/abs/1603.09320

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
