---
summary: "Aligning language models to human preferences by training a reward model and optimizing the policy with PPO."
status: active
tags: [reference, engineering, ai-ml, alignment, reward-model]
private: false
---

# Reinforcement Learning from Human Feedback

## Purpose

Aligning language models to human preferences by training a reward model and optimizing the policy with PPO.

## Pipeline

- Start from a supervised fine-tuned (SFT) model that already follows instructions in a basic form.
- Collect preference data: humans rank or compare multiple model completions for the same prompt.
- Train a reward model on these comparisons to output a scalar score predicting human preference, typically via a Bradley-Terry ranking loss.
- Optimize the SFT policy with reinforcement learning (PPO) to maximize reward-model score.

## Engineering Notes

- A KL-divergence penalty against the frozen SFT reference keeps the policy from drifting into degenerate, high-reward-but-off-distribution text (reward hacking).
- The reward model is a proxy and can be over-optimized, so reward, KL budget, and validation quality are monitored together.
- InstructGPT showed RLHF-tuned models were preferred over a much larger base model, demonstrating alignment gains beyond raw scale.
- The core idea traces to learning reward models from human preference comparisons in deep RL, later adapted to language.

## Sources

- Training Language Models to Follow Instructions (InstructGPT) - https://arxiv.org/abs/2203.02155
- Deep RL from Human Preferences - https://arxiv.org/abs/1706.03741

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
