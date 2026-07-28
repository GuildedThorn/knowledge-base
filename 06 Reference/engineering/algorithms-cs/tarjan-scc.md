---
summary: "Single-pass DFS computing strongly connected components using discovery indices and a low-link stack."
status: active
tags: [reference, engineering, algorithms, graphs, dfs]
private: false
---

# Tarjan's SCC Algorithm

## Purpose

Single-pass DFS computing strongly connected components using discovery indices and a low-link stack.

## Core Model

- A strongly connected component (SCC) is a maximal set of vertices mutually reachable via directed paths.
- Each vertex gets an `index` (DFS discovery order) and a `lowlink`, the smallest index reachable from its DFS subtree via tree and back edges.
- Vertices are pushed onto an explicit stack when first visited and marked "on stack" to distinguish cross edges from back edges.
- After exploring a vertex's neighbors, `lowlink = min(lowlink, child.lowlink)` for tree edges and `min(lowlink, neighbor.index)` for on-stack neighbors.

## How It Works

- When a vertex `v` finishes with `lowlink == index`, it is an SCC root; pop the stack down to and including `v` to emit that component.
- Components are output in reverse topological order of the condensation DAG.
- Only one DFS pass is needed, unlike Kosaraju's two-pass transpose approach.

## Tradeoffs

- Runs in O(V + E) time and O(V) auxiliary space; optimal for adjacency-list graphs.
- Recursive form can overflow the stack on deep graphs; an explicit iterative stack is used for large inputs.

## Sources

- Tarjan, Depth-First Search and Linear Graph Algorithms (1972) - https://doi.org/10.1137/0201010

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
