---
summary: "Accelerating autoregressive generation by drafting tokens with a small model and verifying them with the target model."
status: active
tags: [reference, engineering, ai-ml, inference, decoding]
private: false
---

# Speculative Decoding

## Purpose

Accelerating autoregressive generation by drafting tokens with a small model and verifying them with the target model.

## How It Works

- A cheap draft model proposes several candidate continuation tokens; the large target model then scores all of them in a single parallel forward pass.
- A modified rejection-sampling rule accepts the longest prefix consistent with the target distribution and resamples the first rejected position, so output is provably identical in distribution to standard sampling from the target.
- Each verification step commits at least one token and often several, turning multiple sequential target-model calls into one batched call.

## Key Ideas

- Speedup depends on the acceptance rate: the closer the draft model's distribution is to the target's, the more tokens survive per step.
- Draft models are chosen for low latency and high agreement, e.g. a smaller model from the same family, a distilled model, or n-gram/lookahead heuristics.
- No target-model retraining is needed, and correctness is exact rather than approximate, distinguishing it from lossy shortcuts like early exit.

## Sources

- Fast Inference from Transformers via Speculative Decoding - https://arxiv.org/abs/2211.17192
- Accelerating LLM Decoding with Speculative Sampling - https://arxiv.org/abs/2302.01318

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
