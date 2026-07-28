---
summary: "Dynamic programming solves problems with overlapping subproblems and optimal substructure by caching or tabulating intermediate results."
status: active
tags: [reference, engineering, algorithms, dynamic-programming]
private: false
---

# Dynamic Programming Patterns

## Purpose

Dynamic programming solves problems with overlapping subproblems and optimal substructure by caching or tabulating intermediate results.

## Core Model

- Memoization is top-down recursion plus cache; tabulation is bottom-up table construction.
- Common shapes include 1D recurrence, grid DP, interval DP, knapsack, sequence alignment, and tree DP.
- State definition is the core design step; recurrence and iteration order follow from it.

## Engineering Notes

- Write the brute-force recurrence first, then add cache/table and prove the state captures all needed history.
- Compress space only after correctness is clear.
- Watch exponential state spaces; DP is not automatically efficient if state dimensions explode.

## Sources

- CLRS - Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- MIT OpenCourseWare - 6.006 Introduction to Algorithms - https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Princeton Algorithms - https://algs4.cs.princeton.edu/home/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
