---
summary: "Viewstamped Replication provides state machine replication with primary-backup and view changes to tolerate crash failures."
status: active
tags: [reference, engineering, distributed-systems, replication, consensus]
private: false
---

# Viewstamped Replication

## Purpose

Viewstamped Replication provides state machine replication with primary-backup and view changes to tolerate crash failures.

## Core Model

- A group of 2f+1 replicas tolerates f crash failures; one replica is the primary for a given view, the rest are backups.
- In normal operation the primary assigns each client request a monotonic op-number, appends it to its log, and sends PREPARE to backups.
- A backup acknowledges with PREPAREOK; once the primary has f matching acks it commits, executes against the state machine, and replies to the client.
- The commit-number and op-number are piggybacked on later messages so backups learn what is committed without extra rounds.

## View Changes and Recovery

- Each configuration is a numbered view; the primary is deterministically the replica whose index equals view-number mod N.
- A backup that suspects the primary (missed heartbeats) starts a view change, broadcasting STARTVIEWCHANGE then DOVIEWCHANGE with its log.
- The new primary picks the most up-to-date log among received DOVIEWCHANGE messages, guaranteeing all committed ops survive.
- A recovering replica fetches current state via a recovery protocol before rejoining, so it never votes with stale data.

## Relationship to Paxos and Raft

- VR solves the same problem as Multi-Paxos but frames it as replication with explicit leaders and views rather than independent ballots.
- Raft's leader election, terms, and log-matching are close analogues of VR's primary, views, and view-change log selection.
- Unlike single-decree Paxos, VR is inherently a log/state-machine protocol, so ordering falls out of the op-number sequence.

## Sources

- Viewstamped Replication Revisited (Liskov, Cowling) - https://pmg.csail.mit.edu/papers/vr-revisited.pdf
- Viewstamped Replication (Oki, Liskov) - https://dl.acm.org/doi/10.1145/62546.62549

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
