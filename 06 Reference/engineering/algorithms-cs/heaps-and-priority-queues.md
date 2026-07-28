---
summary: "Heaps implement priority queues for repeatedly extracting the smallest or largest item without fully sorting every update."
status: active
tags: [reference, engineering, algorithms, heaps]
private: false
---

# Heaps and Priority Queues

## Purpose

Heaps implement priority queues for repeatedly extracting the smallest or largest item without fully sorting every update.

## Core Model

- Binary heaps store a nearly complete tree in an array for compact memory and O(log n) push/pop.
- Decrease-key matters for some graph algorithms but is absent or awkward in many standard libraries.
- Priority queues are not sorted lists; iteration order is not globally sorted.

## Engineering Notes

- Use heaps for schedulers, timers, top-k, Dijkstra/A*, event simulation, and streaming medians.
- For small top-k, bounded heaps keep memory predictable.
- Prefer explicit tie-breakers for deterministic output when priorities are equal.

## Sources

- CLRS - Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- MIT OpenCourseWare - 6.006 Introduction to Algorithms - https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Princeton Algorithms - https://algs4.cs.princeton.edu/home/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
