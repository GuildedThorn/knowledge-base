---
summary: "Amortized-optimal priority queue with O(1) insert and decrease-key, speeding up Dijkstra and Prim."
status: active
tags: [reference, engineering, algorithms, priority-queue, amortized]
private: false
---

# Fibonacci Heaps

## Purpose

Amortized-optimal priority queue with O(1) insert and decrease-key, speeding up Dijkstra and Prim.

## How It Works

- The heap is a forest of heap-ordered trees held in a circular root list, with a pointer to the minimum root.
- Insert and meld just splice into the root list; work is deferred, so these cost O(1) actual time.
- Extract-min removes the min root, promotes its children to roots, then consolidates trees of equal degree until degrees are distinct.
- Decrease-key cuts the affected node from its parent into the root list; if the parent had already lost a child, it too is cut, cascading upward.

## Amortized Bounds

- A potential function counts root-list nodes plus twice the number of marked nodes, charging cheap operations to pay for later consolidation.
- Insert, find-min, decrease-key, and meld are O(1) amortized; extract-min and delete are O(log n) amortized.
- The marking rule (cascading cuts) keeps trees bushy so a tree of degree d contains at least F(d+2) nodes, bounding max degree at O(log n) - the source of the Fibonacci name.

## Tradeoffs

- Fast decrease-key drops Dijkstra and Prim to O(E + V log V), asymptotically better than binary-heap O(E log V) on dense graphs.
- Large constant factors and pointer-heavy nodes make them slower in practice than binary or pairing heaps for most inputs.
- Bounds are amortized, not worst-case per operation, which matters for real-time workloads.

## Sources

- Fredman & Tarjan, Fibonacci Heaps and Their Uses in Improved Network Optimization Algorithms (1987) - https://doi.org/10.1145/28869.28874

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
