---
summary: "Columnar systems store values by column to accelerate scans, compression, vectorized execution, and analytical aggregation."
status: active
tags: [reference, engineering, databases, olap]
private: false
---

# Columnar Storage and OLAP

## Purpose

Columnar systems store values by column to accelerate scans, compression, vectorized execution, and analytical aggregation.

## Core Model

- Column stores read only needed attributes and compress similar adjacent values efficiently.
- Vectorized execution processes batches instead of one row at a time.
- OLAP workloads favor scans, joins, grouping, and append-heavy ingestion over single-row updates.

## Engineering Notes

- Use columnar formats for analytics, logs, metrics, and historical event data.
- Partition and cluster by query predicates to reduce scanned data.
- Keep OLTP and OLAP workload assumptions separate; one schema rarely serves both optimally.

## Sources

- C-Store paper - https://www.vldb.org/conf/2005/papers/p553-stonebraker.pdf
- Apache Parquet documentation - https://parquet.apache.org/docs/
- ClickHouse documentation - https://clickhouse.com/docs

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
