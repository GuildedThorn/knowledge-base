---
summary: "ZooKeeper provides wait-free coordination primitives via a replicated hierarchical namespace with ordered atomic broadcast."
status: active
tags: [reference, engineering, distributed-systems, coordination, consensus]
private: false
---

# Apache ZooKeeper Coordination Service

## Purpose

ZooKeeper provides wait-free coordination primitives via a replicated hierarchical namespace with ordered atomic broadcast.

## Data Model

- State is a hierarchy of znodes resembling a filesystem; each znode holds small data (typically under 1 MB) and metadata including a version.
- Ephemeral znodes exist only for the lifetime of the creating session; sequential znodes get a monotonically increasing suffix assigned by the leader.
- Clients set one-time watches on znodes to receive a notification when data or children change, avoiding polling.
- Reads are served from any replica and may be stale; a `sync` call forces a replica up to date before a subsequent read.

## Consistency and Replication

- Writes are linearizable and totally ordered through the ZAB atomic broadcast protocol; a quorum (majority) must acknowledge each proposal.
- One server is elected leader and sequences all state changes; followers serve reads and forward writes to the leader.
- The API is wait-free: operations never block on other clients, and ordering guarantees let clients build blocking primitives themselves.

## Recipes

- Locks: create an ephemeral sequential znode and watch the next-lowest to acquire in queue order, avoiding herd effects.
- Leader election and group membership follow the same sequential-plus-ephemeral pattern.
- Configuration management and barriers are built on watches over shared znodes.

## Sources

- ZooKeeper: Wait-free coordination (Hunt et al.) - https://www.usenix.org/legacy/event/atc10/tech/full_papers/Hunt.pdf
- ZooKeeper Documentation - https://zookeeper.apache.org/doc/current/

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
