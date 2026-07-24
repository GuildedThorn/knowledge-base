---
summary: Running local text embedding models from C#/.NET via ONNX Runtime — model choice, incremental re-embedding, brute-force cosine similarity at vault scale. Direct path to vr-brain's flagged SemanticIndex upgrade.
status: active
tags: [reference, ai, embeddings, dotnet]
private: false
---

## Purpose

vr-brain's `SemanticIndex` is TF-IDF + cosine similarity, explicitly flagged in [vr-brain Improvement Areas](kb://00-inbox-vr-brain-improvement-areas) as "a drop-in for real embeddings later" and the single highest-value relevance upgrade. This note is that research — how to actually run a local embedding model from C#/.NET with no cloud dependency. Compiled 2026-07-24.

## Why Embeddings Beat TF-IDF

TF-IDF is purely lexical — "car maintenance" and "vehicle upkeep" score near-zero similarity despite being the same topic, since there's no shared vocabulary. An embedding model is a neural encoder trained (via contrastive learning on paraphrase/retrieval data) to map any text into a dense vector such that semantically related texts land close together regardless of exact wording — cosine similarity between vectors approximates semantic relatedness. This is exactly `SemanticIndex`'s current weak axis: it'll miss "GPU thermal throttling" being related to "frame time spikes under load" with zero shared words. The swap is mechanical: replace the TF-IDF vectorizer with an encoder pass per note (cache the output), keep cosine similarity as the comparison (no change needed), keep the same top-K constellation-line logic downstream.

## Model Choice (2025-2026)

MTEB rankings churn fast and different MTEB versions aren't comparable — read the benchmark version, not just the score. For a CPU/consumer-GPU, few-thousand-notes workload:

| Model | Params | Dim | Max context | Notes |
|---|---|---|---|---|
| all-MiniLM-L6-v2 | 23M | 384 | 256 tok | lightest/fastest (~46MB), older architecture, "good enough" first swap |
| BGE-small-en-v1.5 | ~33M | 384 | 512 tok | similar footprint to MiniLM, higher retrieval scores, well-trodden ONNX path |
| nomic-embed-text-v1.5 | 137M | Matryoshka 768→64 | 8192 tok | long context sidesteps most chunking; truncatable output vector for cheaper storage |
| Qwen3-Embedding-0.6B | 600M | up to 1024, Matryoshka | 32K tok | near top of MTEB-eng-v2 (~70.7) among small models, Apache-2.0, best quality-per-size; still CPU-feasible in batch |
| EmbeddingGemma-300M | 300M | Matryoshka | — | solid sub-1B alternative, less mature ONNX tooling as of this research |

**Recommendation**: start with **BGE-small-en-v1.5** or **nomic-embed-text-v1.5** — both have mature ONNX exports, small enough for fast CPU batch embedding; nomic's 8K context sidesteps chunking for all but the longest notes. Qwen3-Embedding-0.6B is the upgrade path if relevance quality becomes the bottleneck — still CPU-fine for a few thousand notes, just slower per-note. **Chunking**: 256-512 token windows (MiniLM/BGE-small) silently truncate longer notes unless chunked (split by heading/paragraph, embed each, take max-similarity across chunks); 8K+ context models (nomic, Qwen3) let most notes embed whole, architecturally simpler and matching VaultSync's per-note model better.

## Running Locally from C#/.NET: ONNX Runtime (In-Process)

`Microsoft.ML.OnnxRuntime` is the natural fit — Microsoft's own cross-platform runtime, first-class C# API, NuGet package, no extra process.

