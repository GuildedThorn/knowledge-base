---
summary: "Deep convolutional networks using identity skip connections that enable training of very deep architectures."
status: active
tags: [reference, engineering, ai-ml, cnn, skip-connections]
private: false
---

# Residual Networks (ResNet)

## Purpose

Deep convolutional networks using identity skip connections that enable training of very deep architectures.

## Core Model

- A residual block computes y = F(x) + x, so the layers learn a residual function relative to the identity mapping.
- Identity shortcuts add no parameters and let gradients flow directly to earlier layers, easing optimization.
- Addresses the degradation problem: without shortcuts, adding layers to a deep plain network raised training error.
- Enabled practical training of networks with 50, 101, and 152 layers, winning ImageNet 2015.

## Engineering Notes

- The bottleneck block uses 1x1, 3x3, 1x1 convolutions to cut compute while preserving representational capacity.
- When input and output dimensions differ, a projection (1x1 conv) shortcut matches shapes.
- Batch normalization after each convolution stabilizes training of the deep stacks.
- The follow-up "Identity Mappings" paper showed pre-activation (BN and ReLU before the conv) yields cleaner gradient flow and better very-deep results.

## Sources

- Deep Residual Learning for Image Recognition - https://arxiv.org/abs/1512.03385
- Identity Mappings in Deep Residual Networks - https://arxiv.org/abs/1603.05027

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
