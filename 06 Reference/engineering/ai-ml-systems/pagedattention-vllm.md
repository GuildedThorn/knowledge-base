---
summary: "A KV-cache memory manager modeled on OS paging that reduces fragmentation and boosts LLM serving throughput."
status: active
tags: [reference, engineering, ai-ml, serving, kv-cache]
private: false
---

# PagedAttention and vLLM Serving

## Purpose

A KV-cache memory manager modeled on OS paging that reduces fragmentation and boosts LLM serving throughput.

## Core Model

- Splits each sequence's key-value cache into fixed-size blocks stored non-contiguously in GPU memory, tracked by a per-sequence block table.
- Eliminates the internal and external fragmentation that plagues contiguous KV allocation, letting near-100% of reserved cache memory hold live tokens.
- Attention kernels gather keys and values through the block table, so logically contiguous sequences can occupy physically scattered blocks.
- Enables copy-on-write block sharing across requests that share a prefix, cutting memory for beam search, parallel sampling, and shared system prompts.

## Engineering Notes

- vLLM is the reference serving engine built on PagedAttention, pairing it with continuous (iteration-level) batching that admits and retires requests each step.
- Higher effective memory utilization allows larger batch sizes, which raises aggregate throughput without hurting per-request latency much.
- Supports features like tensor parallelism, quantized weights, and an OpenAI-compatible API server for drop-in deployment.

## Sources

- Efficient Memory Management for LLM Serving (PagedAttention) - https://arxiv.org/abs/2309.06180
- vLLM documentation - https://docs.vllm.ai/

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
