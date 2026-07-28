---
summary: "LLM inference performance is dominated by prefill/decode phases, KV cache memory, batching, quantization, and memory bandwidth."
status: active
tags: [reference, engineering, ai, inference]
private: false
---

# LLM Inference, KV Cache, and Quantization

## Purpose

LLM inference performance is dominated by prefill/decode phases, KV cache memory, batching, quantization, and memory bandwidth.

## Core Model

- Prefill processes input context; decode generates tokens autoregressively.
- KV cache stores attention keys/values so prior tokens do not need full recomputation.
- Quantization reduces memory and bandwidth by using lower-precision weights or activations.

## Engineering Notes

- Measure tokens/sec, time-to-first-token, latency percentiles, memory, and throughput under realistic batching.
- Choose quantization based on quality impact for the task, not only benchmark speed.
- Keep context size under control; long contexts increase memory and prefill cost.

## Sources

- vLLM documentation - https://docs.vllm.ai/
- llama.cpp documentation - https://github.com/ggml-org/llama.cpp
- Hugging Face text generation inference - https://huggingface.co/docs/text-generation-inference/index

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
