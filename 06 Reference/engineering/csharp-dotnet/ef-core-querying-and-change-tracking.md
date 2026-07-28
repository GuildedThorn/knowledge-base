---
summary: "EF Core maps object graphs to relational data, translating LINQ where possible and tracking entity changes for persistence."
status: active
tags: [reference, engineering, dotnet, ef-core]
private: false
---

# EF Core Querying and Change Tracking

## Purpose

EF Core maps object graphs to relational data, translating LINQ where possible and tracking entity changes for persistence.

## Core Model

- DbContext is a unit-of-work boundary; it tracks entities, original values, relationships, and pending changes.
- LINQ queries are translated to SQL by providers, so supported operations depend on provider capabilities.
- Lazy loading, eager Include, split queries, projections, and tracking/no-tracking queries have different performance profiles.

## Engineering Notes

- Default to projections for read models; do not load full entities when a DTO is enough.
- Watch N+1 queries, client evaluation, cartesian explosion, and long-lived DbContext instances.
- Use migrations carefully: schema history is operational infrastructure, not just app code.

## Sources

- Microsoft - EF Core documentation - https://learn.microsoft.com/en-us/ef/core/
- Microsoft - EF Core querying - https://learn.microsoft.com/en-us/ef/core/querying/
- Microsoft - EF Core change tracking - https://learn.microsoft.com/en-us/ef/core/change-tracking/

## Related

- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
