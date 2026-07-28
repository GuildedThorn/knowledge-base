---
summary: "Amazon Dynamo partitions and replicates data across a consistent-hashing ring with quorum reads and vector-clock reconciliation."
status: active
tags: [reference, engineering, distributed-systems, partitioning, availability]
private: false
---

# Dynamo and Consistent Hashing

## Purpose

Amazon Dynamo partitions and replicates data across a consistent-hashing ring with quorum reads and vector-clock reconciliation.

## Ring Partitioning and Virtual Nodes

- Keys and nodes are hashed onto a fixed circular space; each key is owned by the first node clockwise from its hash position.
- Consistent hashing means adding or removing a node only remaps keys in its immediate ring neighborhood, minimizing reshuffling.
- Each physical node holds many "virtual nodes" (tokens) scattered around the ring, smoothing load imbalance and enabling heterogeneous capacities.
- Each key is replicated to the next N distinct physical nodes (the preference list) clockwise from its position.

## Sloppy Quorum and Hinted Handoff

- Reads and writes use configurable quorums with the R + W > N rule to tune the consistency-availability tradeoff.
- A "sloppy" quorum uses the first N healthy nodes rather than strictly the top N owners, keeping the system writable during failures.
- Hinted handoff stores a replica temporarily on a stand-in node, tagged with a hint, and delivers it to the intended owner once it recovers.
- Concurrent versions are reconciled with vector clocks; unresolved siblings are returned to the client for application-level merge.

## Anti-Entropy with Merkle Trees

- Background anti-entropy repairs divergence that hinted handoff misses, keeping replicas eventually consistent.
- Each node maintains a Merkle tree per key range; comparing root hashes lets peers detect differing subtrees without scanning all data.
- Only the ranges under mismatching hashes are exchanged, minimizing the data transferred to reconcile replicas.

## Sources

- Dynamo: Amazon's Highly Available Key-value Store - https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
- Consistent Hashing and Random Trees (Karger et al.) - https://www.akamai.com/site/en/documents/research-paper/consistent-hashing-and-random-trees-distributed-caching-protocols-for-relieving-hot-spots-on-the-world-wide-web-technical-publication.pdf

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
