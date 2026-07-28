---
summary: "Architecture patterns, API design, DDD, event-driven systems, testing strategy, ADRs, and legacy-system evolution notes."
status: active
tags: [reference, engineering, architecture, software-design, index]
private: false
---

# Software Architecture - Index

## Purpose

Architecture patterns, API design, DDD, event-driven systems, testing strategy, ADRs, and legacy-system evolution notes.

## Notes

- [Architecture Decision Records](kb://06-reference-engineering-software-architecture-architecture-decision-records) - ADRs capture important design decisions, context, options, consequences, and status in a durable lightweight format.
- [Clean Architecture, Hexagonal Architecture, and Ports/Adapters](kb://06-reference-engineering-software-architecture-clean-architecture-ports-adapters) - Ports-and-adapters architectures isolate domain/application logic from delivery and infrastructure details through explicit boundaries.
- [CQRS and Read Models](kb://06-reference-engineering-software-architecture-cqrs-and-read-models) - CQRS separates write-side commands from read-side queries when they have materially different models, scaling needs, or consistency requirements.
- [Dependency Injection and Composition Root](kb://06-reference-engineering-software-architecture-dependency-injection-composition-root) - Dependency injection separates object construction from behavior; the composition root wires concrete implementations at application startup.
- [Domain-Driven Design and Bounded Contexts](kb://06-reference-engineering-software-architecture-domain-driven-design-bounded-contexts) - DDD uses domain language, model boundaries, and strategic design to keep software aligned with business concepts.
- [Event-Driven Architecture](kb://06-reference-engineering-software-architecture-event-driven-architecture) - Event-driven systems communicate facts through messages or streams, reducing temporal coupling while adding ordering, schema, and replay concerns.
- [Feature Flags and Progressive Delivery](kb://06-reference-engineering-software-architecture-feature-flags-progressive-delivery) - Feature flags decouple deployment from release, enabling gradual rollout, experiments, kill switches, and operational control.
- [LLVM Compiler Pipeline](kb://06-reference-engineering-software-architecture-llvm-compiler-pipeline) - LLVM-based compilers typically lex, parse, build an AST, emit LLVM IR, optimize, JIT or lower to object code, and attach debug information.
- [Microservices vs Modular Monolith](kb://06-reference-engineering-software-architecture-microservices-vs-modular-monolith) - Microservices optimize independent deployment and ownership at the cost of distributed-systems complexity; modular monoliths optimize local simplicity with internal boundaries.
- [OpenAPI Contracts](kb://06-reference-engineering-software-architecture-openapi-contracts) - OpenAPI describes HTTP APIs in a machine-readable contract for documentation, clients, servers, validation, and governance.
- [Refactoring Legacy Systems](kb://06-reference-engineering-software-architecture-refactoring-legacy-systems) - Legacy-system evolution is controlled change: characterization tests, seams, strangler patterns, and small reversible refactors.
- [REST API Design](kb://06-reference-engineering-software-architecture-rest-api-design) - REST-style APIs model resources, representations, links, methods, status codes, caching, and stateless interactions over HTTP.
- [Testing Pyramid and Contract Tests](kb://06-reference-engineering-software-architecture-testing-pyramid-and-contract-tests) - A healthy test strategy layers fast unit tests, focused integration tests, contract tests, and a smaller number of end-to-end workflows.

## Related

- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Engineering Source Corpus](kb://06-reference-engineering-engineering-source-corpus)
- [Reference Map](kb://01-maps-reference-map)
