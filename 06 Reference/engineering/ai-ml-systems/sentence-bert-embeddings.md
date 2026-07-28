---
summary: "A Siamese BERT network producing semantically meaningful sentence embeddings usable with cosine similarity."
status: active
tags: [reference, engineering, ai-ml, embeddings, retrieval]
private: false
---

# Sentence-BERT Sentence Embeddings

## Purpose

A Siamese BERT network producing semantically meaningful sentence embeddings usable with cosine similarity.

## Core Model

- Runs a shared-weight (Siamese) BERT encoder over each sentence and pools token outputs into a single fixed-size vector, most commonly by mean pooling.
- Fine-tunes with siamese or triplet objectives so that semantically similar sentences land close together under cosine distance.
- Solves BERT's efficiency problem: cross-encoding every candidate pair is quadratic, whereas SBERT encodes each sentence once and compares vectors cheaply.

## How It Works

- Classification training pairs use a softmax over the two embeddings and their element-wise difference; regression uses cosine similarity against gold scores; triplet loss pulls anchor toward positive and away from negative.
- Precomputed embeddings enable fast semantic search, clustering, and deduplication via nearest-neighbor indexes over cosine similarity.
- The sentence-transformers library packages many pretrained models and supports domain fine-tuning for retrieval and semantic textual similarity.

## Sources

- Sentence-BERT: Sentence Embeddings using Siamese Networks - https://arxiv.org/abs/1908.10084
- Sentence-Transformers documentation - https://www.sbert.net/

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
