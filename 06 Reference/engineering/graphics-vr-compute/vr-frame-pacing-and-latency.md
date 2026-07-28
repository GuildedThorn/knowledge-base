---
summary: "VR comfort depends on predictable frame timing, low motion-to-photon latency, reprojection behavior, and avoiding sensor/visual mismatch."
status: active
tags: [reference, engineering, vr, latency]
private: false
---

# VR Frame Pacing and Latency

## Purpose

VR comfort depends on predictable frame timing, low motion-to-photon latency, reprojection behavior, and avoiding sensor/visual mismatch.

## Core Model

- VR targets strict refresh deadlines; missed frames cause reprojection, judder, or discomfort.
- Motion-to-photon latency includes tracking, simulation, rendering, compositing, display scanout, and persistence.
- Foveation, fixed timestep discipline, asynchronous reprojection, and stable frametimes matter more than peak FPS.

## Engineering Notes

- Budget CPU and GPU frame time separately with margin below the headset refresh interval.
- Avoid blocking asset loads, shader compilation, GC spikes, and main-thread stalls during interaction.
- Test with the actual runtime/headset because compositor behavior varies by platform.

## Sources

- OpenXR specification - https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html
- Meta Quest performance guidelines - https://developer.oculus.com/resources/vrc-quest-performance-1/
- Godot XR docs - https://docs.godotengine.org/en/stable/tutorials/xr/index.html

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
