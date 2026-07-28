---
summary: "Concurrency control that keeps multiple row versions so readers never block writers and snapshots see consistent data."
status: active
tags: [reference, engineering, databases, mvcc, versioning, concurrency]
private: false
---

# Multi-Version Concurrency Control (MVCC)

## Purpose

Concurrency control that keeps multiple row versions so readers never block writers and snapshots see consistent data.

## Version Chains and Visibility

- An update creates a new physical version of a row rather than overwriting it; versions are linked in a chain ordered by the writing transaction.
- Each version carries begin/end markers (creating and deleting transaction ids or commit timestamps) that bound its visibility.
- A reader traverses the chain and selects the version valid as of its snapshot, so it sees a consistent point-in-time view without locks.
- Because reads consult versions instead of taking locks, readers do not block writers and writers do not block readers.

## Timestamp and Snapshot Ordering

- Snapshot isolation gives each transaction a snapshot (a commit-timestamp or a set of visible transaction ids) taken at start.
- A version is visible if it was committed before the snapshot and not superseded by another committed version within it.
- Write-write conflicts are resolved by first-committer-wins or explicit row locks; snapshot isolation alone permits write-skew anomalies, which serializable variants (SSI) detect and abort.

## Garbage Collection

- Old versions no longer visible to any live snapshot are dead and must be reclaimed to bound storage and scan cost.
- PostgreSQL uses VACUUM (heap tuples plus a separate visibility map); other engines use background vacuum threads or in-place undo logs.
- Long-running transactions hold back the reclaim horizon, causing version bloat and slower scans until they finish.

## Sources

- Bernstein & Goodman - Concurrency Control in Distributed Database Systems - https://dl.acm.org/doi/10.1145/356842.356846
- PostgreSQL Documentation - Concurrency Control - https://www.postgresql.org/docs/current/mvcc.html
- Wu et al. - An Empirical Evaluation of In-Memory MVCC - https://www.vldb.org/pvldb/vol10/p781-Wu.pdf

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
