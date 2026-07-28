---
summary: "Joint image-text embedding learned by contrastive matching over web-scale pairs enabling zero-shot classification."
status: active
tags: [reference, engineering, ai-ml, multimodal, contrastive]
private: false
---

# CLIP Contrastive Vision-Language Pretraining

## Purpose

Joint image-text embedding learned by contrastive matching over web-scale pairs enabling zero-shot classification.

## How It Works

- Two encoders, an image encoder (ResNet or ViT) and a text encoder (Transformer), map inputs into a shared embedding space.
- Training uses a symmetric InfoNCE contrastive loss over a batch: the model matches each image to its true caption against all other captions, and vice versa.
- A learned temperature scales the cosine-similarity logits before the softmax over the batch.
- Trained on ~400M image-text pairs scraped from the web, using natural language as a broad, cheap supervision signal.

## Zero-Shot Transfer

- Classification is framed as retrieval: candidate class names are turned into text prompts (e.g. "a photo of a {label}") and embedded.
- The image embedding is compared to each class-prompt embedding, and the highest cosine similarity wins, with no task-specific training.
- Prompt engineering and prompt ensembling measurably improve zero-shot accuracy.
- CLIP embeddings became a reusable backbone for retrieval, captioning, and text-conditioned image generation guidance.

## Sources

- Learning Transferable Visual Models From Natural Language Supervision - https://arxiv.org/abs/2103.00020
- OpenAI CLIP repo - https://github.com/openai/CLIP

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
