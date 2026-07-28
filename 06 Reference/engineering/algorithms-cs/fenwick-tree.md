---
summary: "Structure computing prefix sums and point updates in O(log n) using low-bit index arithmetic."
status: active
tags: [reference, engineering, algorithms, prefix-sum, indexing]
private: false
---

# Fenwick Tree (Binary Indexed Tree)

## Purpose

Structure computing prefix sums and point updates in O(log n) using low-bit index arithmetic.

## Low-Bit Traversal

- A Fenwick tree stores partial sums in a flat 1-indexed array; index i covers a range whose length equals the lowest set bit of i.
- The lowest set bit is extracted as i & (-i) using two's-complement arithmetic.
- Both query and update walk the array by repeatedly adding or removing this low bit, taking O(log n) steps.
- The structure uses only O(n) space and can be built in O(n) time.

## Query and Update

- A prefix query for sum over [1, i] starts at i and repeatedly subtracts the low bit, accumulating stored partials.
- A point update at index i adds the delta, then repeatedly adds the low bit to propagate to all covering ranges.
- A range sum over [l, r] is computed as prefix(r) minus prefix(l-1).

## Extensions

- With a difference-array trick, a Fenwick tree supports range updates with point queries, or range updates with range queries using two trees.
- The idea generalizes to 2D grids for rectangle sums, with query and update cost O(log n * log m).
- Simpler and more cache-friendly than segment trees for pure prefix-sum workloads, though less flexible for arbitrary range operations.

## Sources

- Fenwick, A New Data Structure for Cumulative Frequency Tables (1994) - https://doi.org/10.1002/spe.4380240306

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
