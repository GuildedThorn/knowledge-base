---
summary: "C# async/await composes non-blocking I/O with Task-based APIs; it is a concurrency tool, not a magic performance switch."
status: active
tags: [reference, engineering, csharp, async]
private: false
---

# Async/Await and Task-Based Asynchrony

## Purpose

C# async/await composes non-blocking I/O with Task-based APIs; it is a concurrency tool, not a magic performance switch.

## Core Model

- `async` methods compile into state machines that resume after awaited operations complete.
- Awaiting I/O frees the current thread; CPU-bound work still needs explicit scheduling, parallelism, or backpressure.
- SynchronizationContext and TaskScheduler influence continuation placement, which matters in UI, ASP.NET, and library code.

## Engineering Notes

- Use async all the way through call chains; blocking on `.Result` or `.Wait()` can deadlock and burns thread-pool capacity.
- Accept and pass CancellationToken for external I/O, timers, service shutdown, and user-initiated cancellation.
- Prefer ValueTask only when profiling proves allocation pressure; misuse can make APIs harder to consume safely.

## Sources

- Microsoft - Asynchronous programming with async and await - https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/
- Microsoft - Task asynchronous programming model - https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model
- Stephen Toub - ConfigureAwait FAQ - https://devblogs.microsoft.com/dotnet/configureawait-faq/

## Related

- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
