---
summary: "Embeddings map items into vector space so semantic similarity can be searched with approximate nearest-neighbor indexes."
status: active
tags: [reference, engineering, ai, embeddings]
private: false
---

# Embeddings and Vector Search

## Purpose

Embeddings map items into vector space so semantic similarity can be searched with approximate nearest-neighbor indexes.

## Core Model

- Embedding models encode text, images, audio, code, or mixed modalities into fixed-size vectors.
- Similarity is usually measured with cosine, dot product, or Euclidean distance depending on model training.
- ANN indexes such as HNSW, IVF, and PQ trade recall, latency, memory, and build cost.

## Engineering Notes

- Evaluate embeddings on your retrieval task; generic benchmarks may not match domain language.
- Store source metadata, chunk boundaries, model version, and normalization state with vectors.
- Tune recall/latency with real query sets and inspect failures manually.

## Sources

- FAISS documentation - https://faiss.ai/
- HNSW paper - https://arxiv.org/abs/1603.09320
- Sentence Transformers docs - https://www.sbert.net/

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
