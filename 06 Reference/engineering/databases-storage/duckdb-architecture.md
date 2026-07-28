---
summary: "An in-process analytical database with vectorized execution, columnar storage, and MVCC designed for embedded OLAP."
status: active
tags: [reference, engineering, databases, duckdb, olap, embedded]
private: false
---

# DuckDB Architecture

## Purpose

An in-process analytical database with vectorized execution, columnar storage, and MVCC designed for embedded OLAP.

## Core Model

- DuckDB runs in-process (like SQLite) with no server, linked directly into the host application and sharing its address space.
- Execution is vectorized: operators pass batches (vectors, ~2048 values) of columnar data, amortizing per-row overhead and improving cache use.
- It uses a push-based (pull-then-push) execution model with morsel-driven parallelism for scaling across cores.
- Storage is a single-file columnar format organized into row groups, with lightweight per-column compression and zone maps for pruning.

## Engineering Notes

- MVCC provides ACID transactions with snapshot isolation, so readers do not block writers within the embedded process.
- The buffer manager streams data so queries can process datasets larger than RAM by spilling to disk.
- It ingests and queries Parquet, CSV, and Arrow directly, and can query data in place without a load step.
- The vectorized engine and columnar layout target analytical scans and aggregations, not high-rate single-row OLTP writes.

## Sources

- Raasveldt & Mühleisen - DuckDB: an Embeddable Analytical Database - https://dl.acm.org/doi/10.1145/3299869.3320212
- DuckDB Documentation - https://duckdb.org/docs/
- DuckDB - Internals/Storage - https://duckdb.org/docs/internals/storage

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
