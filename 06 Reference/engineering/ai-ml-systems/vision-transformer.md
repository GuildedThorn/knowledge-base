---
summary: "An image classifier that treats fixed-size image patches as tokens fed to a standard Transformer encoder."
status: active
tags: [reference, engineering, ai-ml, vision, patches]
private: false
---

# Vision Transformer (ViT)

## Purpose

An image classifier that treats fixed-size image patches as tokens fed to a standard Transformer encoder.

## How It Works

- The image is split into fixed-size non-overlapping patches (e.g. 16x16); each patch is flattened and linearly projected to a token embedding.
- A learnable [class] token is prepended; its final-layer representation feeds the classification head.
- Learned 1D positional embeddings are added, since patches carry no inherent spatial order.
- The token sequence passes through a standard Transformer encoder, with no image-specific inductive bias like convolution.

## Tradeoffs

- Lacking convolutional locality/translation-equivariance priors, ViT underperforms CNNs when trained on mid-sized data alone.
- With large-scale pretraining (e.g. JFT-300M, ImageNet-21k), ViT matches or exceeds strong CNNs and transfers well.
- Attention scales quadratically with the number of patches, so patch size and resolution trade accuracy against compute.
- Established that a nearly unmodified Transformer can serve as a general vision backbone, spurring DeiT, Swin, and later variants.

## Sources

- An Image is Worth 16x16 Words - https://arxiv.org/abs/2010.11929
- google-research vision_transformer repo - https://github.com/google-research/vision_transformer

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
