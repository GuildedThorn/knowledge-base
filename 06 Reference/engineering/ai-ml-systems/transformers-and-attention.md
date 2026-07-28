---
summary: "Transformers use attention over token sequences to build contextual representations and power modern language, vision, and multimodal models."
status: active
tags: [reference, engineering, ai, transformers]
private: false
---

# Transformers and Attention

## Purpose

Transformers use attention over token sequences to build contextual representations and power modern language, vision, and multimodal models.

## Core Model

- Self-attention lets each token combine information from other tokens in a sequence.
- Multi-head attention, feed-forward blocks, residual connections, layer normalization, and positional encoding form the basic architecture.
- Training and inference cost scale strongly with sequence length, model size, and memory bandwidth.

## Engineering Notes

- Separate model architecture facts from product claims; transformer does not imply reasoning quality by itself.
- Track context length, tokenizer behavior, latency, memory, and evals for every model deployment.
- Use smaller task-specific models when latency, privacy, or cost dominates.

## Sources

- Attention Is All You Need - https://arxiv.org/abs/1706.03762
- The Illustrated Transformer - https://jalammar.github.io/illustrated-transformer/
- Hugging Face Transformers docs - https://huggingface.co/docs/transformers/index

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
