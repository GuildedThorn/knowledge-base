---
summary: "Single-source shortest paths allowing negative edges and detecting negative cycles by repeated relaxation."
status: active
tags: [reference, engineering, algorithms, shortest-path, negative-weights]
private: false
---

# Bellman-Ford Algorithm

## Purpose

Single-source shortest paths allowing negative edges and detecting negative cycles by repeated relaxation.

## How It Works

- Relaxes every edge of the graph repeatedly, running V-1 full passes over the edge list, where V is the number of vertices.
- After i passes, tentative distances are correct for all shortest paths using at most i edges; V-1 passes suffice since any simple path has at most V-1 edges.
- A final Vth pass that still relaxes some edge proves a negative-weight cycle is reachable from the source.

## Engineering Notes

- Runs in O(V * E), slower than Dijkstra's O((V + E) log V), but tolerates negative edge weights that Dijkstra cannot.
- Detects negative cycles, making it suitable for arbitrage detection and constraint systems; distances are undefined when such a cycle is reachable.
- Serves as the per-node relaxation core of distance-vector routing protocols (e.g. RIP).
- The SPFA (queue-based) variant often runs faster in practice but has the same worst-case bound.

## Sources

- Bellman, On a Routing Problem (1958) - https://doi.org/10.1090/qam/102435
- CLRS, Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
