---
summary: "A wide-column, masterless store using consistent hashing, tunable quorums, and an LSM storage engine over a gossip cluster."
status: active
tags: [reference, engineering, databases, cassandra, wide-column, gossip]
private: false
---

# Apache Cassandra Storage and Gossip

## Purpose

A wide-column, masterless store using consistent hashing, tunable quorums, and an LSM storage engine over a gossip cluster.

## Cluster and Distribution

- Cassandra is masterless: every node is a peer, and cluster membership plus liveness spread through a periodic gossip protocol rather than a coordinator.
- A partitioner hashes the partition key onto a token ring; the replication strategy places each partition on N successive nodes (and across racks/datacenters with NetworkTopologyStrategy).
- Any node can coordinate a request, forwarding to replicas that own the token; virtual nodes spread token ranges finely to smooth rebalancing.
- Hinted handoff stores writes for a temporarily down replica and replays them on recovery; read repair and anti-entropy repair reconcile divergent replicas.

## Consistency and Storage Engine

- Consistency is tunable per query via consistency levels (ONE, QUORUM, ALL, LOCAL_QUORUM); when read and write levels overlap a majority, reads observe the latest committed write.
- Writes append to a commit log and an in-memory memtable; memtables flush to immutable SSTables, and compaction merges SSTables while resolving conflicts by last-write-wins timestamps.
- Deletes are tombstones with timestamps, retained until gc_grace_seconds so a deletion is not resurrected by a lagging replica.
- This LSM design favors high write throughput and horizontal scale over strong single-node transactional semantics.

## Sources

- Lakshman & Malik - Cassandra: A Decentralized Structured Storage System - https://dl.acm.org/doi/10.1145/1773912.1773922
- Apache Cassandra Documentation - https://cassandra.apache.org/doc/latest/
- Cassandra Docs - Architecture - https://cassandra.apache.org/doc/latest/cassandra/architecture/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
