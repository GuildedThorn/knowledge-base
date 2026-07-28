---
summary: "A one-shot weight quantization method using approximate second-order information to compress LLMs to low bit-widths."
status: active
tags: [reference, engineering, ai-ml, quantization, compression]
private: false
---

# GPTQ Post-Training Quantization

## Purpose

A one-shot weight quantization method using approximate second-order information to compress LLMs to low bit-widths.

## How It Works

- Quantizes weights one layer at a time, minimizing the squared error between the original and quantized layer outputs on a small calibration set.
- Uses approximate second-order (Hessian) information to decide rounding, quantizing columns sequentially while updating the remaining weights to compensate for the introduced error.
- Applies Cholesky-based reformulation and lazy batch updates to keep the Hessian computation numerically stable and fast on billion-parameter models.
- Requires no retraining or gradient descent; a single pass over calibration data produces the quantized model.

## Tradeoffs

- Reaches 3-4 bit weights with modest accuracy loss; 4-bit is typically near-lossless, while 3-bit degrades more, especially on smaller models.
- Weight-only quantization shrinks memory and bandwidth but leaves activations in higher precision, so gains are largest in memory-bound decoding.
- AWQ offers an alternative that protects salient weight channels identified via activation magnitudes, often preserving accuracy at low bit-widths with a simpler scheme.

## Sources

- GPTQ: Accurate Post-Training Quantization for GPTs - https://arxiv.org/abs/2210.17323
- AWQ: Activation-aware Weight Quantization - https://arxiv.org/abs/2306.00978

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
