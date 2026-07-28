---
summary: "Paxos is a family of consensus algorithms for agreeing on a value despite crash failures and asynchronous communication."
status: active
tags: [reference, engineering, distributed-systems, consensus]
private: false
---

# Consensus: Paxos

## Purpose

Paxos is a family of consensus algorithms for agreeing on a value despite crash failures and asynchronous communication.

## Core Model

- The single-decree Paxos core separates proposers, acceptors, and learners.
- Safety relies on quorum intersection: any two majorities share at least one acceptor.
- Multi-Paxos optimizes repeated consensus by stabilizing a leader.

## Engineering Notes

- Use a library or managed system rather than implementing Paxos casually; edge cases are the algorithm.
- Understand quorum size, failure tolerance, durable acceptor state, leader election, and reconfiguration before operating it.
- Separate safety guarantees from liveness assumptions under network partitions.

## Sources

- Lamport - Paxos Made Simple - https://www.microsoft.com/en-us/research/publication/paxos-made-simple/
- Lamport - The Part-Time Parliament - https://www.microsoft.com/en-us/research/publication/part-time-parliament/
- MIT 6.824 Paxos lecture - https://pdos.csail.mit.edu/6.824/

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
