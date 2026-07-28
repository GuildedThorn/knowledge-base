---
summary: "Distributed consistency models range from linearizable to eventual, trading real-time guarantees for availability and performance."
status: active
tags: [reference, engineering, distributed-systems, consistency, semantics]
private: false
---

# Consistency Models Spectrum

## Purpose

Distributed consistency models range from linearizable to eventual, trading real-time guarantees for availability and performance.

## Strong, Weak, and Eventual

- Strong models (linearizability, strict serializability) make replicas behave like a single copy with real-time ordering; they cost latency and availability under partition.
- Weak models relax which reads must reflect prior writes, permitting stale or reordered results in exchange for lower latency.
- Eventual consistency only promises that replicas converge to the same state once updates cease, with no bound on staleness in the interim.

## Session and Causal Guarantees

- Session guarantees strengthen weak models per client: read-your-writes, monotonic reads, monotonic writes, and writes-follow-reads.
- Causal consistency preserves the happens-before ordering of causally related operations while allowing concurrent operations to be seen in any order.
- Causal+ adds convergence, making it the strongest model still achievable under network partitions.

## Model Hierarchy and Implications

- The models form a partial order of strength: strict serializability > linearizability > sequential > causal > eventual.
- Stronger models are easier to reason about but require more coordination and are limited by CAP during partitions.
- Jepsen's hierarchy distinguishes single-object models (registers) from transactional (multi-object) models like serializability and snapshot isolation.

## Sources

- Consistency Models (Jepsen) - https://jepsen.io/consistency
- Sequential Consistency (Lamport) - https://lamport.azurewebsites.net/pubs/multi.pdf

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
