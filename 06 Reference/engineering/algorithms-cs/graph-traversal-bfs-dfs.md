---
summary: "BFS and DFS are the two basic graph exploration strategies behind reachability, connected components, shortest unweighted paths, and dependency analysis."
status: active
tags: [reference, engineering, algorithms, graphs]
private: false
---

# Graph Traversal: BFS and DFS

## Purpose

BFS and DFS are the two basic graph exploration strategies behind reachability, connected components, shortest unweighted paths, and dependency analysis.

## Core Model

- BFS explores in layers using a queue and finds shortest path length in unweighted graphs.
- DFS explores depth-first using recursion or an explicit stack and underlies cycle detection and topological sorting.
- Adjacency lists are standard for sparse real-world graphs; adjacency matrices buy O(1) edge lookup at O(V^2) space.

## Engineering Notes

- Always define visited-state semantics: node visited, edge visited, color states, or path-local visited.
- Use iterative DFS for very deep graphs to avoid stack overflow.
- For dependency graphs, include cycle diagnostics that explain the path, not just that a cycle exists.

## Sources

- CLRS - Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- MIT OpenCourseWare - 6.006 Introduction to Algorithms - https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Princeton Algorithms - https://algs4.cs.princeton.edu/home/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
