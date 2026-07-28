---
summary: "RAMP-TAO layers read-atomic transaction semantics onto TAO while preserving the performance profile of a read-optimized eventually consistent graph store."
status: active
tags: [reference, engineering, databases, storage, transactions, consistency]
private: false
---

# RAMP-TAO Read-Atomic Transactions

## Purpose

RAMP-TAO adds stronger read-transaction semantics on top of Meta's TAO graph store, targeting fractured-read anomalies without replacing the underlying eventually consistent architecture.

## Core Model

- TAO is optimized for massive read throughput and low latency.
- Some product logic needs a transactionally coherent view across related objects/associations.
- Read Atomic Multi-Partition protocols prevent fractured reads: readers should not observe only part of a multi-object transaction.
- RAMP-TAO layers metadata and protocol behavior onto TAO so applications can opt into stronger semantics.

## Design Tradeoff

- Full serializability would be expensive and misaligned with the existing read-dominant workload.
- Eventual consistency alone forces application developers to reason about rare but real anomalies.
- Read atomicity targets a narrower correctness property with lower overhead.
- The reported design keeps most reads local-cache one-round-trip and confines overhead mostly to transactional users.

## Engineering Notes

- "Bolt-on" consistency can be practical when the workload has clear anomaly boundaries.
- Narrower guarantees can be better engineering than global strictness.
- Metadata overhead, cache friendliness, and hotspot behavior decide whether a consistency upgrade is deployable.
- Transaction APIs should hide anomaly handling when the storage layer can do so cheaply.

## Sources

- Meta Engineering - RAMP-TAO: Layering atomic transactions on Facebook's online graph store - https://engineering.fb.com/2021/08/18/core-infra/ramp-tao/
- Meta Engineering - TAO: The power of the graph - https://engineering.fb.com/2013/06/25/core-infra/tao-the-power-of-the-graph/
- Meta Engineering - TAOBench - https://engineering.fb.com/2022/09/07/core-infra/taobench/

## Related

- [TAO Social Graph Store](kb://06-reference-engineering-databases-storage-tao-social-graph-store)
- [Transactions, Isolation, and ACID](kb://06-reference-engineering-databases-storage-transactions-isolation-and-acid)
- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
