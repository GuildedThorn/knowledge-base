---
summary: "Modern LLM serving improves throughput and latency with KV-cache management, IO-aware attention kernels, batching, quantization, and GPU-specific runtimes."
status: active
tags: [reference, engineering, ai, ml, inference, gpu]
private: false
---

# LLM Serving: PagedAttention, FlashAttention, and TensorRT-LLM

## Purpose

LLM serving performance is dominated by memory movement, KV-cache growth, batching strategy, attention kernels, and GPU runtime efficiency. PagedAttention, FlashAttention, and TensorRT-LLM represent major production optimization directions.

## Core Model

- Prefill processes prompt tokens in parallel and is compute-heavy.
- Decode generates tokens autoregressively and is often memory-bandwidth/KV-cache bound.
- KV cache stores key/value tensors for previous tokens to avoid recomputing attention history.
- Attention kernels are performance-critical because naive attention creates heavy memory traffic.
- Serving runtimes combine batching, scheduling, parallelism, quantization, and specialized kernels.

## Technique Notes

- FlashAttention is IO-aware exact attention that reduces high-bandwidth-memory traffic by tiling around SRAM/cache behavior.
- PagedAttention manages KV cache in blocks/pages to reduce fragmentation and improve batching of variable-length requests.
- TensorRT-LLM provides NVIDIA-specific optimized engines, runtime components, quantization, in-flight batching, paged attention, and deployment integration.

## Operational Notes

- Measure time to first token separately from tokens per second.
- Track prefill/decode utilization, KV-cache memory, batch composition, queue time, and cancellation behavior.
- Quantization changes cost, memory, and quality; validate against task-specific evals.
- Long-context workloads stress KV cache and scheduler fairness.

## Sources

- FlashAttention official repository - https://github.com/Dao-AILab/flash-attention
- arXiv - FlashAttention - https://arxiv.org/abs/2205.14135
- vLLM / PagedAttention paper - https://arxiv.org/abs/2309.06180
- NVIDIA TensorRT-LLM docs - https://docs.nvidia.com/tensorrt-llm/index.html

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [LLM Inference, KV Cache, and Quantization](kb://06-reference-engineering-ai-ml-systems-llm-inference-kv-cache-and-quantization)
- [Evals and Benchmarks](kb://06-reference-engineering-ai-ml-systems-evals-and-benchmarks)
