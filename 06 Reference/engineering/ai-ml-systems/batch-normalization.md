---
summary: "A training technique that normalizes layer inputs over each mini-batch to stabilize and accelerate deep-network training."
status: active
tags: [reference, engineering, ai-ml, normalization, training]
private: false
---

# Batch Normalization

## Purpose

A training technique that normalizes layer inputs over each mini-batch to stabilize and accelerate deep-network training.

## How It Works

- For each feature (channel), BatchNorm computes the mean and variance across the mini-batch and normalizes activations to zero mean and unit variance.
- Two learnable parameters, scale (gamma) and shift (beta), restore representational capacity the normalization would otherwise remove.
- During training, statistics come from the current batch; running averages of mean and variance are accumulated for use at inference.
- At inference the fixed running statistics replace batch statistics, so outputs no longer depend on other examples in a batch.

## Key Ideas

- BatchNorm smooths the optimization landscape, permitting higher learning rates and reducing sensitivity to initialization.
- It has a mild regularizing effect because each example is normalized using noisy batch statistics.
- Placement (before or after the activation) and interaction with dropout and weight decay affect results.

## Engineering Notes

- Small or highly variable batch sizes degrade statistics; GroupNorm, LayerNorm, or synchronized BatchNorm are used for small-batch or distributed training.
- Folding BatchNorm into preceding convolution weights at inference removes its runtime cost.

## Sources

- Batch Normalization - https://arxiv.org/abs/1502.03167

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
