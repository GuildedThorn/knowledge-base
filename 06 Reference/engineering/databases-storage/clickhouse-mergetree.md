---
summary: "ClickHouse's columnar table engine using sorted, sparsely-indexed data parts merged in the background for fast analytics."
status: active
tags: [reference, engineering, databases, clickhouse, mergetree, olap]
private: false
---

# ClickHouse MergeTree Engine

## Purpose

ClickHouse's columnar table engine using sorted, sparsely-indexed data parts merged in the background for fast analytics.

## How It Works

- Each insert creates an immutable data part: columns stored separately, rows sorted by the table's `ORDER BY` sorting key.
- A background merge process combines small parts into larger ones, keeping part count low and preserving sort order (LSM-like).
- The primary index is sparse: it records one mark per granule (default 8192 rows) rather than one entry per row, so it stays in memory.
- Query execution uses the sparse index to prune granules, then reads only the required column files for the surviving ranges.

## Engineering Notes

- `PARTITION BY` (often by month) groups parts so whole partitions can be dropped or skipped; over-partitioning creates too many small parts.
- Per-column compression codecs (`LZ4` default, `ZSTD`, plus `Delta`, `DoubleDelta`, `Gorilla`) exploit type-specific patterns before general compression.
- `TTL` expressions expire rows or move parts across storage tiers automatically during merges.
- Specialized variants (`ReplacingMergeTree`, `AggregatingMergeTree`, `SummingMergeTree`) collapse or aggregate rows during merges by sorting key.

## Sources

- ClickHouse Documentation - MergeTree - https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree
- ClickHouse Documentation - Primary Index - https://clickhouse.com/docs/en/optimize/sparse-primary-indexes
- ClickHouse Documentation - Column Compression Codecs - https://clickhouse.com/docs/en/sql-reference/statements/create/table

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
