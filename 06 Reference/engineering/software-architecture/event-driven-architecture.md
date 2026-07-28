---
summary: "Event-driven systems communicate facts through messages or streams, reducing temporal coupling while adding ordering, schema, and replay concerns."
status: active
tags: [reference, engineering, architecture, events]
private: false
---

# Event-Driven Architecture

## Purpose

Event-driven systems communicate facts through messages or streams, reducing temporal coupling while adding ordering, schema, and replay concerns.

## Core Model

- Events describe something that happened; commands request something to happen.
- Brokers/logs decouple producers and consumers but do not remove contracts.
- Ordering is usually scoped by partition/key, not global.

## Engineering Notes

- Design event names, schema evolution, idempotent consumers, dead-letter handling, and replay semantics upfront.
- Use outbox/inbox patterns to bridge database commits and message publication.
- Avoid event soup: not every internal method call should become a distributed event.

## Sources

- Martin Fowler - What do you mean by Event-Driven? - https://martinfowler.com/articles/201701-event-driven.html
- Microsoft - Event-driven architecture - https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven
- Kafka documentation - https://kafka.apache.org/documentation/

## Related

- [Software Architecture - Index](kb://06-reference-engineering-software-architecture-software-architecture-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
