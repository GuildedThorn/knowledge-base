---
summary: "Sparsely-activated expert layers with a learned router that scale parameter count without proportional compute per token."
status: active
tags: [reference, engineering, ai-ml, sparsity, routing]
private: false
---

# Mixture-of-Experts Layers

## Purpose

Sparsely-activated expert layers with a learned router that scale parameter count without proportional compute per token.

## How It Works

- An MoE layer holds many parallel expert sub-networks (typically feed-forward blocks) plus a gating/router network.
- The router scores experts per token and dispatches each token to only the top-k experts (often k=1 or 2), so most experts stay inactive.
- Conditional computation decouples total parameters from per-token FLOPs, enabling very large models at fixed inference cost.
- Switch Transformers simplified routing to top-1, cutting routing overhead and improving stability at scale.

## Engineering Notes

- Each expert has a fixed capacity; tokens exceeding it are dropped or overflow, so load imbalance wastes compute.
- An auxiliary load-balancing loss encourages the router to spread tokens evenly across experts.
- Experts are commonly sharded across devices, making all-to-all communication the dominant cost in distributed training.
- Training can be unstable; techniques include router z-loss, careful initialization, and selective precision.

## Sources

- Outrageously Large Neural Networks (Sparsely-Gated MoE) - https://arxiv.org/abs/1701.06538
- Switch Transformers - https://arxiv.org/abs/2101.03961

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
