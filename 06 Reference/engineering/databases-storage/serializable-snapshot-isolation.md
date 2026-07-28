---
summary: "Upgrades snapshot isolation to full serializability by detecting dangerous read-write dependency cycles."
status: active
tags: [reference, engineering, databases, ssi, serializability, snapshot]
private: false
---

# Serializable Snapshot Isolation (SSI)

## Purpose

A technique that upgrades snapshot isolation to full serializability by detecting dangerous read-write dependency cycles.

## How It Works

- Plain snapshot isolation reads a consistent snapshot and blocks write-write conflicts but permits write skew, where two transactions read overlapping data and each updates a disjoint part.
- SSI tracks read-write antidependencies (rw-conflicts): one transaction reads a version that another concurrently overwrites.
- A serialization anomaly can only occur when a transaction has both an inbound and an outbound rw-antidependency to concurrent transactions, forming a "dangerous structure."
- Detecting such a structure, the system aborts one participant to break the potential cycle rather than validating the full dependency graph.

## Engineering Notes

- PostgreSQL implements SSI using SIREAD locks (predicate-style read markers) that record read footprints without blocking other transactions.
- SIREAD locks can be held past commit and may be summarized coarsely under memory pressure, trading precision for bounded overhead.
- The approach is optimistic: no read locking, so contention is low, but false-positive aborts can occur and callers must retry.
- SSI adds serializability atop an existing MVCC snapshot engine with modest changes, avoiding two-phase locking's blocking.

## Sources

- Cahill, Fekete & Rohm - Serializable Isolation for Snapshot Databases - https://dl.acm.org/doi/10.1145/1620585.1620587
- PostgreSQL Documentation - Transaction Isolation - https://www.postgresql.org/docs/current/transaction-iso.html
- Ports & Grittner - Serializable Snapshot Isolation in PostgreSQL - https://www.vldb.org/pvldb/vol5/p1850_danrkports_vldb2012.pdf

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
