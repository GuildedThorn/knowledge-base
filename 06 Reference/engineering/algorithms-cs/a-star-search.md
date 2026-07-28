---
summary: "Best-first graph search using an admissible heuristic to find optimal paths while expanding fewer nodes."
status: active
tags: [reference, engineering, algorithms, search, heuristics]
private: false
---

# A* Search

## Purpose

Best-first graph search using an admissible heuristic to find optimal paths while expanding fewer nodes.

## Core Model

- Each node is evaluated by `f(n) = g(n) + h(n)`, where `g(n)` is the known cost from the start and `h(n)` estimates remaining cost to the goal.
- A priority queue (open set) expands the node with the lowest `f` first; a closed set tracks settled nodes.
- On expansion, neighbor `g` values are relaxed and the queue is updated, mirroring Dijkstra's relaxation with an added heuristic bias toward the goal.

## Key Properties

- A heuristic is admissible if it never overestimates the true remaining cost; this guarantees an optimal solution.
- A heuristic is consistent (monotone) if `h(n) <= cost(n, n') + h(n')`; consistency implies admissibility and lets nodes be settled once without re-expansion.
- With `h = 0`, A* reduces exactly to Dijkstra's algorithm; a more informed (larger, still admissible) heuristic expands fewer nodes.

## Tradeoffs

- Memory grows with the open set and can be prohibitive; variants like IDA* and weighted A* trade optimality or memory for speed.
- An inadmissible heuristic can find solutions faster but forfeits the optimality guarantee.

## Sources

- Hart, Nilsson & Raphael, A Formal Basis for the Heuristic Determination of Minimum Cost Paths (1968) - https://doi.org/10.1109/TSSC.1968.300136

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
