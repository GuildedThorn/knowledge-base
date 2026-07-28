---
summary: "Normalization across features within a single example, making it well-suited to sequence models and Transformers."
status: active
tags: [reference, engineering, ai-ml, normalization, transformer]
private: false
---

# Layer Normalization

## Purpose

Normalization across features within a single example, making it well-suited to sequence models and Transformers.

## Core Model

- Computes mean and variance over the feature (hidden) dimension of a single token, independent of batch size or other examples.
- Unlike batch normalization, statistics do not depend on the batch, so behavior is identical at training and inference and stable for variable-length sequences.
- Applies learnable per-feature gain and bias after normalizing, letting the layer rescale and re-center the output.
- Removes the batch-statistics coupling that makes BatchNorm fragile for recurrent and attention models.

## Placement and Variants

- Post-norm (original Transformer) applies LayerNorm after the residual add; pre-norm applies it inside the residual branch before the sublayer.
- Pre-norm keeps residual gradients cleaner and enables training deep Transformers without careful warmup, which is why most modern LLMs use it.
- RMSNorm drops mean-centering and the bias term, rescaling only by the root-mean-square of activations, cutting compute while retaining stability.
- RMSNorm is widely adopted in recent large models (e.g. LLaMA-family) for its lower cost and comparable quality.

## Sources

- Layer Normalization - https://arxiv.org/abs/1607.06450
- Root Mean Square Layer Normalization - https://arxiv.org/abs/1910.07467

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
