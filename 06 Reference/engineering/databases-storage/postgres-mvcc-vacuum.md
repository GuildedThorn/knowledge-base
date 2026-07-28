---
summary: "PostgreSQL MVCC keeps multiple row versions so readers and writers can proceed concurrently, then vacuum cleans dead tuples."
status: active
tags: [reference, engineering, databases, postgres]
private: false
---

# PostgreSQL MVCC and Vacuum

## Purpose

PostgreSQL MVCC keeps multiple row versions so readers and writers can proceed concurrently, then vacuum cleans dead tuples.

## Core Model

- Updates create new tuple versions; old versions remain visible to transactions whose snapshots need them.
- Vacuum reclaims dead tuples and prevents transaction ID wraparound.
- Long-running transactions and replication slots can keep old versions alive, causing bloat.

## Engineering Notes

- Monitor autovacuum, table/index bloat, dead tuples, transaction age, and long-running sessions.
- Tune vacuum per workload; write-heavy tables often need explicit attention.
- Use indexes and query shape to reduce unnecessary version scanning.

## Sources

- PostgreSQL - MVCC - https://www.postgresql.org/docs/current/mvcc.html
- PostgreSQL - Routine vacuuming - https://www.postgresql.org/docs/current/routine-vacuuming.html
- PostgreSQL - Monitoring database activity - https://www.postgresql.org/docs/current/monitoring.html

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
