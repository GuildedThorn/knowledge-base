---
summary: "Network flow theory equating maximum flow with minimum cut, solved by augmenting-path algorithms."
status: active
tags: [reference, engineering, algorithms, network-flow, duality]
private: false
---

# Max-Flow Min-Cut

## Purpose

Network flow theory equating maximum flow with minimum cut, solved by augmenting-path algorithms.

## Core Model

- A flow network is a directed graph with a source, sink, and non-negative edge capacities; a flow respects capacity and conserves flow at every internal node.
- The residual graph tracks remaining capacity, including backward edges that let earlier flow be rerouted.
- An augmenting path is a source-to-sink path in the residual graph; pushing flow along it increases total flow until none remain.
- The max-flow min-cut theorem states the maximum flow value equals the minimum total capacity of any source-sink cut (a linear-programming duality).

## Engineering Notes

- Ford-Fulkerson augments along any residual path; with integer capacities it terminates but its running time can depend on capacity magnitudes and may loop on irrationals.
- Edmonds-Karp picks the shortest augmenting path via BFS, giving a capacity-independent O(V * E^2) bound.
- Push-relabel and Dinic's algorithm are faster in practice for dense or large graphs.
- Applications include bipartite matching, image segmentation, and network reliability and scheduling.

## Sources

- Ford & Fulkerson, Maximal Flow Through a Network (1956) - https://doi.org/10.4153/CJM-1956-045-5
- Edmonds & Karp, Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems (1972) - https://doi.org/10.1145/321694.321699

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
