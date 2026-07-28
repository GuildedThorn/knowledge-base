---
summary: "Shortest-path algorithms differ by edge weights, negative edges, graph size, and whether a target-specific heuristic is available."
status: active
tags: [reference, engineering, algorithms, shortest-paths]
private: false
---

# Shortest Paths: Dijkstra, Bellman-Ford, and A*

## Purpose

Shortest-path algorithms differ by edge weights, negative edges, graph size, and whether a target-specific heuristic is available.

## Core Model

- Dijkstra assumes non-negative edge weights and greedily finalizes nearest unsettled nodes.
- Bellman-Ford handles negative edges and can detect negative cycles at higher cost.
- A* biases Dijkstra toward a target using an admissible heuristic.

## Engineering Notes

- Use Dijkstra for routing-like non-negative weighted paths and A* for game/navigation paths with a good distance heuristic.
- Reject negative weights before using Dijkstra; incorrect assumptions silently produce wrong paths.
- For all-pairs paths, consider repeated single-source, Floyd-Warshall, Johnson, or domain-specific preprocessing.

## Sources

- CLRS - Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- MIT OpenCourseWare - 6.006 Introduction to Algorithms - https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Princeton Algorithms - https://algs4.cs.princeton.edu/home/
- Dijkstra 1959 paper - https://doi.org/10.1007/BF01386390

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
