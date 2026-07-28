---
summary: "A bidirectional Transformer encoder pretrained with masked-token and next-sentence objectives for transfer to NLP tasks."
status: active
tags: [reference, engineering, ai-ml, pretraining, encoder]
private: false
---

# BERT and Masked Language Modeling

## Purpose

A bidirectional Transformer encoder pretrained with masked-token and next-sentence objectives for transfer to NLP tasks.

## Pretraining Objectives

- Masked Language Modeling (MLM) randomly masks ~15% of input tokens and trains the model to predict the originals from bidirectional context.
- Of masked positions, 80% become [MASK], 10% a random token, 10% unchanged, reducing pretrain/fine-tune mismatch.
- Next Sentence Prediction (NSP) trains a binary classifier on whether sentence B actually follows sentence A.
- Later work (e.g. RoBERTa) found NSP largely unnecessary, but it was part of the original recipe.

## Architecture and Use

- BERT is a Transformer encoder only; it reads the whole sequence at once rather than left-to-right.
- Inputs combine token, segment, and positional embeddings; a [CLS] token aggregates sequence-level representation.
- Bidirectional conditioning lets each token attend to both left and right context, unlike causal language models.
- Fine-tuning adds a lightweight task head (classification, span extraction, tagging) and updates all weights on downstream data.

## Sources

- BERT: Pre-training of Deep Bidirectional Transformers - https://arxiv.org/abs/1810.04805
- Google Research BERT repo - https://github.com/google-research/bert

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
