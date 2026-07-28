---
summary: "Lowest-total-weight tree connecting all graph vertices, built greedily by Kruskal's or Prim's algorithm."
status: active
tags: [reference, engineering, algorithms, greedy, graphs]
private: false
---

# Minimum Spanning Tree

## Purpose

Lowest-total-weight tree connecting all graph vertices, built greedily by Kruskal's or Prim's algorithm.

## Key Ideas

- An MST is an acyclic subgraph spanning all V vertices with V-1 edges and the minimum possible total edge weight, defined for connected undirected weighted graphs.
- Cut property: the lightest edge crossing any cut of the vertices is safe to include in some MST.
- Cycle property: the heaviest edge on any cycle can be excluded from some MST.
- When all edge weights are distinct the MST is unique.

## How It Works

- Kruskal sorts all edges by weight and adds each edge whose endpoints are in different components, using a union-find (disjoint-set) structure to reject cycles; runs in O(E log E).
- Prim grows one tree from an arbitrary start, repeatedly adding the cheapest edge leaving the current tree via a priority queue; runs in O(E log V) with a binary heap.
- Both are greedy and provably optimal thanks to the cut property; Kruskal suits sparse graphs, Prim dense ones.

## Sources

- Kruskal, On the Shortest Spanning Subtree of a Graph (1956) - https://doi.org/10.1090/S0002-9939-1956-0078686-7
- Prim, Shortest Connection Networks and Some Generalizations (1957) - https://doi.org/10.1002/j.1538-7305.1957.tb01515.x

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
