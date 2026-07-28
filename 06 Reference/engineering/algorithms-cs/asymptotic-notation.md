---
summary: "Big-O, Omega, and Theta notation classifying algorithm growth rates independent of constants."
status: active
tags: [reference, engineering, algorithms, analysis, notation]
private: false
---

# Asymptotic Notation

## Purpose

Big-O, Omega, and Theta notation classifying algorithm growth rates independent of constants.

## Formal Definitions

- f(n) = O(g(n)) means there exist constants c > 0 and n0 such that 0 <= f(n) <= c*g(n) for all n >= n0; an asymptotic upper bound.
- f(n) = Omega(g(n)) means f(n) >= c*g(n) beyond n0; an asymptotic lower bound.
- f(n) = Theta(g(n)) means f is both O(g(n)) and Omega(g(n)); a tight bound sandwiching f between two constant multiples of g.
- The notation deliberately discards constant factors and lower-order terms to capture growth rate as input size scales.

## Little-o and Tight Bounds

- f(n) = o(g(n)) is a strictly loose upper bound: the ratio f(n)/g(n) tends to 0, so g dominates f.
- The dual little-omega, f(n) = omega(g(n)), denotes a strictly loose lower bound where f dominates g.
- Big-O permits equality of growth rates, while little-o forbids it; Theta is the strongest single-bound claim.
- Knuth (1976) advocated precise use of Omicron, Omega, and Theta to distinguish upper, lower, and exact orders.

## Common Growth Classes

- Ordered from slowest- to fastest-growing: O(1), O(log n), O(n), O(n log n), O(n^2), O(n^3), O(2^n), O(n!).
- Polynomial time (n^k for constant k) is the practical boundary of tractability; exponential and factorial classes are infeasible at scale.
- Bounds describe worst, average, or best case separately; unqualified Big-O usually refers to the worst case.

## Sources

- Knuth, Big Omicron and Big Omega and Big Theta (1976) - https://doi.org/10.1145/1008328.1008329
- CLRS, Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
