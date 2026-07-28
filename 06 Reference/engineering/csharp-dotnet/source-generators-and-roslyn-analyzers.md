---
summary: "Roslyn analyzers inspect C# at compile time, while source generators add code to the compilation based on syntax and semantic models."
status: active
tags: [reference, engineering, csharp, roslyn]
private: false
---

# Source Generators and Roslyn Analyzers

## Purpose

Roslyn analyzers inspect C# at compile time, while source generators add code to the compilation based on syntax and semantic models.

## Core Model

- Analyzers report diagnostics and code fixes; generators create additional source without mutating user files.
- Incremental generators cache pipeline steps and scale better for large solutions.
- Generators are common for serializers, dependency injection, regex, logging, interop, and strongly typed clients.

## Engineering Notes

- Keep generated APIs debuggable and predictable; generated code is still production code.
- Use analyzers for architectural contracts and unsafe patterns that code review misses repeatedly.
- Benchmark build impact; generator convenience is not free in developer inner loops.

## Sources

- Microsoft - Source generators - https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators-overview
- Microsoft - Incremental generators cookbook - https://github.com/dotnet/roslyn/blob/main/docs/features/incremental-generators.cookbook.md
- Microsoft - Roslyn analyzers overview - https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview

## Related

- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
