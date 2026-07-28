---
summary: ".NET GC trades automatic memory management for allocation patterns, pause behavior, generations, and large-object-heap concerns."
status: active
tags: [reference, engineering, dotnet, gc]
private: false
---

# Garbage Collection and Allocation

## Purpose

.NET GC trades automatic memory management for allocation patterns, pause behavior, generations, and large-object-heap concerns.

## Core Model

- The GC is generational: short-lived objects are collected cheaply, while long-lived objects move into older generations.
- Server GC and workstation GC target different throughput/latency profiles.
- Large objects and pinned memory can fragment heaps and hurt pause behavior.

## Engineering Notes

- Measure allocation rate, not just retained memory; high allocation can saturate GC even without a leak.
- Use object pooling for expensive or frequent transient buffers, but do not pool tiny objects blindly.
- Use dotnet-counters, dotnet-trace, PerfView, and Visual Studio profilers to verify GC hypotheses.

## Sources

- Microsoft - Fundamentals of garbage collection - https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/fundamentals
- Microsoft - Server garbage collection - https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/workstation-server-gc
- Microsoft - .NET diagnostics tools - https://learn.microsoft.com/en-us/dotnet/core/diagnostics/

## Related

- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
