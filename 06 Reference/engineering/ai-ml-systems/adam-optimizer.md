---
summary: "An adaptive first-order optimizer combining momentum and per-parameter RMS scaling with bias correction."
status: active
tags: [reference, engineering, ai-ml, optimization, gradient-descent]
private: false
---

# Adam Optimizer

## Purpose

An adaptive first-order optimizer combining momentum and per-parameter RMS scaling with bias correction.

## How It Works

- Adam maintains two exponential moving averages per parameter: the first moment (mean of gradients) and the second moment (mean of squared gradients).
- The first moment supplies momentum; the second moment scales each parameter's step by the inverse root of its recent gradient magnitude.
- Both estimates start at zero and are bias-biased toward zero early on, so bias-correction terms divide by (1 - beta^t) to unbias them.
- The update divides the corrected first moment by the square root of the corrected second moment plus epsilon, giving adaptive per-parameter learning rates.

## Key Ideas

- Default hyperparameters (beta1 ~0.9, beta2 ~0.999, epsilon ~1e-8) work broadly, reducing tuning versus plain SGD.
- Adam couples L2 regularization with the adaptive scaling, which weakens weight decay for large-gradient parameters.
- AdamW decouples weight decay from the gradient update, applying decay directly to weights for more consistent regularization and better generalization.

## Engineering Notes

- AdamW is the standard optimizer for training large transformers.
- Adaptive methods can generalize slightly worse than tuned SGD+momentum on some vision tasks; learning-rate warmup and schedules matter.

## Sources

- Adam: A Method for Stochastic Optimization - https://arxiv.org/abs/1412.6980
- Decoupled Weight Decay Regularization (AdamW) - https://arxiv.org/abs/1711.05101

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
