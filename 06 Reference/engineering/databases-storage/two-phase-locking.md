---
summary: "The classic locking protocol whose growing/shrinking phases guarantee conflict-serializable schedules."
status: active
tags: [reference, engineering, databases, locking, serializability, concurrency]
private: false
---

# Two-Phase Locking (2PL)

## Purpose

The classic locking protocol whose growing/shrinking phases guarantee conflict-serializable schedules.

## Core Model

- A transaction acquires locks in a growing phase and releases them in a shrinking phase; once it releases any lock it may acquire no more.
- Locks come in modes: shared (S) for reads and exclusive (X) for writes, arbitrated by a compatibility matrix.
- Obeying the two-phase discipline is sufficient to produce only conflict-serializable schedules.
- The serialization order corresponds to the point where each transaction acquires its final lock (its lock point).

## Variants and Hazards

- Basic 2PL may release locks before commit, exposing uncommitted writes and allowing cascading aborts.
- Strict 2PL holds all exclusive locks until commit or abort, preventing dirty reads and cascading rollback; it is the common practical choice.
- Rigorous 2PL holds all locks (shared and exclusive) until end of transaction, giving commit-order serializability.
- 2PL does not prevent deadlocks; systems resolve them with wait-for-graph detection or timeout/wound-wait/wait-die schemes.
- Lock contention and deadlock frequency scale with transaction length and hotspot data.

## Sources

- Eswaran et al. - The Notions of Consistency and Predicate Locks in a Database System - https://dl.acm.org/doi/10.1145/360363.360369
- Gray & Reuter - Transaction Processing: Concepts and Techniques - https://www.google.com/books/edition/Transaction_Processing/VfkIykQBLEwC
- CMU 15-445 Two-Phase Locking - https://15445.courses.cs.cmu.edu/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
