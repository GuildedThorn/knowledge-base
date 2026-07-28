---
summary: "The immutable ordered log is a foundational abstraction unifying replication, stream processing, and data integration."
status: active
tags: [reference, engineering, distributed-systems, log, streaming]
private: false
---

# The Log: Unifying Data Integration

## Purpose

The immutable ordered log is a foundational abstraction unifying replication, stream processing, and data integration.

## Core Model

- A log is an append-only sequence of records ordered by time, where the offset acts as a logical clock timestamping each entry.
- State machine replication: if replicas apply the same deterministic operations from a shared log in the same order, they reach identical state.
- Both the primary-backup ("apply then log the result") and consensus ("log then apply") approaches reduce to agreeing on log contents and order.
- The log serves as the single source of truth; consumers materialize whatever derived views, indexes, or caches they need from it.

## Key Ideas

- Log-centric data integration replaces N-squared point-to-point ETL pipelines with a central log every system publishes to and subscribes from.
- Stream-table duality: a table is the accumulated result of a log of changes, and a changelog captures every update to a table; each can be reconstructed from the other.
- Reprocessing is trivial: rebuild a downstream view by replaying the log from the start, enabling schema changes and bug fixes without upstream coordination.
- Decoupling producers from consumers in time and space lets systems evolve independently while staying eventually consistent.

## Sources

- The Log: What every engineer should know (Kreps) - https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
