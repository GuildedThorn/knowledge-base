---
summary: "Event sourcing stores immutable domain events as the source of truth and derives current state by replaying or projecting them."
status: active
tags: [reference, engineering, databases, event-sourcing]
private: false
---

# Event Sourcing Storage Model

## Purpose

Event sourcing stores immutable domain events as the source of truth and derives current state by replaying or projecting them.

## Core Model

- Events represent facts that happened, not commands or mutable rows.
- Aggregates use event streams to enforce local invariants.
- Read models/projections provide query-friendly views and can be rebuilt from the event log.

## Engineering Notes

- Version event schemas and write upcasters/migration strategies before the stream becomes long-lived.
- Keep idempotency and ordering rules explicit for projectors.
- Use snapshots for replay performance, but keep the event log authoritative.

## Sources

- Martin Fowler - Event Sourcing - https://martinfowler.com/eaaDev/EventSourcing.html
- EventStoreDB documentation - https://developers.eventstore.com/
- Microsoft - CQRS pattern - https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
