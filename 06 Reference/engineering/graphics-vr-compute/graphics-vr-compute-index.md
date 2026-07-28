---
summary: "Rendering, GPU architecture, shaders, VR latency, OpenXR, spatial audio, terrain LOD, and profiling notes."
status: active
tags: [reference, engineering, graphics, vr, gpu, index]
private: false
---

# Graphics, VR, and GPU Compute - Index

## Purpose

Rendering, GPU architecture, shaders, VR latency, OpenXR, spatial audio, terrain LOD, and profiling notes.

## Notes

- [Compute Shaders and GPGPU](kb://06-reference-engineering-graphics-vr-compute-compute-shaders-and-gpgpu) - Compute shaders run general-purpose parallel work on the GPU, useful for simulation, culling, image processing, particles, and data transforms.
- [ECS, Scene Graphs, and Game Architecture](kb://06-reference-engineering-graphics-vr-compute-ecs-scene-graphs-and-game-architecture) - Game engines organize objects through scene graphs, entity-component systems, or hybrids; each changes data layout and update flow.
- [GPU and CPU Profiling Workflow](kb://06-reference-engineering-graphics-vr-compute-gpu-cpu-profiling-workflow) - Graphics performance work starts by identifying whether the frame is CPU-bound, GPU-bound, sync-bound, memory-bound, or presentation-bound.
- [GPU Architecture: SIMT, Memory, and Tensor Cores](kb://06-reference-engineering-graphics-vr-compute-gpu-architecture-simt-memory-and-tensor-cores) - GPU performance depends on SIMT execution, occupancy, memory hierarchy, bandwidth, synchronization, and specialized matrix/tensor hardware.
- [OpenXR Architecture](kb://06-reference-engineering-graphics-vr-compute-openxr-architecture) - OpenXR standardizes XR application interaction with runtimes through instances, sessions, spaces, swapchains, actions, and extensions.
- [PBR Materials and Lighting](kb://06-reference-engineering-graphics-vr-compute-pbr-materials-and-lighting) - Physically based rendering models materials and light with energy-aware parameters such as base color, roughness, metallic, normals, and environment lighting.
- [Rendering Pipeline and GPU Model](kb://06-reference-engineering-graphics-vr-compute-rendering-pipeline-gpu-model) - Modern GPUs transform scene data into pixels through programmable shader stages, fixed-function rasterization, memory hierarchies, and synchronization.
- [Shaders and GPU Programming](kb://06-reference-engineering-graphics-vr-compute-shaders-and-gpu-programming) - Shaders are small parallel programs that run across vertices, fragments, compute invocations, or other GPU stages.
- [Spatial Audio and HRTF](kb://06-reference-engineering-graphics-vr-compute-spatial-audio-and-hrtf) - Spatial audio uses position, orientation, attenuation, reverberation, and HRTFs to make sound behave plausibly in 3D space.
- [Terrain LOD and Clipmaps](kb://06-reference-engineering-graphics-vr-compute-terrain-lod-and-clipmaps) - Terrain rendering uses level-of-detail, tiling, clipmaps, streaming, and crack prevention to keep large worlds interactive.
- [VR Frame Pacing and Latency](kb://06-reference-engineering-graphics-vr-compute-vr-frame-pacing-and-latency) - VR comfort depends on predictable frame timing, low motion-to-photon latency, reprojection behavior, and avoiding sensor/visual mismatch.

## Related

- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Engineering Source Corpus](kb://06-reference-engineering-engineering-source-corpus)
- [Reference Map](kb://01-maps-reference-map)
