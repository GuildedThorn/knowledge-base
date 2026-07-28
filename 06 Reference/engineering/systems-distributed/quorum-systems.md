---
summary: "Quorum-based replication guarantees consistency when read and write quorums overlap, formalized by the R plus W greater than N rule."
status: active
tags: [reference, engineering, distributed-systems, quorum, replication]
private: false
---

# Quorum Systems and R+W>N

## Purpose

Quorum-based replication guarantees consistency when read and write quorums overlap, formalized by the R plus W greater than N rule.

## Core Model

- N is the number of replicas; W is the replicas a write must acknowledge; R is the replicas a read must contact.
- R + W > N forces every read quorum to intersect every write quorum, so a read always sees at least one replica holding the latest write.
- W > N/2 additionally guarantees write quorums overlap each other, preventing two concurrent writes from both succeeding without a shared node to order them.
- Version numbers or timestamps let a reader pick the freshest value among the intersecting replicas.
- Tuning R and W trades read latency against write latency and availability without changing durability.

## Key Ideas

- Gifford's weighted voting assigns each replica a vote count, generalizing quorums so heterogeneous or more-trusted nodes carry more weight.
- Flexible (Fast) Paxos shows the leader-election and replication quorums need not be majorities: only phase-1 and phase-2 quorums must intersect, not each class internally.
- Grid and tree quorum constructions reduce quorum size below a simple majority while preserving pairwise intersection, lowering per-operation cost.
- Sloppy quorums plus hinted handoff (Dynamo-style) relax strict membership for higher availability at the cost of temporary inconsistency.

## Sources

- Weighted Voting for Replicated Data (Gifford) - https://dl.acm.org/doi/10.1145/800215.806583
- Flexible Paxos: Quorum Intersection Revisited - https://arxiv.org/abs/1608.06696

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
