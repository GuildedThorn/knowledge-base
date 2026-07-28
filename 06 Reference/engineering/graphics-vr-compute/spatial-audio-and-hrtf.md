---
summary: "Spatial audio uses position, orientation, attenuation, reverberation, and HRTFs to make sound behave plausibly in 3D space."
status: active
tags: [reference, engineering, audio, vr]
private: false
---

# Spatial Audio and HRTF

## Purpose

Spatial audio uses position, orientation, attenuation, reverberation, and HRTFs to make sound behave plausibly in 3D space.

## Core Model

- HRTFs model how head, torso, and ears filter sound from different directions.
- Binaural rendering, ambisonics, room effects, and occlusion add immersion but cost CPU and design effort.
- VR audio must stay stable during head movement to avoid breaking presence.

## Engineering Notes

- Use mono sources for positional audio and stereo/ambisonic beds for environmental ambience.
- Tune distance curves and occlusion by scene scale, not default engine values.
- Profile audio DSP alongside rendering; audio glitches are comfort issues in VR.

## Sources

- Steam Audio documentation - https://valvesoftware.github.io/steam-audio/
- Godot audio streams and buses - https://docs.godotengine.org/en/stable/tutorials/audio/index.html
- OpenAL Soft HRTF docs - https://openal-soft.org/

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
