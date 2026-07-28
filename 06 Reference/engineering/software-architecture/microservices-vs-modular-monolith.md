---
summary: "Microservices optimize independent deployment and ownership at the cost of distributed-systems complexity; modular monoliths optimize local simplicity with internal boundaries."
status: active
tags: [reference, engineering, architecture, microservices]
private: false
---

# Microservices vs Modular Monolith

## Purpose

Microservices optimize independent deployment and ownership at the cost of distributed-systems complexity; modular monoliths optimize local simplicity with internal boundaries.

## Core Model

- A modular monolith can enforce clear module boundaries while staying in one deployable/process.
- Microservices add network calls, versioned APIs, distributed data, observability, deployment orchestration, and operational overhead.
- Team structure, ownership boundaries, scaling independence, and failure isolation should drive the choice.

## Engineering Notes

- Start modular unless independent deployment or scaling is already a real constraint.
- Extract services along stable bounded contexts, not database tables.
- Require service ownership, on-call, dashboards, SLIs, and deployment pipelines before splitting.

## Sources

- Martin Fowler - Microservices - https://martinfowler.com/articles/microservices.html
- Martin Fowler - Monolith First - https://martinfowler.com/bliki/MonolithFirst.html
- Microsoft - .NET microservices architecture - https://learn.microsoft.com/en-us/dotnet/architecture/microservices/

## Related

- [Software Architecture - Index](kb://06-reference-engineering-software-architecture-software-architecture-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
