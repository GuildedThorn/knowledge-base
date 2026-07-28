---
summary: "FoundationDB is a distributed transactional key-value store with a disaggregated transaction, log, and storage architecture."
status: active
tags: [reference, engineering, databases, distributed-systems, transactions]
private: false
---

# FoundationDB Unbundled Transactional KV

## Purpose

FoundationDB combines ACID transactions with a distributed key-value architecture by separating transaction management, logging, and storage roles.

## Core Model

- Clients execute optimistic transactions over ordered key ranges.
- A sequencer assigns versions.
- Proxies coordinate transaction commit.
- Resolvers detect write conflicts.
- Log servers persist the committed mutation stream.
- Storage servers materialize key ranges from logs and serve reads.

## Design Lessons

- Disaggregating transaction, log, and storage roles enables independent scaling and recovery behavior.
- Ordered key-value APIs can support higher-level layers such as document, SQL, or graph models.
- Strong consistency does not require a monolithic database process; it requires carefully defined serialization, logging, recovery, and conflict detection.
- Simulation testing is a core FoundationDB design practice because distributed failure combinations are too large for example-based testing alone.

## Engineering Notes

- FoundationDB is useful as a reference model when evaluating "database as substrate" designs.
- Ordered keys make data modeling powerful but push responsibility for locality and encoding into the application or layer.
- Optimistic concurrency works best when transactions are short and conflict rates are controlled.

## Sources

- DBLP - FoundationDB: A Distributed Unbundled Transactional Key Value Store - https://dblp.org/rec/conf/sigmod/ZhouXSNMTABSLRD21.html
- ACM DOI - FoundationDB paper - https://doi.org/10.1145/3448016.3457559
- FoundationDB documentation - https://apple.github.io/foundationdb/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Transactions, Isolation, and ACID](kb://06-reference-engineering-databases-storage-transactions-isolation-and-acid)
- [Spanner and TrueTime](kb://06-reference-engineering-systems-distributed-spanner-and-truetime)
