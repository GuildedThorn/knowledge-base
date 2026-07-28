---
summary: "OpenXR standardizes XR application interaction with runtimes through instances, sessions, spaces, swapchains, actions, and extensions."
status: active
tags: [reference, engineering, vr, openxr]
private: false
---

# OpenXR Architecture

## Purpose

OpenXR standardizes XR application interaction with runtimes through instances, sessions, spaces, swapchains, actions, and extensions.

## Core Model

- Applications talk to an OpenXR runtime instead of headset-specific APIs.
- Spaces define coordinate relationships; actions abstract controller input from physical device layouts.
- Swapchains provide runtime-owned images that apps render into for composition.

## Engineering Notes

- Use action sets and semantic actions rather than hard-coded controller buttons.
- Treat reference spaces, recentering, and tracking loss as normal runtime states.
- Gate optional behavior by extension availability and runtime support.

## Sources

- OpenXR specification - https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html
- Khronos OpenXR overview - https://www.khronos.org/openxr/
- Godot OpenXR plugin docs - https://docs.godotengine.org/en/stable/tutorials/xr/openxr/index.html

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
