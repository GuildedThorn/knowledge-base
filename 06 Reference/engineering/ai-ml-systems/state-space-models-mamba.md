---
summary: "Selective structured state space sequence models offering linear-time alternatives to attention for long sequences."
status: active
tags: [reference, engineering, ai-ml, ssm, long-context]
private: false
---

# State Space Models and Mamba

## Purpose

Selective structured state space sequence models offering linear-time alternatives to attention for long sequences.

## Core Model

- A state space model maps an input sequence to output through a latent state evolving by a linear recurrence, discretized from continuous-time parameters A, B, C.
- S4 makes this practical at scale with structured (diagonal-plus-low-rank) state matrices and stable initialization (HiPPO) for long-range memory.
- Compute and memory scale linearly with sequence length, versus quadratic self-attention, enabling very long contexts.

## Key Ideas

- Mamba adds selectivity: the recurrence parameters become input-dependent, letting the model choose what to remember or ignore per token.
- Input-dependent parameters break the fixed-convolution form, so Mamba uses a hardware-aware parallel scan computed in fast SRAM to stay efficient.
- The result is a simplified attention-free block with content-based reasoning and constant-memory autoregressive inference.

## Tradeoffs

- Linear-time recurrence gives fast, cheap long-sequence inference but lacks attention's explicit all-pairs lookup, which can matter for exact recall tasks.
- Hybrid designs interleave SSM and attention layers to combine strengths.

## Sources

- Mamba: Linear-Time Sequence Modeling - https://arxiv.org/abs/2312.00752
- Efficiently Modeling Long Sequences with S4 - https://arxiv.org/abs/2111.00396

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
