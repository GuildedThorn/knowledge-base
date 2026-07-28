---
summary: "Raft is a consensus algorithm designed for understandability, using leader election, log replication, and safety rules."
status: active
tags: [reference, engineering, distributed-systems, consensus]
private: false
---

# Consensus: Raft

## Purpose

Raft is a consensus algorithm designed for understandability, using leader election, log replication, and safety rules.

## Core Model

- Raft decomposes consensus into leader election, log replication, and safety.
- A leader appends log entries, replicates to followers, and commits once entries are stored on a majority.
- Terms and voting rules prevent older leaders from overwriting committed entries.

## Engineering Notes

- Operators need to understand quorum, election timeouts, disk latency, snapshots, and membership changes.
- A five-node cluster tolerates two failures but increases write quorum latency compared with three nodes.
- Do not place a quorum in one failure domain; consensus cannot rescue correlated outages.

## Sources

- Raft official site - https://raft.github.io/
- Ongaro and Ousterhout - In Search of an Understandable Consensus Algorithm - https://raft.github.io/raft.pdf
- etcd Raft design - https://etcd.io/docs/latest/learning/

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
