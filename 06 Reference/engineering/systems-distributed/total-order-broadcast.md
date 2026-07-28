---
summary: "Atomic broadcast delivers messages to all correct processes in the same total order, equivalent in power to consensus."
status: active
tags: [reference, engineering, distributed-systems, broadcast, ordering]
private: false
---

# Total Order Broadcast (Atomic Broadcast)

## Purpose

Atomic broadcast delivers messages to all correct processes in the same total order, equivalent in power to consensus.

## Core Properties

- Validity: if a correct process broadcasts a message, it eventually delivers it.
- Agreement: if any correct process delivers a message, all correct processes deliver it.
- Integrity: each message is delivered at most once, and only if it was actually broadcast.
- Total order: if two correct processes both deliver messages m and m', they deliver them in the same relative order.

## Equivalence to Consensus

- Total order broadcast and consensus are reducible to each other: a solution to one yields a solution to the other.
- This makes atomic broadcast impossible in a purely asynchronous system with even one crash (FLP), requiring failure detectors, partial synchrony, or randomization.
- State machine replication is the canonical application: feed identical, totally ordered command streams to deterministic replicas and they stay consistent.

## Implementation Approaches

- Fixed sequencer: a designated process assigns sequence numbers to all messages; simple but the sequencer is a bottleneck and failure point.
- Moving sequencer / token: the sequencer role circulates to spread load and avoid a single hotspot.
- Destination agreement: receivers run a consensus/agreement step (e.g. per-message timestamps or a shared consensus log) to agree on order.
- Communication history / causal approaches use vector-clock-like metadata so receivers deterministically derive a consistent order.

## Sources

- Total Order Broadcast and Multicast Algorithms: Taxonomy and Survey (Defago et al.) - https://dl.acm.org/doi/10.1145/1041680.1041682

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
