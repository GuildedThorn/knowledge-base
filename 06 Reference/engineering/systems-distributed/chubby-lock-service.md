---
summary: "Chubby is a coarse-grained distributed lock service built on Paxos providing reliable storage and leader election for Google systems."
status: active
tags: [reference, engineering, distributed-systems, coordination, locking]
private: false
---

# Chubby Lock Service

## Purpose

Chubby is a coarse-grained distributed lock service built on Paxos providing reliable storage and leader election for Google systems.

## Design and Data Model

- A Chubby cell is typically five replicas; a master is elected via Paxos and holds the lease while a majority supports it.
- The interface resembles a small filesystem of files and directories; nodes can hold advisory locks and small amounts of data.
- Locks are advisory and coarse-grained, intended to be held for hours or days (e.g. electing a primary), not for fine-grained mutual exclusion.
- Sequencers are opaque byte strings describing a lock's state; a holder passes one to a downstream service so stale requests can be rejected.

## Replication and Sessions

- All replicas keep a consistent copy of a simple database; writes go through Paxos, and reads are served by the master.
- Clients maintain sessions kept alive by KeepAlive RPCs; a lease expiry with no renewal invalidates the session and releases its locks and handles.
- Clients aggressively cache file data and metadata, and the master invalidates caches by blocking KeepAlive replies until acknowledgements return, keeping caches strongly consistent.
- Reducing load on this critical path motivated proxies and partitioning; many clients use Chubby chiefly as a highly available name service.

## Sources

- The Chubby Lock Service for Loosely-Coupled Distributed Systems - https://research.google/pubs/the-chubby-lock-service-for-loosely-coupled-distributed-systems/

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
