---
summary: "Game engines organize objects through scene graphs, entity-component systems, or hybrids; each changes data layout and update flow."
status: active
tags: [reference, engineering, game-dev, architecture]
private: false
---

# ECS, Scene Graphs, and Game Architecture

## Purpose

Game engines organize objects through scene graphs, entity-component systems, or hybrids; each changes data layout and update flow.

## Core Model

- Scene graphs naturally represent hierarchy, transforms, ownership, and editor structure.
- ECS separates identity, component data, and systems, often improving cache locality for large homogeneous workloads.
- Hybrid engines use nodes for authoring and specialized data-oriented systems for hot paths.

## Engineering Notes

- Use scene graphs for authored objects and ECS/data-oriented structures for thousands of similar dynamic entities.
- Avoid deep per-frame tree walks when data can be batched or cached.
- Profile update order, transform propagation, allocation, and scripting overhead.

## Sources

- Game Programming Patterns - https://gameprogrammingpatterns.com/
- Unity DOTS ECS docs - https://docs.unity3d.com/Packages/com.unity.entities@latest
- Godot nodes and scenes - https://docs.godotengine.org/en/stable/getting_started/step_by_step/nodes_and_scenes.html

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