- **Getting the model**: many embedding models already have ONNX exports on HuggingFace directly (`sentence-transformers/all-MiniLM-L6-v2` has an `onnx/` folder; `onnx-community/*-ONNX` repos for newer models). Where none exists, `optimum-cli export onnx --model <repo> ./out/` (HuggingFace's `optimum` library) — needed for Qwen3-Embedding as of this research.
- **Tokenization**: must exactly match training (WordPiece for BERT-family MiniLM/BGE, BPE for Qwen3/Gemma). `Microsoft.ML.Tokenizers` (NuGet, ML.NET family) ships `BertTokenizer`/`WordPieceTokenizer`/`Bpe` classes specifically for this — avoids hand-rolling a tokenizer.
- **Inference loop**: tokenize → build tensors (`input_ids`, `attention_mask`, sometimes `token_type_ids`) → `InferenceSession.Run()` → mean-pool token embeddings using the attention mask (standard for BERT-family sentence embeddings) → L2-normalize → cosine similarity reduces to a dot product.

## Alternative: Local Inference Server

**Sidecar** (llama.cpp/llama-cpp-python server, OpenAI-compatible `/v1/embeddings`): decouples model/runtime updates from the C#/Godot build entirely, at the cost of an extra process to launch/manage, HTTP overhead per call (negligible for batch, irrelevant off the per-frame path), and another thing that can fail to start (port conflicts, Python env) — a worse fit for vr-brain's self-contained offline framing.

**LLamaSharp** (in-process C#/.NET binding around llama.cpp, `LLamaEmbedder` class, GGUF, CPU/CUDA backends via NuGet): splits the difference — in-process like ONNX but wider immediate access to whatever the llama.cpp ecosystem supports, at the cost of less-standardized pooling/normalization conventions than `sentence-transformers`-derived ONNX exports.

**Given "no cloud dependency, self-contained": in-process ONNX Runtime is the better default** — embeds into the existing app with no process boundary. LLamaSharp is a reasonable fallback if a desired model only ships in GGUF.

## Vector Storage and Similarity Search

At a few thousand notes, **brute-force cosine similarity over an in-memory float array is the correct answer, full stop.** A 384-dim float32 vector is 1.5KB; 5,000 notes is ~7.5MB, trivially resident. A top-K query is one pass of 5,000 dot products (pre-normalize so cosine reduces to a dot product) — sub-to-low-millisecond even in managed C#, more so with `System.Numerics.Vector<T>`/SIMD. No case for FAISS/HNSW/a vector database here — that machinery earns its complexity in the tens-of-thousands-to-millions range, not thousands. Adding an ANN index at this scale is pure overengineering.

## Incremental Re-Embedding

Mirror VaultSync's existing snapshot/reparse model: persist an embeddings cache (JSON or a simple binary blob) keyed by **note slug + content hash** (SHA-256 of the body). Each sync: compute current hash per note; if slug+hash matches the cache, reuse the stored vector; otherwise re-embed and update; remove entries for deleted/renamed slugs. Version/key the cache by model name+dimension too — swapping models invalidates all prior vectors, and a full rebuild ("clear cache, re-run all") remains a simple fallback.

## GPU vs CPU

Sub-1B embedding models are small enough that CPU inference is typically fast enough for this batch-ish (not per-frame) workload — a few thousand notes at MiniLM/BGE-small size should embed in low-to-tens-of-seconds on a modern CPU, and incremental re-embedding after the first sync only touches changed notes. ONNX Runtime supports GPU execution providers if throughput ever bottlenecks: CUDA EP is most mature (NVIDIA-only); DirectML EP is Windows-only, hardware-agnostic but in "sustained engineering" (new work moving to WinML); **ROCm/MIGraphX EP (AMD, Linux) exist and are real but honestly less mature and less commonly used than CUDA — expect more friction and thinner community troubleshooting** on the fleet's actual AMD hardware. Given the batch nature of vault embedding, default to CPU and only reach for a GPU execution provider if sync times become annoying — don't provision GPU complexity up front.

## Related

- [vr-brain Improvement Areas](kb://00-inbox-vr-brain-improvement-areas)
- [vr-brain - Architecture](kb://07-projects-vr-brain-vr-brain-architecture)
- [Data Structures and Algorithms](kb://06-reference-data-structures-and-algorithms) — bloom filters/consistent hashing, adjacent data-structure reasoning
- [AI Coding Tools](kb://04-software-ai-coding-tools)
- [Reference Map](kb://01-maps-reference-map)
