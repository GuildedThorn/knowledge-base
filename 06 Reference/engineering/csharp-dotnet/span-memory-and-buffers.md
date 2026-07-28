---
summary: "Span<T>, Memory<T>, and pooled buffers let .NET code process contiguous memory with fewer allocations and clearer ownership boundaries."
status: active
tags: [reference, engineering, dotnet, performance]
private: false
---

# Span, Memory, and Buffers

## Purpose

Span<T>, Memory<T>, and pooled buffers let .NET code process contiguous memory with fewer allocations and clearer ownership boundaries.

## Core Model

- Span<T> is stack-only byref-like memory; Memory<T> is heap-storable and can cross async boundaries.
- ArrayPool<T>, MemoryPool<T>, pipelines, and buffers reduce per-request allocations in hot paths.
- Slicing creates cheap views; it does not copy the underlying data.

## Engineering Notes

- Prefer simple arrays/strings first; reach for spans when profiling shows allocation or copy cost.
- Document ownership: who rents, who clears sensitive data, who returns, and whether the buffer can be retained.
- Avoid returning pooled arrays directly to callers unless the lifetime contract is explicit.

## Sources

- Microsoft - Memory and Span usage guidelines - https://learn.microsoft.com/en-us/dotnet/standard/memory-and-spans/memory-t-usage-guidelines
- Microsoft - Span<T> - https://learn.microsoft.com/en-us/dotnet/api/system.span-1
- Microsoft - ArrayPool<T> - https://learn.microsoft.com/en-us/dotnet/api/system.buffers.arraypool-1

## Related

- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
