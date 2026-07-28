---
summary: "Computer vision models extract visual features for classification, detection, segmentation, tracking, and multimodal understanding."
status: active
tags: [reference, engineering, ai, computer-vision]
private: false
---

# Computer Vision: CNNs and Vision Transformers

## Purpose

Computer vision models extract visual features for classification, detection, segmentation, tracking, and multimodal understanding.

## Core Model

- CNNs use local convolutional filters, pooling, and hierarchical feature maps.
- Vision Transformers split images into patches and apply transformer attention.
- Detection and segmentation add localization outputs beyond image-level labels.

## Engineering Notes

- Evaluate on domain-specific lighting, camera, compression, occlusion, and class distribution.
- Track data labeling quality; visual models inherit annotation errors and blind spots.
- Use augmentation carefully so it reflects plausible deployment variation.

## Sources

- ImageNet classification with deep CNNs - https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
- An Image is Worth 16x16 Words - https://arxiv.org/abs/2010.11929
- PyTorch vision docs - https://pytorch.org/vision/stable/index.html

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
