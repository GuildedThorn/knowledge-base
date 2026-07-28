## Purpose

Reference for offline speech I/O — the exact stack vr-brain's `VoiceInput.cs`/`Tts.cs` already run, plus the streaming upgrade path neither uses yet. Compiled 2026-07-24.

## vr-brain's actual implementation (checked against source)

- **STT — `VoiceInput.cs`:** push-to-talk, not streaming. Captures mic at 16 kHz mono while a key is held; on release, shells out to `whisper-cli` (whisper.cpp) as a one-shot subprocess: `whisper-cli -m {model} -f {wav} -l en`. Model is `ggml-base.en.bin`, fetched once from `huggingface.co/ggerganov/whisper.cpp` on first launch and cached under `user://models/`. Config: `[voice] whisper_bin/model_path/model_url`.
- **TTS — `Tts.cs`:** shells out to `piper` per utterance — text piped to `piper`'s stdin, WAV piped to `pw-play` (PipeWire) for playback. Voice model `en_US-lessac-medium.onnx` from `huggingface.co/rhasspy/piper-voices`, also fetched once and cached. A new agent run or an explicit dismiss kills the in-flight `Process` (`entireProcessTree: true`) to cut speech off immediately. Config: `[voice] tts/tts_bin/tts_model_url`.
- **Both are one-shot subprocess invocations, not long-running streaming servers** — simple and zero-dependency (just needs the binaries on `PATH`), but each utterance pays full process-startup + model-load latency rather than amortizing it across a session.

## Streaming STT (not what vr-brain does, but the upgrade path)

- Whisper wasn't designed for streaming; a real-time pipeline wraps it: **Audio Source → Audio Buffer → Segmenter (VAD-driven chunking) → Whisper inference → post-processing → consumer**. The segmenter is what actually determines perceived latency — cutting audio into ~2-4s chunks on silence/VAD boundaries, not fixed windows, to avoid mid-word cuts.
- **faster-whisper** (CTranslate2 reimplementation): ~4x faster than stock Whisper on GPU, ~2x on CPU, same accuracy — the go-to if the current per-utterance subprocess latency becomes noticeable and a persistent server process is acceptable.
- **whisper.cpp** (what vr-brain already uses) is the right call for CPU/cross-platform/embedded — it also runs on Metal/CUDA/Vulkan, so a GPU path exists without switching runtimes if push-to-talk with a bigger model is ever wanted.
- Realistic budget for a fully streaming voice pipeline (STT→LLM→TTS): **~0.5-1.5s STT, ~1-2s until the LLM starts generating, ~0.2-0.5s until TTS starts speaking** — a few seconds end-to-end is normal even in a well-tuned 2026 local stack, not just vr-brain's simpler subprocess approach.

## TTS alternatives to Piper

- **Piper** (what vr-brain uses): fast, small, good-enough quality, trivial to self-host — the reason it's the default in most "fully local voice assistant" writeups alongside Whisper.
- **Orpheus, Kokoro**: newer open-source TTS models specifically tuned for low first-byte latency in streaming voice-agent contexts (streamed synthesis, not synthesize-then-play like Piper's current usage in `Tts.cs`). Worth a look if voice replies ever need to start speaking before the full sentence is synthesized.

## Related

- [vr-brain - Overview](kb://07-projects-vr-brain-vr-brain-overview)
- [Local Embedding Models for Semantic Search](kb://06-reference-local-embedding-models-for-semantic-search) — the other "local model instead of a cloud API" pattern already in vr-brain.

Sources:
- [Real-Time Streaming with Whisper: Guide to Low-Latency Speech-to-Text (2026)](https://www.saytowords.com/blogs/Real-Time-Streaming-with-Whisper/)
- [Whisper.cpp vs faster-whisper 2026: STT Speed Test](https://www.promptquorum.com/power-local-llm/local-whisper-stt-comparison-2026)
- [Local AI Voice Assistant Stack 2026: Whisper + Piper + Ollama](https://dev.to/kunal_d6a8fea2309e1571ee7/local-ai-voice-assistant-stack-2026-whisper-piper-ollama-wired-together-572l)
- [Announcing the fastest inference for realtime voice AI agents](https://www.together.ai/blog/the-fastest-inference-for-realtime-voice-ai-agents)
