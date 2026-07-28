---
summary: "The Task Parallel Library, thread pool, locks, channels, and concurrent collections provide different concurrency tools for different failure modes."
status: active
tags: [reference, engineering, dotnet, concurrency]
private: false
---

# Threading, TPL, and Concurrency

## Purpose

The Task Parallel Library, thread pool, locks, channels, and concurrent collections provide different concurrency tools for different failure modes.

## Core Model

- Concurrency is about overlapping work; parallelism is about running CPU work simultaneously.
- ThreadPool scheduling, work stealing, async continuations, and blocking calls all interact under load.
- Data races are correctness bugs even when they are rare; memory visibility and synchronization must be deliberate.

## Engineering Notes

- Use async I/O for waiting, Parallel/PLINQ for CPU-bound loops, Channels/Dataflow for producer-consumer pipelines, and locks for small critical sections.
- Avoid sync-over-async and long blocking calls on thread-pool threads in servers.
- Treat cancellation, bounded queues, and backpressure as part of the concurrency design, not cleanup.

## Sources

- Microsoft - Managed threading - https://learn.microsoft.com/en-us/dotnet/standard/threading/
- Microsoft - Task Parallel Library - https://learn.microsoft.com/en-us/dotnet/standard/parallel-programming/task-parallel-library-tpl
- Microsoft - System.Threading.Channels - https://learn.microsoft.com/en-us/dotnet/core/extensions/channels

## Related

- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
