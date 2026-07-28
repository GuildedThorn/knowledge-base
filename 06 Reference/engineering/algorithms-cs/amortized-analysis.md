---
summary: "Technique bounding average cost per operation over a sequence via aggregate, accounting, and potential methods."
status: active
tags: [reference, engineering, algorithms, analysis, complexity]
private: false
---

# Amortized Analysis

## Purpose

Technique bounding average cost per operation over a sequence via aggregate, accounting, and potential methods.

## Key Ideas

- Amortized analysis bounds the total cost of a sequence of operations, then divides by the count, so occasional expensive steps are averaged against many cheap ones.
- It is a worst-case guarantee over the whole sequence, not a probabilistic average, and requires no assumptions about input distribution.
- It differs from average-case analysis, which averages over random inputs rather than over a run of operations.

## The Three Methods

- Aggregate method: bound the total cost T(n) of any n operations directly, then report T(n)/n as the amortized cost per operation.
- Accounting method: assign each operation a charged cost that may exceed or undercut its real cost, banking credit on cheap operations to pay for later expensive ones; stored credit must stay non-negative.
- Potential method: define a potential function on the data structure; amortized cost equals actual cost plus the change in potential, and a telescoping sum bounds the sequence when potential never drops below its start.

## Worked Structures

- Dynamic-array (table doubling) push is O(1) amortized despite O(n) resize copies.
- Binary counter increment averages O(1) bit flips per increment over a sequence.
- Splay trees and Fibonacci heaps use the potential method to prove O(log n) amortized operations while permitting costly individual steps.

## Sources

- Tarjan, Amortized Computational Complexity (1985) - https://doi.org/10.1137/0606031
- CLRS, Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
