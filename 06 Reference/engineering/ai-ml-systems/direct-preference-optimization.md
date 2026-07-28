---
summary: "A reward-model-free alignment method that optimizes a classification loss directly on preference pairs."
status: active
tags: [reference, engineering, ai-ml, alignment, preference]
private: false
---

# Direct Preference Optimization

## Purpose

A reward-model-free alignment method that optimizes a classification loss directly on preference pairs.

## Key Ideas

- DPO reparameterizes the RLHF objective so the optimal policy defines an implicit reward, eliminating a separately trained reward model.
- The implicit reward is the log-ratio of the policy to a frozen reference model, scaled by a temperature beta.
- Training minimizes a simple binary cross-entropy loss that raises the likelihood of preferred completions and lowers dispreferred ones on the same prompt.
- The reference model plays the role of RLHF's KL anchor, keeping the tuned policy close to the base distribution.

## Tradeoffs

- Removes the online RL loop (no sampling, no PPO), making training more stable and far simpler to implement than reward-model + PPO RLHF.
- beta controls how strongly the policy may diverge from the reference; too large under-fits preferences, too small risks over-optimization.
- Uses fixed offline preference pairs, so it cannot explore new completions the way on-policy RLHF can.
- Widely adopted as a practical alignment default, often matching or beating PPO-based RLHF on preference benchmarks.

## Sources

- Direct Preference Optimization - https://arxiv.org/abs/2305.18290

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
