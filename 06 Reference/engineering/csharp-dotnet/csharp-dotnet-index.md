---
summary: "C#/.NET language, runtime, libraries, diagnostics, web, data, and deployment reference notes."
status: active
tags: [reference, engineering, csharp, dotnet, index]
private: false
---

# C# and .NET - Index

## Purpose

C#/.NET language, runtime, libraries, diagnostics, web, data, and deployment reference notes.

## Notes

- [.NET Testing, Benchmarking, and Diagnostics](kb://06-reference-engineering-csharp-dotnet-dotnet-testing-benchmarking-diagnostics) - .NET ships test frameworks, BenchmarkDotNet ecosystem support, and diagnostics tools for traces, counters, dumps, and managed profiling.
- [ASP.NET Core Middleware and Minimal APIs](kb://06-reference-engineering-csharp-dotnet-aspnet-core-middleware-and-minimal-apis) - ASP.NET Core request handling is a middleware pipeline ending in endpoints; Minimal APIs expose compact route definitions over the same hosting model.
- [Async/Await and Task-Based Asynchrony](kb://06-reference-engineering-csharp-dotnet-async-await-task-asynchrony) - C# async/await composes non-blocking I/O with Task-based APIs; it is a concurrency tool, not a magic performance switch.
- [C# Language and .NET Release Model](kb://06-reference-engineering-csharp-dotnet-csharp-language-and-dotnet-release-model) - C# evolves with the .NET SDK; language features, runtime libraries, and deployment targets should be pinned together in project documentation.
- [EF Core Querying and Change Tracking](kb://06-reference-engineering-csharp-dotnet-ef-core-querying-and-change-tracking) - EF Core maps object graphs to relational data, translating LINQ where possible and tracking entity changes for persistence.
- [Garbage Collection and Allocation](kb://06-reference-engineering-csharp-dotnet-garbage-collection-and-allocation) - .NET GC trades automatic memory management for allocation patterns, pause behavior, generations, and large-object-heap concerns.
- [Generics, Variance, and Constraints](kb://06-reference-engineering-csharp-dotnet-generics-variance-and-constraints) - C# generics provide type-safe reusable code; constraints and variance define what generic APIs can promise and safely substitute.
- [Interop, P/Invoke, and SafeHandle](kb://06-reference-engineering-csharp-dotnet-interop-pinvoke-and-safehandle) - .NET interop bridges managed code to native libraries; SafeHandle, marshaling, and lifetime ownership decide whether it stays reliable.
- [LINQ Query Model](kb://06-reference-engineering-csharp-dotnet-linq-query-model) - LINQ unifies query syntax over in-memory objects, expression trees, and provider-backed data sources, but execution semantics vary by provider.
- [NativeAOT, Trimming, and Single-File Deployment](kb://06-reference-engineering-csharp-dotnet-nativeaot-trimming-single-file) - Modern .NET deployment can publish trimmed, single-file, or NativeAOT binaries, but dynamic features must be designed for static analysis.
- [Nullable Reference Types](kb://06-reference-engineering-csharp-dotnet-nullable-reference-types) - Nullable reference types make nullability part of the C# type flow analysis so APIs can express and check null contracts.
- [Source Generators and Roslyn Analyzers](kb://06-reference-engineering-csharp-dotnet-source-generators-and-roslyn-analyzers) - Roslyn analyzers inspect C# at compile time, while source generators add code to the compilation based on syntax and semantic models.
- [Span, Memory, and Buffers](kb://06-reference-engineering-csharp-dotnet-span-memory-and-buffers) - Span<T>, Memory<T>, and pooled buffers let .NET code process contiguous memory with fewer allocations and clearer ownership boundaries.
- [Threading, TPL, and Concurrency](kb://06-reference-engineering-csharp-dotnet-threading-tpl-concurrency) - The Task Parallel Library, thread pool, locks, channels, and concurrent collections provide different concurrency tools for different failure modes.

## Related

- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Engineering Source Corpus](kb://06-reference-engineering-engineering-source-corpus)
- [Reference Map](kb://01-maps-reference-map)
