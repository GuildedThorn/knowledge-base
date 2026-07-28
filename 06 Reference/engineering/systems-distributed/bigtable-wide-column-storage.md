---
summary: "Bigtable stores sparse distributed sorted maps over rows, columns, and timestamps, influencing HBase, Cassandra, and many cloud databases."
status: active
tags: [reference, engineering, distributed-systems, bigtable]
private: false
---

# Bigtable Wide-Column Storage

## Purpose

Bigtable stores sparse distributed sorted maps over rows, columns, and timestamps, influencing HBase, Cassandra, and many cloud databases.

## Core Model

- Rows are lexicographically ordered by row key and grouped into tablets for distribution.
- Column families define locality and storage configuration, while columns within families can be sparse.
- SSTables, memtables, compaction, and Bloom filters provide LSM-tree-like storage behavior.

## Engineering Notes

- Row-key design is workload design; bad keys cause hotspots or scan inefficiency.
- Group columns by access pattern and lifecycle, not by object-oriented class shape.
- Expect eventual compaction costs and tune for read/write amplification.

## Sources

- Google Bigtable paper - https://research.google/pubs/bigtable-a-distributed-storage-system-for-structured-data/
- Apache HBase architecture - https://hbase.apache.org/book.html#architecture
- Google Cloud Bigtable docs - https://cloud.google.com/bigtable/docs/overview

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
