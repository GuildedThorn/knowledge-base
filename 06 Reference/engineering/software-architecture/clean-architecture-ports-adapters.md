---
summary: "Ports-and-adapters architectures isolate domain/application logic from delivery and infrastructure details through explicit boundaries."
status: active
tags: [reference, engineering, architecture, clean-architecture]
private: false
---

# Clean Architecture, Hexagonal Architecture, and Ports/Adapters

## Purpose

Ports-and-adapters architectures isolate domain/application logic from delivery and infrastructure details through explicit boundaries.

## Core Model

- Core business logic depends on abstractions, not frameworks or transport details.
- Adapters translate HTTP, CLI, DB, message bus, or UI concerns into application ports.
- Dependency direction points inward toward the policies that should change least often.

## Engineering Notes

- Use boundaries to make tests and replacement easier, not to add layers mechanically.
- Keep DTOs, ORM entities, and transport schemas from becoming the domain model by accident.
- Prefer simple architecture for simple apps; the pattern pays off when boundaries are real.

## Sources

- Alistair Cockburn - Hexagonal Architecture - https://alistair.cockburn.us/hexagonal-architecture/
- Martin Fowler - Inversion of Control Containers - https://martinfowler.com/articles/injection.html
- Microsoft - Clean architecture eBook - https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures

## Related

- [Software Architecture - Index](kb://06-reference-engineering-software-architecture-software-architecture-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
