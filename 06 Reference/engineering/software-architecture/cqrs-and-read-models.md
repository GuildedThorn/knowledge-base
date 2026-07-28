---
summary: "CQRS separates write-side commands from read-side queries when they have materially different models, scaling needs, or consistency requirements."
status: active
tags: [reference, engineering, architecture, cqrs]
private: false
---

# CQRS and Read Models

## Purpose

CQRS separates write-side commands from read-side queries when they have materially different models, scaling needs, or consistency requirements.

## Core Model

- Commands change state and enforce invariants; queries read optimized projections.
- Read models may be eventually consistent and rebuilt from events or change streams.
- CQRS is independent from event sourcing, though they are often paired.

## Engineering Notes

- Use CQRS where read/write complexity differs; do not split simple CRUD just to follow a pattern.
- Expose staleness expectations in UI and API contracts.
- Make projector replay idempotent, observable, and resumable.

## Sources

- Martin Fowler - CQRS - https://martinfowler.com/bliki/CQRS.html
- Microsoft - CQRS pattern - https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs
- EventStoreDB documentation - https://developers.eventstore.com/

## Related

- [Software Architecture - Index](kb://06-reference-engineering-software-architecture-software-architecture-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
