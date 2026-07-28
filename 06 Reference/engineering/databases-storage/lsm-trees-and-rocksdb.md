---
summary: "Log-structured merge trees optimize write-heavy workloads by buffering writes and compacting sorted files over time."
status: active
tags: [reference, engineering, databases, lsm]
private: false
---

# LSM Trees and RocksDB

## Purpose

Log-structured merge trees optimize write-heavy workloads by buffering writes and compacting sorted files over time.

## Core Model

- Writes land in a memtable and WAL, then flush to immutable sorted files.
- Compaction merges files, removes overwritten/deleted keys, and controls read/write amplification.
- Bloom filters and block indexes reduce unnecessary disk reads.

## Engineering Notes

- Tune compaction, block cache, memtable size, compression, and level sizing for workload shape.
- Watch write amplification and space amplification; LSMs can move much more data than the application writes.
- Use key design to preserve locality and avoid hotspot or tombstone-heavy scans.

## Sources

- RocksDB Wiki - https://github.com/facebook/rocksdb/wiki
- Bigtable paper - https://research.google/pubs/bigtable-a-distributed-storage-system-for-structured-data/
- LevelDB implementation notes - https://github.com/google/leveldb/blob/main/doc/impl.md

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
