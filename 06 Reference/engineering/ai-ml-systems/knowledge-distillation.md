---
summary: "Training a compact student model to mimic the soft output distribution of a larger teacher network."
status: active
tags: [reference, engineering, ai-ml, compression, teacher-student]
private: false
---

# Knowledge Distillation

## Purpose

Training a compact student model to mimic the soft output distribution of a larger teacher network.

## Core Model

- A large trained teacher produces soft targets (full probability distributions), and a smaller student is trained to reproduce them.
- Soft targets carry "dark knowledge": relative probabilities across wrong classes encode teacher similarity structure that hard labels omit.
- A temperature T softens the teacher (and student) softmax, spreading probability mass so inter-class relationships are more informative.
- The distillation loss combines a soft-target term (KL to the temperature-scaled teacher) with a standard hard-label cross-entropy term.

## Tradeoffs

- The student's capacity bounds how much it can absorb; too small a student underfits the teacher regardless of signal quality.
- Because soft-target gradients scale by 1/T^2, that term is typically reweighted to balance against the hard-label loss.
- DistilBERT applied this to BERT, retaining ~97% of language-understanding performance at ~40% fewer parameters and ~60% faster inference.
- Distillation yields smaller, cheaper models for deployment and can transfer across architectures, not just shrink the same family.

## Sources

- Distilling the Knowledge in a Neural Network - https://arxiv.org/abs/1503.02531
- DistilBERT - https://arxiv.org/abs/1910.01108

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
