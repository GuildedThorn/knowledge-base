---
summary: "Khronos's low-overhead, explicit graphics and compute API with manual memory, synchronization, and command buffers."
status: active
tags: [reference, engineering, graphics, vulkan, api]
private: false
---

# Vulkan Explicit GPU API

## Purpose

Khronos's low-overhead, explicit graphics and compute API with manual memory, synchronization, and command buffers.

## Core Model

- Vulkan trades driver convenience for explicit control: the application manages memory, synchronization, and state that OpenGL hid inside the driver.
- Work is recorded into command buffers, allocated from command pools, then submitted to queues drawn from queue families (graphics, compute, transfer, present).
- Command buffers can be recorded once and resubmitted, and recorded from multiple threads in parallel, which is a primary source of Vulkan's CPU scalability.
- Pipeline state is largely baked into immutable pipeline objects at creation time, moving validation cost out of the hot path.

## Synchronization and Memory

- The application is responsible for all GPU-GPU and CPU-GPU synchronization; there is no implicit ordering between queue submissions.
- Pipeline barriers order memory access and handle image layout transitions; semaphores synchronize between queue submissions; fences signal the CPU that GPU work finished; events give fine-grained intra-command-buffer sync.
- Memory is allocated explicitly from heaps with declared properties (device-local, host-visible, coherent); buffers and images bind into that memory.
- Descriptor sets, allocated from descriptor pools, bind resources to shaders; the layout must match the pipeline's declared bindings.
- Validation layers catch misuse in development and are stripped in release for zero overhead.

## Sources

- Vulkan Specification - https://registry.khronos.org/vulkan/
- Vulkan Tutorial - https://vulkan-tutorial.com/
- Vulkan Guide - https://vkguide.dev/

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
