---
summary: "Locally optimal choice strategy whose correctness is characterized by matroid and exchange-argument structure."
status: active
tags: [reference, engineering, algorithms, paradigm, matroids]
private: false
---

# Greedy Algorithms and Matroids

## Purpose

Locally optimal choice strategy whose correctness is characterized by matroid and exchange-argument structure.

## Core Model

- A greedy algorithm builds a solution one step at a time, always taking the choice that looks best locally and never reconsidering it.
- Correctness needs two ingredients: the greedy-choice property (a globally optimal solution contains some locally optimal first choice) and optimal substructure.
- Exchange arguments prove optimality by transforming any optimal solution into the greedy one without worsening its value.
- Unlike dynamic programming, greedy makes its choice before solving the subproblem, so it explores no alternatives.

## Matroid Optimality

- A matroid is a ground set with an independence family closed downward and satisfying the exchange axiom: if one independent set is larger, it has an element extending the other.
- For any weight function, the greedy algorithm that adds the heaviest element keeping independence yields a maximum-weight independent set - and this holds precisely for matroids.
- This theorem explains why greedy works for spanning trees (graphic matroid) and fails where the independence structure is not a matroid.

## Canonical Examples

- Kruskal's and Prim's minimum spanning tree, Huffman coding, activity selection, and fractional knapsack.
- Dijkstra's shortest path is greedy over a growing settled set with non-negative weights.
- Interval scheduling and set-cover approximations show greedy giving exact or bounded-ratio results.

## Sources

- Edmonds, Matroids and the Greedy Algorithm (1971) - https://doi.org/10.1007/BF01584082
- CLRS, Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
