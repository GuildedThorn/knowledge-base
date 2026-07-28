---
summary: "NP-completeness explains why many optimization problems resist known polynomial-time exact algorithms and need approximation, heuristics, or constraints."
status: active
tags: [reference, engineering, algorithms, np-complete]
private: false
---

# NP-Completeness and Approximation

## Purpose

NP-completeness explains why many optimization problems resist known polynomial-time exact algorithms and need approximation, heuristics, or constraints.

## Core Model

- P problems have polynomial-time algorithms; NP problems have efficiently checkable solutions.
- NP-complete problems are as hard as any problem in NP under reductions.
- Approximation algorithms provide bounded-quality solutions for some hard optimization problems.

## Engineering Notes

- If a problem smells like scheduling, routing, packing, covering, or graph coloring, check whether exact solving is realistic.
- Use reductions and small counterexamples to avoid building impossible exact systems.
- Choose between exact solvers, approximation, heuristics, constraints, and offline precomputation based on business tolerance.

## Sources

- CLRS - Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- MIT OpenCourseWare - 6.006 Introduction to Algorithms - https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Princeton Algorithms - https://algs4.cs.princeton.edu/home/
- MIT OCW - Advanced Algorithms - https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2005/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
