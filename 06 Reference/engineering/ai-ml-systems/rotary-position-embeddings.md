---
summary: "A method encoding token positions by rotating query and key vectors, giving relative-position awareness that extrapolates."
status: active
tags: [reference, engineering, ai-ml, positional, attention]
private: false
---

# Rotary Position Embeddings

## Purpose

A method encoding token positions by rotating query and key vectors, giving relative-position awareness that extrapolates.

## How It Works

- RoPE multiplies query and key vectors by a position-dependent rotation matrix, pairing embedding dimensions and rotating each pair by an angle proportional to position.
- Rotation frequencies vary across dimension pairs, so low frequencies capture long-range position and high frequencies capture local order.
- Because the attention dot product of two rotated vectors depends only on their position difference, RoPE injects relative position without additive embeddings.

## Key Ideas

- Position is applied inside attention on Q and K only, not on values, and requires no learned position parameters.
- The relative-position property helps models generalize to sequence positions unseen at the trained context length.
- Extending context often uses frequency scaling such as NTK-aware or linear position interpolation to reduce degradation beyond training length.

## Engineering Notes

- RoPE is standard in many open LLM families (LLaMA, GPT-NeoX, PaLM-style) due to its simplicity and extrapolation behavior.
- Rotations are cheap and can be precomputed as cos/sin tables per position.

## Sources

- RoFormer: Enhanced Transformer with Rotary Position Embedding - https://arxiv.org/abs/2104.09864

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
