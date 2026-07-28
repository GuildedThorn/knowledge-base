---
summary: "Low-rank adapter matrices injected into frozen weights to fine-tune large models with a fraction of trainable parameters."
status: active
tags: [reference, engineering, ai-ml, fine-tuning, adapters]
private: false
---

# LoRA Parameter-Efficient Fine-Tuning

## Purpose

Low-rank adapter matrices injected into frozen weights to fine-tune large models with a fraction of trainable parameters.

## How It Works

- Freezes the pretrained weight matrix W and learns a low-rank update dW = B A, where A and B have inner rank r much smaller than the layer dimensions.
- Only A and B are trained, reducing trainable parameters and optimizer state by orders of magnitude versus full fine-tuning.
- The update is scaled by alpha/r; at inference dW can be merged back into W, adding zero latency.
- Because the base weights are untouched, one frozen model can host many swappable task-specific adapters.

## Engineering Notes

- Rank r trades capacity against cost; small ranks (4-16) often suffice, with larger r for harder domain shifts.
- Target-module choice matters: applying LoRA to attention projections (q, k, v, o) is common, and extending to MLP layers can help.
- QLoRA fine-tunes adapters on top of a 4-bit NF4-quantized frozen base, using paged optimizers to fit large models on a single GPU.
- QLoRA preserves near-full-precision quality while drastically cutting memory, enabling 65B-class fine-tuning on modest hardware.

## Sources

- LoRA: Low-Rank Adaptation of Large Language Models - https://arxiv.org/abs/2106.09685
- QLoRA: Efficient Finetuning of Quantized LLMs - https://arxiv.org/abs/2305.14314

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
