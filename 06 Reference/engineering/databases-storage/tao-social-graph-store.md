---
summary: "TAO is Meta's read-optimized distributed graph store for serving social graph objects and associations at massive scale."
status: active
tags: [reference, engineering, databases, storage, distributed-systems, graph]
private: false
---

# TAO Social Graph Store

## Purpose

TAO is Meta/Facebook's distributed data store for serving social graph objects and associations with a read-heavy, geographically distributed workload.

## Core Model

- The data model centers on objects and associations rather than relational joins.
- MySQL stores persistent object/association data; TAO caching clusters serve most reads.
- Requests go to caching servers that also coordinate writes and cache consistency.
- Sharding separates large graph data into many partitions while geographic deployment keeps reads close to users.
- The design prioritizes low-latency, high-throughput reads while preserving practical consistency for product semantics.

## Why It Exists

- Social feed rendering needs hundreds of graph lookups per user-visible page.
- The workload is read-dominant, highly personalized, and difficult to precompute.
- Some entities become hotspots unpredictably.
- Generic relational storage plus client-side memcache was not enough for cache consistency, locality, and coordination.

## Engineering Notes

- Creation-time locality matters: recently created social objects are often accessed heavily.
- Cache consistency is a product-correctness problem, not merely an optimization detail.
- Graph stores for user-facing products should model association access patterns directly.
- Read scaling, write routing, shard placement, and regional failover need to be designed together.

## Sources

- Meta Engineering - TAO: The power of the graph - https://engineering.fb.com/2013/06/25/core-infra/tao-the-power-of-the-graph/
- Meta Engineering - TAOBench - https://engineering.fb.com/2022/09/07/core-infra/taobench/
- Meta Engineering - RAMP-TAO - https://engineering.fb.com/2021/08/18/core-infra/ramp-tao/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Distributed Systems Principles](kb://06-reference-engineering-systems-distributed-distributed-systems-principles)
- [Replication, Quorums, and Conflict Resolution](kb://06-reference-engineering-systems-distributed-replication-quorums-and-conflict-resolution)
