---
summary: "Mobile GPU architecture that bins geometry into on-chip tiles to minimize external memory bandwidth and power."
status: active
tags: [reference, engineering, graphics, mobile-gpu, tiling]
private: false
---

# Tile-Based Deferred Rendering on Mobile GPUs

## Purpose

Mobile GPU architecture that bins geometry into on-chip tiles to minimize external memory bandwidth and power.

## Core Model

- The framebuffer is divided into small tiles (e.g. 16x16 or 32x32 pixels); each tile is rendered entirely within fast on-chip memory before being written to main memory once.
- Rendering runs in two phases: a binning (tiling) pass processes all geometry and records which primitives touch each tile into per-tile lists, then a per-tile fragment pass shades each tile.
- "Deferred" here means fragment shading is deferred until the tile list is complete, enabling hidden-surface removal that discards occluded fragments before shading (PowerVR's hallmark).
- Contrast with immediate-mode desktop GPUs that shade primitives as they arrive and rely on external-memory depth/color buffers.

## Engineering Notes

- Bandwidth win: the color and depth buffers live in on-chip tile memory during shading, so external memory sees mostly a single resolved color write per pixel instead of repeated read-modify-write blending traffic. This directly cuts power on battery devices.
- Render-pass load/store hints matter: on Vulkan/Metal, LOAD_OP_CLEAR/DONT_CARE avoids reading the old tile from memory, and STORE_OP_DONT_CARE for depth avoids writing it back.
- Avoid mid-frame reads of a render target you are still writing (framebuffer fetch is cheap, but breaking the tiled pass to sample it forces a flush).
- Minimize the number of render passes and geometry submitted, since binning cost scales with vertex count.

## Sources

- Imagination: A look at the PowerVR architecture — tile-based rendering - https://blog.imaginationtech.com/a-look-at-the-powervr-graphics-architecture-tile-based-rendering/
- Arm Mali GPU Best Practices - https://developer.arm.com/documentation/101897/latest/

---
## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
