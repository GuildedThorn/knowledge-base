---
summary: "LINQ unifies query syntax over in-memory objects, expression trees, and provider-backed data sources, but execution semantics vary by provider."
status: active
tags: [reference, engineering, csharp, linq]
private: false
---

# LINQ Query Model

## Purpose

LINQ unifies query syntax over in-memory objects, expression trees, and provider-backed data sources, but execution semantics vary by provider.

## Core Model

- LINQ-to-Objects runs delegates in-process; IQueryable providers translate expression trees into another query language or execution plan.
- Deferred execution means query construction and query execution are separate events.
- Operators like Select, Where, GroupBy, Join, Any, All, and Aggregate describe a pipeline, not necessarily a materialized collection.

## Engineering Notes

- Know when queries cross a boundary: EF Core, OData, and custom providers may reject or client-evaluate patterns that LINQ-to-Objects accepts.
- Materialize intentionally with ToList/ToArray when lifetime, multiple enumeration, or transaction boundaries matter.
- Benchmark hot LINQ paths; allocations and iterator layering are usually fine, but tight loops may need spans or explicit loops.

## Sources

- Microsoft - LINQ in C# - https://learn.microsoft.com/en-us/dotnet/csharp/linq/
- Microsoft - Standard query operators - https://learn.microsoft.com/en-us/dotnet/csharp/linq/standard-query-operators/
- Microsoft - Expression trees - https://learn.microsoft.com/en-us/dotnet/csharp/advanced-topics/expression-trees/

## Related

- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
