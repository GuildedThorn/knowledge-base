---
summary: "The application, geometry, rasterization, and pixel stages that turn a 3D scene into a frame on GPU hardware."
status: active
tags: [reference, engineering, graphics, pipeline, rasterization]
private: false
---

# The Real-Time Rendering Graphics Pipeline

## Purpose

The application, geometry, rasterization, and pixel stages that turn a 3D scene into a frame on GPU hardware.

## Core Model

- The pipeline is conceptually four stages: application, geometry processing, rasterization, and pixel processing.
- The application stage runs on the CPU, handling culling, scene updates, and draw-call submission.
- Geometry processing transforms vertices through model, view, and projection matrices into clip and screen space.
- Rasterization converts assembled primitives into fragments; pixel processing shades and composites them into the framebuffer.

## How It Works

- The vertex shader is programmable, computing per-vertex position and attributes; optional tessellation and geometry shaders add or reshape primitives.
- Clipping, perspective divide, and viewport mapping bridge geometry output to the fixed-function rasterizer.
- The rasterizer interpolates vertex attributes across each primitive, producing per-pixel fragments with depth values.
- The fragment shader computes color; the output-merger applies depth/stencil tests and blending before writing pixels.

## Engineering Notes

- Per-primitive (vertex) work scales with mesh complexity, while per-pixel (fragment) work scales with screen coverage and overdraw.
- Fixed-function stages (rasterizer, depth test, blend) are configured, not coded; programmable stages run shader programs.
- Modern APIs like Vulkan expose the pipeline explicitly as immutable pipeline-state objects to reduce driver overhead.

## Sources

- Real-Time Rendering (book) - https://www.realtimerendering.com/
- LearnOpenGL: Hello Triangle - https://learnopengl.com/Getting-started/Hello-Triangle
- Vulkan Specification - https://registry.khronos.org/vulkan/

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
