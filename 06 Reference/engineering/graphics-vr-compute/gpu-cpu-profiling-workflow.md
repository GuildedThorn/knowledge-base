---
summary: "Graphics performance work starts by identifying whether the frame is CPU-bound, GPU-bound, sync-bound, memory-bound, or presentation-bound."
status: active
tags: [reference, engineering, graphics, profiling]
private: false
---

# GPU and CPU Profiling Workflow

## Purpose

Graphics performance work starts by identifying whether the frame is CPU-bound, GPU-bound, sync-bound, memory-bound, or presentation-bound.

## Core Model

- CPU profiling shows script, scene traversal, physics, rendering submission, allocation, and job scheduling cost.
- GPU captures show passes, draw calls, shaders, overdraw, bandwidth, barriers, and occupancy.
- Frame pacing tools reveal jitter that average FPS hides.

## Engineering Notes

- Use repeatable scenes and camera paths before comparing optimizations.
- Capture both CPU and GPU timelines; one side can wait on the other.
- Track p50/p95/p99 frame time, not just mean FPS.

## Sources

- RenderDoc documentation - https://renderdoc.org/docs/index.html
- AMD Radeon GPU Profiler - https://gpuopen.com/rgp/
- NVIDIA Nsight Graphics - https://developer.nvidia.com/nsight-graphics

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
