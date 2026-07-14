## Purpose

Document the `surround-panner` project and its relationship to the `mixxx-surround-fork` experiment.

## Summary

surround-panner is a dependency-free Node.js (ESM) 7.1 spatial-audio engine: VBAP (Vector Base Amplitude Panning) panning, a WAV encoder, a synth, and generated demo tracks, all rendered offline with zero runtime dependencies (no npm packages, no ffmpeg, no audio device needed to build). GitHub: [GuildedThorn/surround-panner](https://github.com/GuildedThorn/surround-panner).

## How the Panning Works

`panner.mjs` implements constant-power pairwise VBAP on a horizontal 8-speaker ring (FL/FR at ±30°, FC at 0°, SL/SR at ±90°, BL/BR at ±135°, LFE non-directional):

- `vbapGains(azimuth)` uses a tangent-law formula between the two adjacent speakers bracketing the source angle — at most 2 speakers active at once, with gains² always summing to 1 (constant power).
- Elevation (`spatialGains`) is faked as "phantom height" on this height-less layout — a power-domain cos²/sin² blend between the VBAP azimuth gains and an equal-power spread across all 7 directional speakers (0° elevation = pure VBAP, ±90° = uniform "everywhere").
- Distance uses a simple inverse-law gain, clamped at 1.
- `render()` does a per-sample loop at 48kHz.

`wav.mjs` is a hand-rolled `WAVE_FORMAT_EXTENSIBLE` encoder with correct `dwChannelMask` bits (`0x63F` for 7.1) so players/ffmpeg see a real 7.1 layout rather than 8 anonymous channels, plus an ATSC-style 7.1→stereo downmix (center/surrounds −3dB, LFE omitted) for preview files.

## Repo Layout

- `panner.mjs`: the VBAP engine
- `wav.mjs`: WAV encode/downmix
- `synth.mjs`: ADSR envelopes, note sequencer, shared voices
- `demo.mjs`: orbit/elevation/distance/LFE showcase
- `testsuite.mjs`: speaker-ID check
- `music.mjs` / `edm.mjs`: two full generative tracks (A-minor 110bpm chill, C-minor 128bpm EDM with sidechain/riser/drop)
- `playlist.mjs`: concatenates all demos into `all_in_one_7dot1.wav`
- `selfcheck.mjs`: prints the VBAP gain table
- `panner.test.mjs` / `wav.test.mjs`: `node --test` suite — 28 tests covering VBAP constant-power, L-R symmetry, continuity, elevation blend, EXTENSIBLE header layout, and downmix coefficients
- `speaker-room.html`: browser-based demo/visualization page
- rendered `.wav`/`.raw` output files for demos and previews

## Status

Per the README (dated 2026-07-03): the engine and elevation model are complete, all 28 tests pass and have been verified analytically (ffprobe/astats), but the output has **not yet been played on real 7.1 speakers** — that's the explicit next step. Roadmap ideas: room-tuning trim/delay, gain smoothing, block-based rendering (~10x speedup), real-time streaming playback, true 7.1.4 height via layered VBAP, Doppler, seedable generative music, 24-bit/float32 output.

## Relationship to mixxx-surround-fork

`~/Downloads/mixxx-surround-fork` (a shallow fork of [mixxxdj/mixxx](https://github.com/mixxxdj/mixxx), branch `surround-fork`) is a **separate, related** effort — not shared code. Where surround-panner is algorithmic/offline VBAP spatialization, the Mixxx fork's `SURROUND-FORK.md` and `docs/surround/` plan a completely different thing: **live, discrete, channel-based multichannel DJ mixing** in the Mixxx DJ software. The pitch is that Mixxx already does real-time discrete N-channel mixing via its "stems" feature but sums to stereo at the deck — the fork's idea is to extend stems through the output stage instead of collapsing to stereo, routing each deck/stem to independent 5.1/7.1 output channels live, as a performance instrument, rather than a studio/offline workflow.

Status of the Mixxx fork is research/planning only — `docs/surround/00-PROJECT.md` (goal/novelty/estimates), `01-FINDINGS.md` (file:line references into Mixxx's current channel-handling code), `02-PLAN.md` (milestones), `03-DECK-COUNT.md` — no engine code written yet. Both projects share the same underlying interest (real discrete multichannel audio, not stereo-only or algorithmic upmixing) but are independent codebases at very different maturity: surround-panner is a working, tested, offline engine awaiting its first real-speaker listen; the Mixxx fork is a fully-scoped plan with zero code.

## Stack

Plain Node.js ESM, no dependencies, `node --test` for the test suite.

## Related

- [[01 Maps/Projects Map|Projects Map]]
