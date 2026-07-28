---
summary: "Database buffer pools cache pages and mediate disk I/O; cache policy determines whether working sets stay hot or churn."
status: active
tags: [reference, engineering, databases, caching]
private: false
---

# Buffer Pools and Caches

## Purpose

Database buffer pools cache pages and mediate disk I/O; cache policy determines whether working sets stay hot or churn.

## Core Model

- A buffer pool maps disk pages to memory frames and tracks dirty/clean state.
- Replacement policies approximate recency/frequency while respecting pinned pages and writeback.
- OS page cache and database cache can duplicate or complement each other depending on storage engine design.

## Engineering Notes

- Tune memory based on working set, checkpoints, writeback, and read amplification, not raw table size.
- Measure cache hit ratios with latency and I/O counters; ratios alone can mislead.
- Avoid random large scans through hot OLTP caches unless the engine has scan-resistant policy or separate workloads.

## Sources

- CMU Database Systems - https://15445.courses.cs.cmu.edu/
- PostgreSQL - Resource consumption - https://www.postgresql.org/docs/current/runtime-config-resource.html
- PostgreSQL - WAL configuration - https://www.postgresql.org/docs/current/wal-configuration.html

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
