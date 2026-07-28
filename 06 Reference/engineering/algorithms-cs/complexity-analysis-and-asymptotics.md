---
summary: "Complexity analysis estimates how resource use scales with input size so engineers can compare algorithms independent of one machine."
status: active
tags: [reference, engineering, algorithms, complexity]
private: false
---

# Complexity Analysis and Asymptotics

## Purpose

Complexity analysis estimates how resource use scales with input size so engineers can compare algorithms independent of one machine.

## Core Model

- Big-O is an upper-bound growth model; Theta is tight growth; Omega is lower-bound growth.
- Worst-case, average-case, amortized, and expected analyses answer different questions.
- Space complexity matters as much as time when caches, memory bandwidth, and data movement dominate runtime.

## Engineering Notes

- Estimate complexity before optimizing constants; then benchmark the real workload.
- Use amortized analysis for resizable arrays, hash tables, and union-find operations.
- Watch hidden costs: allocation, cache misses, branch misprediction, lock contention, and I/O can dominate simple operation counts.

## Sources

- CLRS - Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- MIT OpenCourseWare - 6.006 Introduction to Algorithms - https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Princeton Algorithms - https://algs4.cs.princeton.edu/home/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
