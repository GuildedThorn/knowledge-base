---
summary: "CRDTs are replicated data structures whose merge is commutative, associative, and idempotent, guaranteeing eventual convergence."
status: active
tags: [reference, engineering, distributed-systems, replication, convergence]
private: false
---

# CRDTs (Conflict-Free Replicated Data Types)

## Purpose

CRDTs are replicated data structures whose merge operation is commutative, associative, and idempotent to guarantee convergence.

## State-Based vs Operation-Based

- State-based (CvRDT) replicas periodically ship their full state; a merge function combines states and must form a join-semilattice.
- Operation-based (CmRDT) replicas broadcast operations, which must be commutative and delivered under a specified (often causal) order without duplication.
- CvRDTs tolerate lossy, out-of-order, duplicated message channels; CmRDTs need reliable causal broadcast but send smaller payloads.
- The two forms are equivalent in expressive power and can emulate each other.

## Join-Semilattice Convergence

- State-based convergence (SEC) follows because merge is a least-upper-bound over a partial order that is commutative, associative, and idempotent.
- Monotonic, non-decreasing state updates plus LUB merges mean replicas that have seen the same updates reach identical states regardless of order.
- This makes conflict resolution deterministic and coordination-free, avoiding consensus for merges.

## Common CRDTs

- Counters: G-Counter (grow-only, per-replica increments) and PN-Counter (a pair of G-Counters for increment and decrement).
- Sets: G-Set, 2P-Set (add/remove-once), OR-Set (observed-remove using unique tags to allow re-adds).
- Registers: LWW-Register (last-writer-wins by timestamp) and Multi-Value Register (keeps concurrent values).
- Sequences: RGA, Treedoc, and Logoot for collaborative text editing with stable element ordering.

## Sources

- A Comprehensive Study of CRDTs (Shapiro et al.) - https://inria.hal.science/inria-00555588/document
- Conflict-free Replicated Data Types (Shapiro et al.) - https://pages.lip6.fr/Marc.Shapiro/papers/CRDTs_SSS-2011.pdf

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
