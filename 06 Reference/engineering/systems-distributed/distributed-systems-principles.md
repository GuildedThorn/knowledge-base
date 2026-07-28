---
summary: "Distributed systems coordinate multiple computers under partial failure, latency, concurrency, and independent clocks."
status: active
tags: [reference, engineering, distributed-systems, systems]
private: false
---

# Distributed Systems Principles

## Purpose

Distributed systems coordinate multiple computers under partial failure, latency, concurrency, and independent clocks.

## Core Model

- The network is not reliable, latency is not zero, bandwidth is finite, and clocks are not globally consistent.
- Partial failure is the defining property: one component can be broken while others continue.
- Replication, partitioning, consensus, leases, queues, and logs are tools for controlling failure modes.

## Engineering Notes

- Design APIs around retries, idempotency, timeouts, backpressure, and observability from the first draft.
- Prefer explicit consistency and durability contracts over vague terms like real-time or eventually.
- Model degraded modes: stale reads, duplicate messages, split brain, clock skew, and regional outage.

## Sources

- Designing Data-Intensive Applications - https://dataintensive.net/
- MIT 6.824 Distributed Systems - https://pdos.csail.mit.edu/6.824/
- Google SRE Book - https://sre.google/sre-book/table-of-contents/

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
