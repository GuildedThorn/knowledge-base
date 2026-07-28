---
summary: "Single-source shortest paths on non-negative-weight graphs using priority-queue greedy expansion."
status: active
tags: [reference, engineering, algorithms, shortest-path, greedy]
private: false
---

# Dijkstra's Algorithm

## Purpose

Single-source shortest paths on non-negative-weight graphs using priority-queue greedy expansion.

## How It Works

- Maintains a tentative distance for every vertex and a set of settled vertices whose shortest distance is final.
- Repeatedly extracts the unsettled vertex with the smallest tentative distance, marks it settled, and relaxes its outgoing edges.
- Relaxing edge (u, v) sets dist[v] = min(dist[v], dist[u] + w(u, v)); once a vertex is settled its distance never changes.
- The greedy choice is valid only because edge weights are non-negative, so no later path can undercut a settled vertex.

## Engineering Notes

- Binary-heap implementation runs in O((V + E) log V); a Fibonacci heap improves the theoretical bound to O(E + V log V).
- Fails on negative edge weights, which can make a settled vertex reachable more cheaply later; use Bellman-Ford instead.
- With a target and an admissible heuristic it generalizes to A*; on unweighted graphs it reduces to breadth-first search.

## Sources

- Dijkstra, A Note on Two Problems in Connexion with Graphs (1959) - https://doi.org/10.1007/BF01386390
- CLRS, Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
