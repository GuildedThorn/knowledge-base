---
summary: "Replication improves availability and durability but introduces quorum, lag, conflict, and failover tradeoffs."
status: active
tags: [reference, engineering, distributed-systems, replication]
private: false
---

# Replication, Quorums, and Conflict Resolution

## Purpose

Replication improves availability and durability but introduces quorum, lag, conflict, and failover tradeoffs.

## Core Model

- Leader-follower, multi-leader, and leaderless replication make different write coordination choices.
- Read/write quorums use overlap to trade latency and consistency against fault tolerance.
- Conflicts require prevention, detection, merge rules, last-writer-wins, CRDTs, or human resolution.

## Engineering Notes

- Tie replication mode to data semantics: account balances and presence indicators do not need the same guarantees.
- Measure replication lag and expose it in dashboards and APIs where stale reads matter.
- Design conflict resolution before the first partition; after data diverges is too late.

## Sources

- Designing Data-Intensive Applications - https://dataintensive.net/
- Dynamo paper - https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
- Jepsen analyses - https://jepsen.io/analyses

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
