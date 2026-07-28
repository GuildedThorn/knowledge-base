---
summary: "Union-find tracks dynamic connectivity with near-constant amortized operations using union by rank and path compression."
status: active
tags: [reference, engineering, algorithms, union-find]
private: false
---

# Union-Find / Disjoint Sets

## Purpose

Union-find tracks dynamic connectivity with near-constant amortized operations using union by rank and path compression.

## Core Model

- Find returns a representative for an element's set.
- Union merges two sets and can use rank/size to keep trees shallow.
- Path compression flattens trees during find, producing inverse-Ackermann amortized cost.

## Engineering Notes

- Use for Kruskal MST, connected components, equivalence classes, image segmentation, and network connectivity.
- Union-find answers connectivity under additions; deletions need different dynamic graph structures.
- Keep payload data separate from representatives unless merge semantics are carefully defined.

## Sources

- CLRS - Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- MIT OpenCourseWare - 6.006 Introduction to Algorithms - https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Princeton Algorithms - https://algs4.cs.princeton.edu/home/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
