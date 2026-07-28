---
summary: "Linearizability is a strong consistency model requiring operations to appear atomic at some point between invocation and response."
status: active
tags: [reference, engineering, distributed-systems, consistency, correctness]
private: false
---

# Linearizability

## Purpose

Linearizability is a strong consistency model requiring operations to appear to take effect atomically at some point between invocation and response.

## Core Model

- Each operation has an invocation and a response event; its "linearization point" lies somewhere between them.
- Once an operation completes, its effect is visible to every subsequent operation, giving the illusion of a single, atomic global order.
- The chosen total order must respect the real-time ordering: if operation A returns before B is invoked, A must precede B.
- Concurrent (overlapping) operations may be ordered in either direction, giving implementations freedom.

## Composability and Locality

- Linearizability is a "local" property: a system is linearizable if and only if each object it comprises is individually linearizable.
- This locality means linearizable objects compose without extra coordination, unlike sequential consistency, which is not local.
- It is also nonblocking: a pending invocation never has to wait for another to complete to be linearized.

## Contrast with Sequential Consistency

- Sequential consistency requires only that operations respect each process's program order, ignoring real-time ordering across processes.
- Linearizability is strictly stronger: every linearizable history is sequentially consistent, but not vice versa.
- The real-time constraint makes linearizability the correctness condition typically expected of registers, locks, and CAS primitives.

## Sources

- Linearizability: A Correctness Condition for Concurrent Objects (Herlihy, Wing) - https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
