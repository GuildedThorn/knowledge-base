---
summary: "Speech systems convert audio to text and text to speech using acoustic features, sequence models, vocoders, alignment, and latency-aware pipelines."
status: active
tags: [reference, engineering, ai, speech]
private: false
---

# Speech: STT and TTS

## Purpose

Speech systems convert audio to text and text to speech using acoustic features, sequence models, vocoders, alignment, and latency-aware pipelines.

## Core Model

- STT pipelines handle capture, VAD, feature extraction, acoustic/language modeling, decoding, punctuation, and diarization where needed.
- TTS pipelines handle text normalization, pronunciation, prosody, acoustic generation, and vocoding.
- Streaming systems trade accuracy, latency, compute, and endpointing behavior.

## Engineering Notes

- Evaluate with noisy microphones, accents, domain vocabulary, push-to-talk mistakes, and real latency budgets.
- Keep privacy and retention rules explicit because raw audio is sensitive.
- For local systems, measure CPU/GPU load, memory, model load time, and wake/sleep behavior.

## Sources

- Whisper paper - https://arxiv.org/abs/2212.04356
- Piper TTS project - https://github.com/rhasspy/piper
- Hugging Face audio course - https://huggingface.co/learn/audio-course/chapter0/introduction

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
