---
summary: HRTF, convolution vs algorithmic reverb, occlusion/obstruction, Godot 4's actual (non-HRTF) panning, and Steam Audio's fragmented Godot integration status.
status: active
tags: [reference, gamedev, godot, audio, vr]
private: false
---

## Purpose

Positional/spatial audio reference for VR — no spatial audio is currently documented or implemented anywhere in vr-brain despite its voice agent (TTS output), ambient soundscape, and the separate [surround-panner](kb://07-projects-surround-panner-surround-panner-overview) VBAP interest. Compiled 2026-07-24.

## HRTF Fundamentals

A Head-Related Transfer Function is a filter — one per ear — modeling how the pinna, head, and torso alter a sound's amplitude/phase depending on arrival direction before it reaches the eardrum, capturing the physical acoustic shadowing/reflection/resonance of the listener's own body. Convolving a dry mono signal with a direction-matched HRTF pair produces interaural time difference (ITD), interaural level difference (ILD), and the spectral notches/peaks the brain uses for elevation and front/back discrimination.

**Why headphones/headsets specifically need it**: loudspeakers deliver natural ITD/ILD for free (each ear picks up a physically distinct signal shaped by the room and head) — headphones bypass that entirely, both ears get an identical pre-mixed signal, so without HRTF convolution a "3D" mix collapses to left/right panning inside the head, no front/back, no elevation, no externalization. This is precisely why it matters for a headset app and is largely moot for desk speakers.

**Main limitation**: HRTFs are highly individual — pinna/head/ear-canal geometry measurably changes the filter. Generic/averaged datasets (MIT KEMAR, CIPIC, SADIE) work reasonably for most listeners but reliably cause front-back confusion and elevation errors for a meaningful minority, since those cues live in fine spectral detail generic ears don't reproduce for everyone. This is the same class of problem VBAP/surround work sidesteps by not needing HRTFs at all.

## Convolution vs Algorithmic Reverb

**Convolution reverb** convolves the dry signal with an impulse response — a recording/simulation of how a real or virtual space responds to a short impulse — reproducing the space's full frequency/time fingerprint with high realism. CPU-heavy, and effectively a fixed asset (changing the room = loading a different IR, not tweaking parameters).

**Algorithmic/procedural reverb** synthesizes a reverb tail from delay lines + comb/all-pass filters + feedback (Schroeder/Moorer/FDN topologies) — cheap, no asset dependency, fully runtime-adjustable.

**Tradeoff for a dynamic VR environment**: convolution wins on realism but is expensive and static; algorithmic reverb is the practical choice when the environment changes live (procedural geometry, reconfiguring panels) since parameters can be driven by scene state without swapping assets. Godot's built-in `AudioEffectReverb` is algorithmic — no first-class convolution reverb node in core.

## Distance Attenuation and Occlusion/Obstruction

Distance falloff: inverse, inverse-square, or logarithmic — true inverse-square (physically correct) drops very fast near the source and very slowly far away; games often use gentler curves for legibility.

- **Occlusion**: a solid object *fully* blocks the direct path — standard cheap implementation is a low-pass filter (highs cut, since low frequencies diffract through/around obstacles more) plus a volume cut, driven by a listener↔source line-of-sight raycast.
- **Obstruction**: *partial* blocking — a lighter version of the same filter/volume reduction, often derived from a percentage of blocked rays via multi-ray sampling rather than a boolean hit.
- **Practical tier**: single/multi-raycast per frame or tick, mapping hits to filter cutoff/volume — cheap, robust, good enough for panel/terminal-scale scenes.
- **Heavy tier**: geometric acoustic simulation — ray/path tracing sound against actual level geometry for physically accurate occlusion/diffraction/reverb. This is what Steam Audio does — name it as the escalation path, not something to hand-roll.

## Godot 4's Actual Built-In Capabilities

`AudioStreamPlayer3D`: `attenuation_model` (`INVERSE_DISTANCE`/`INVERSE_SQUARE_DISTANCE`/`LOGARITHMIC`/`DISABLED`), `unit_size`/`max_distance` for falloff shaping, `doppler_tracking` (`DISABLED`/`IDLE_STEP`/`PHYSICS_STEP` — physics-step is the stable choice, needs enabling on the listener too). Built-in occlusion-via-lowpass is just `attenuation_filter_cutoff_hz` (default 5000 Hz) / `attenuation_filter_db` (default −24 dB) — distance-driven muffling, not real geometry.

**Important correction**: there is **no** `PANNING_STRATEGY` project setting offering a "stereo vs HRTF panning" toggle in current Godot 4. What exists is `panning_strength` driving a cosine-based stereo panning law (WebAudio `StereoPannerNode`-style), falling back to SPCAP (Speaker-Placement Correction Amplitude) for 5.1/7.1 — **amplitude panning, not real HRTF convolution**. A proper `SpatialAudioModel` resource (loadable HRTF datasets) was proposed in [godot-proposals #4377](https://github.com/godotengine/godot-proposals/issues/4377) in 2022 and remains open/unimplemented as of 4.5/4.6. Godot's panning is head-related in a loose geometric sense, not individualized HRTF.

`AudioEffectReverb` on a bus is algorithmic; environmental "reverb zones" are DIY via `Area3D` reassigning a player's output bus on region entry — not automatic. `AudioEffectCapture` is unrelated to spatialization (taps mixed samples into a ring buffer for scripts — visualization/voice-chat capture, not occlusion/reverb).

**Current-cycle audio changes**: 4.4 added runtime WAV loading; 4.6 (Jan 2026) shipped OpenXR 1.1 and fixed `AudioListener3D` velocity being properly counted for Doppler when the *listener* moves (not just the source) — directly relevant since the VR headset is the listener.

## Steam Audio — The Escalation Path

Valve open-sourced Steam Audio (Apache 2.0) in early 2024: real HRTF personalization, physically-based occlusion/transmission/reflections via ray tracing against actual geometry, ambisonic rendering. **Godot integration is community-maintained and fragmented, not official**:

- `stechyo/godot-steam-audio` — engine module (requires recompiling Godot), targets 4.3, Linux incomplete, **archived Oct 2024**.
- `V-Sekai/godot-steamaudio` — fork continuing the module approach, unrealized roadmap toward GPU/CPU ray-traced reflections.
- `alxsc/godot_steamaudio` — GDExtension (no recompile needed), targets 4.4, alpha quality, implements ambisonics/occlusion/transmission/attenuation/reflections/dynamic geometry; maintainer explicitly under-maintained, open to forks; Linux/Windows confirmed.
- `VirtualBrightPlayz/GodotSharpSteamAudio` — a C# binding, targets 4.2 — notable given vr-brain is C#/.NET, but check update cadence before depending on it.

Bottom line: real but immature/unofficial — the answer to "when raycast-occlusion + algorithmic reverb + amplitude panning isn't enough," not a drop-in today. Budget integration risk and expect to pin a specific fork/commit.

## Why This Matters for vr-brain Specifically

The voice agent's TTS currently outputs flat, non-positional stereo — in a headset that reads as "voice in my head" rather than coming from the panel/avatar. Routing TTS playback through an `AudioStreamPlayer3D` parented to the panel/avatar transform (sane `doppler_tracking`/`unit_size`/`max_distance` defaults) immediately buys distance falloff and left/right/front/back panning matched to head orientation via `AudioListener3D` on the XR camera. Ambient soundscape sources (CRT SOC display hum, terminal panel clicks, cosmic ambience) benefit the same way — discrete positioned emitters instead of a flat 2D bed, `attenuation_filter_cutoff_hz` giving cheap muffling for panels behind the listener or occluded by geometry via a listener→source raycast. Since Godot's panning is amplitude-based (not individualized HRTF), directional accuracy will be "good enough for room-scale UI cueing" but won't nail elevation/front-back for every listener — a reasonable v1, with Steam Audio (or a custom HRTF convolution bus) as the later upgrade if front-back confusion on panel/CRT cues becomes a real usability complaint.

## Related

- [surround-panner - Overview](kb://07-projects-surround-panner-surround-panner-overview)
- [Music Production and Surround Sound](kb://10-hobbies-music-production-and-surround-sound)
- [vr-brain - Architecture](kb://07-projects-vr-brain-vr-brain-architecture)
- [VR Performance Optimization](kb://06-reference-vr-performance-optimization)
- [Godot Engine Architecture and Patterns](kb://06-reference-godot-engine-architecture-and-patterns)
- [Reference Map](kb://01-maps-reference-map)
