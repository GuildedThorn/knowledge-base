---
summary: "DDD uses domain language, model boundaries, and strategic design to keep software aligned with business concepts."
status: active
tags: [reference, engineering, architecture, ddd]
private: false
---

# Domain-Driven Design and Bounded Contexts

## Purpose

DDD uses domain language, model boundaries, and strategic design to keep software aligned with business concepts.

## Core Model

- A bounded context is a boundary where a domain model and ubiquitous language have a specific meaning.
- Entities, value objects, aggregates, repositories, and domain services are tactical patterns, not mandatory ceremony.
- Context maps describe relationships such as partnership, customer/supplier, conformist, shared kernel, and anti-corruption layer.

## Engineering Notes

- Use DDD where domain complexity is the hard part; CRUD/admin screens often do not need it.
- Keep aggregate boundaries small and invariant-driven.
- Name code with the language domain experts use, and revisit it when the business language changes.

## Sources

- Domain-Driven Design Reference - https://domainlanguage.com/ddd/reference/
- Martin Fowler - Bounded Context - https://martinfowler.com/bliki/BoundedContext.html
- Microsoft - DDD microservice patterns - https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/

## Related

- [Software Architecture - Index](kb://06-reference-engineering-software-architecture-software-architecture-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
