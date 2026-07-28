---
summary: "The atomic commitment protocol coordinating prepare and commit across participants in a distributed transaction."
status: active
tags: [reference, engineering, databases, 2pc, atomic-commit, distributed]
private: false
---

# Two-Phase Commit (2PC)

## Purpose

The atomic commitment protocol coordinating prepare and commit across participants in a distributed transaction.

## How It Works

- Phase one (prepare/voting): the coordinator asks each participant to prepare; a participant that can commit durably logs its state and votes yes, otherwise votes no.
- Phase two (commit/abort): if all vote yes the coordinator logs a commit decision and broadcasts commit; any no vote or timeout yields a global abort.
- Once a participant has voted yes it is in an uncertain state and must await and obey the coordinator's decision.
- The coordinator's commit record is the atomic decision point; participants replay their logs to recover after a crash.

## Failure Behavior and Alternatives

- 2PC is blocking: if the coordinator fails after participants have voted yes, prepared participants hold locks and cannot unilaterally resolve until it recovers.
- Three-phase commit (3PC) adds a pre-commit round to become non-blocking under synchronous assumptions, but is fragile under network partitions and rarely used.
- Paxos Commit replaces the single coordinator with a consensus group deciding each participant's vote, tolerating coordinator failure without blocking.
- Because of its blocking and latency costs, distributed databases often prefer consensus-replicated commit or sagas for cross-service atomicity.

## Sources

- Gray - Notes on Data Base Operating Systems - https://link.springer.com/chapter/10.1007/3-540-08755-9_9
- Bernstein, Hadzilacos & Goodman - Concurrency Control and Recovery in Database Systems - https://www.microsoft.com/en-us/research/people/philbe/book/
- CMU 15-445 Distributed Transactions - https://15445.courses.cs.cmu.edu/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
