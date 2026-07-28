---
summary: "The in-memory cache of disk pages and its replacement policies that decide which pages to evict under pressure."
status: active
tags: [reference, engineering, databases, buffer-pool, caching, eviction]
private: false
---

# Buffer Pool and Page Replacement

## Purpose

The in-memory cache of disk pages and its replacement policies that decide which pages to evict under pressure.

## How It Works

- The buffer pool is an array of fixed-size frames; a page table maps page IDs to the frame holding that page in memory.
- Each frame carries a pin/reference count and a dirty flag; a pinned page cannot be evicted, and a dirty page must be flushed before its frame is reused.
- On a miss the pool selects a victim frame via the replacement policy, writes it back if dirty, then loads the requested page.
- Prefetching reads ahead of sequential scans, and scan-resistant handling avoids letting a single large scan flush the entire working set.

## Replacement Policies

- Naive LRU evicts the least-recently-used page but is fooled by sequential floods that touch each page exactly once.
- LRU-K tracks the last K reference timestamps and evicts by backward K-distance, distinguishing pages with true reuse from one-shot accesses.
- CLOCK approximates LRU with a circular buffer and reference bits, avoiding per-access list maintenance; 2Q uses separate FIFO and LRU queues to filter scan traffic.
- WAL ordering constrains flushing: a dirty page cannot be written until its governing log records are on stable storage first.

## Sources

- O'Neil, O'Neil & Weikum - The LRU-K Page Replacement Algorithm - https://dl.acm.org/doi/10.1145/170035.170081
- PostgreSQL Documentation - Resource Consumption - https://www.postgresql.org/docs/current/runtime-config-resource.html
- CMU 15-445 Buffer Pools - https://15445.courses.cs.cmu.edu/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
