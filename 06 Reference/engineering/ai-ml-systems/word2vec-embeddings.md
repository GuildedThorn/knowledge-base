---
summary: "Shallow neural models learning dense word vectors from context, capturing semantic and syntactic regularities."
status: active
tags: [reference, engineering, ai-ml, embeddings, nlp]
private: false
---

# Word2Vec Word Embeddings

## Purpose

Shallow neural models learning dense word vectors from context, capturing semantic and syntactic regularities.

## Core Model

- Two shallow architectures: CBOW predicts a target word from its surrounding context, while skip-gram predicts context words from a target word.
- Training a single-hidden-layer network over a large corpus yields a dense vector per word from the learned weight matrix; no deep network is required.
- Skip-gram generally performs better on rare words, while CBOW is faster and smooths over frequent words.

## How It Works

- Negative sampling replaces the expensive full softmax by distinguishing the true context word from a few sampled noise words, making training scale to billions of tokens.
- Hierarchical softmax is an alternative that factors the output over a binary tree for logarithmic-cost normalization.
- Frequent-word subsampling and context-window sizing tune the balance between semantic and syntactic signal.
- Learned vectors support linear analogy arithmetic, e.g. king - man + woman lands near queen.

## Sources

- Efficient Estimation of Word Representations - https://arxiv.org/abs/1301.3781
- Distributed Representations of Words and Phrases - https://arxiv.org/abs/1310.4546

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
