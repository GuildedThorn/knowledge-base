---
summary: "CAP and PACELC describe tradeoffs between consistency, availability, latency, and partition tolerance in replicated systems."
status: active
tags: [reference, engineering, distributed-systems, consistency]
private: false
---

# CAP, PACELC, and Consistency Models

## Purpose

CAP and PACELC describe tradeoffs between consistency, availability, latency, and partition tolerance in replicated systems.

## Core Model

- CAP says that during a network partition, a distributed data system must choose between consistency and availability for affected operations.
- PACELC adds the normal-case tradeoff: else, when no partition, choose between latency and consistency.
- Consistency models include linearizability, sequential consistency, causal consistency, read-your-writes, monotonic reads, and eventual consistency.

## Engineering Notes

- Do not use CAP as a slogan; describe the exact operation, failure, and consistency guarantee.
- Pick stronger consistency for coordination and weaker consistency for cacheable/mergeable data when business rules allow it.
- Expose staleness and conflict semantics to callers instead of hiding them behind a generic data-access layer.

## Sources

- Brewer - CAP twelve years later - https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/
- Abadi - PACELC - https://www.cs.umd.edu/~abadi/papers/abadi-pacelc.pdf
- Jepsen - Consistency models - https://jepsen.io/consistency

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
