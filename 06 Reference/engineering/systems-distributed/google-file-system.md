---
summary: "GFS is a distributed file system designed for large files, sequential workloads, chunk replication, and commodity-machine failure."
status: active
tags: [reference, engineering, distributed-systems, storage]
private: false
---

# Google File System

## Purpose

GFS is a distributed file system designed for large files, sequential workloads, chunk replication, and commodity-machine failure.

## Core Model

- Files are split into fixed-size chunks managed by chunkservers.
- A master stores metadata and coordinates chunk placement, leases, and namespace operations.
- Replication, checksums, and re-replication handle frequent component failure.

## Engineering Notes

- GFS-style assumptions fit append-heavy analytical workloads better than small random POSIX file workloads.
- Separate metadata and data-plane design questions; metadata masters can become bottlenecks if assumptions shift.
- Chunk size, replication factor, rack awareness, and repair bandwidth are operational parameters.

## Sources

- Google File System paper - https://research.google/pubs/the-google-file-system/
- Google MapReduce paper - https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/
- HDFS architecture - https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
