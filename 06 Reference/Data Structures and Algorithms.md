---
summary: Practical data structure and algorithm reference — complexity cheat sheet plus where each pattern actually shows up in production systems.
status: active
tags: [reference, algorithms, computer-science]
private: false
---

## Purpose

Compact reference for common data structures and algorithmic patterns, aimed at a working engineer rather than interview prep — complexity table, pattern cheat sheet, and where each one actually shows up in real systems. Compiled 2026-07-24.

## Complexity Cheat Sheet

n = number of elements. Amortized costs noted where relevant.

| Structure | Access | Search | Insert | Delete | Notes |
|---|---|---|---|---|---|
| Array (static) | O(1) | O(n) | O(n) | O(n) | dynamic array: O(1) amortized at end |
| Linked List | O(n) | O(n) | O(1)* | O(1)* | *only if you already hold the node |
| Hash Map | — | O(1) avg / O(n) worst | O(1) avg | O(1) avg | worst case from collisions/resize |
| BST (unbalanced) | O(log n) avg | O(log n) avg | O(log n) avg | O(log n) avg | degrades to O(n) on sorted input |
| Balanced Tree (RB/AVL) | O(log n) | O(log n) | O(log n) | O(log n) | guaranteed, not just average. RB: looser balance/faster writes (`std::map`, Linux CFS, Java `TreeMap`). AVL: stricter balance/faster reads |
| Heap (binary) | O(1) min/max | O(n) | O(log n) | O(log n) root | not for general search, only min/max extraction |
| Trie | — | O(k), k=key length | O(k) | O(k) | independent of n; prefix ops |
| Graph — adjacency list | — | O(V+E) | O(1) edge | O(E) edge | sparse graphs (most real-world graphs) |
| Graph — adjacency matrix | — | O(1) edge lookup | O(1) | O(1) | dense graphs / constant connectivity checks |

## Algorithmic Pattern Cheat Sheet

| Pattern | Core idea | Complexity | Use when |
|---|---|---|---|
| Sliding window | shrinking/growing contiguous range, two pointers | O(n) | subarray/substring with a running constraint |
| Two pointers | move from opposite ends or different speeds | O(n) | pair-sum on sorted data, dedup, partition |
| Fast/slow pointers | two pointers at different speeds through a linked structure | O(n) | cycle detection (Floyd's), find list midpoint |
| Binary search (+ variants) | halve the search space; also "search the answer space" | O(log n) | sorted data, or minimal-X-satisfying-predicate problems |
| BFS | level-by-level via queue | O(V+E) | shortest path unweighted, min-steps problems |
| DFS | depth-first via stack/recursion | O(V+E) | exhaustive exploration, connectivity, topo-sort backbone |
| Topological sort | order nodes so edges point forward (Kahn's or DFS+stack) | O(V+E) | build/dependency graphs, task scheduling |
| Union-Find | merge groups with path compression + union by rank | ~O(α(n)) per op | dynamic connectivity, Kruskal's MST, cycle detection |
| Dynamic programming | overlapping subproblems; memoization (top-down+cache) or tabulation (bottom-up) | varies, often O(n·W) | optimization/counting with optimal substructure |
| Dijkstra | greedy shortest path, priority queue, non-negative weights | O((V+E) log V) | weighted shortest path, routing |
| A* | Dijkstra + admissible heuristic biasing toward the goal | O((V+E) log V), fewer nodes in practice | pathfinding with a known target (game/VR navmeshes) |

**DP note:** memoization is easier to write correctly but has call-stack overhead; tabulation is faster and allows space optimization (rolling array). Canonical shapes: **0/1 Knapsack** — `dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i]] + val[i])`. **Longest Common Subsequence** — `dp[i][j] = dp[i-1][j-1]+1` if chars match else `max(dp[i-1][j], dp[i][j-1])`; the same table shape underlies diff tools and DNA alignment.

## Where These Show Up in Production

- **Sliding window** → rate limiters (fixed/sliding window counters, token buckets), TCP congestion windows, request-throttling middleware.
- **Two/fast-slow pointers** → cycle detection in state machines/graph configs, merge steps in external sort / merge-join.
- **Binary search variants** → "search on the answer" for capacity/threshold tuning, `git bisect`, staged rollout binary search.
- **BFS** → shortest-hop routing in unweighted service meshes, "friends of friends" queries, flood-fill.
- **DFS** → dependency resolution, cycle detection in build graphs, tree serialization (e.g. scene graphs in Godot).
- **Topological sort** → CI/CD stage ordering, package-manager install order, spreadsheet recalculation order.
- **Union-Find** → network connectivity checks (same subnet/reachable component), clustering, redundant-connection detection in infra graphs.
- **DP** → memoizing expensive pure computations generally (incremental compilers), diff algorithms, fuzzy-match/autocomplete.
- **Dijkstra/A*** → literal navmesh pathfinding (relevant to [vr-brain](kb://07-projects-vr-brain-vr-brain-overview)'s Earth pathing and any Godot navigation); also OSPF-style network routing.
- **Trie** → autocomplete, IP routing tables (longest-prefix match), spell-checkers, IOC/domain-prefix matching in threat-intel tooling.
- **LRU cache** → in-process caching, DB buffer pools, CDN edge caching.

## LRU Cache

Hash map (key → node pointer) + doubly linked list (recency order, most-recent at head):

- `get(key)`: O(1) map lookup, unlink + relink node at head (O(1) — doubly linked allows arbitrary-position removal without traversal).
- `put(key, value)`: update+move-to-head if present; else create node at head, add to map, evict tail on over-capacity.
- Needs the doubly linked list specifically — a singly linked list can't do O(1) removal from an arbitrary position (no predecessor reference).
- .NET: no built-in — `Dictionary<K, LinkedListNode<T>>` + `LinkedList<T>`. Java: `LinkedHashMap(accessOrder=true)` + `removeEldestEntry` gets this for free.

## Consistent Hashing

Plain `hash(key) % N` remaps almost every key when N (node count) changes — catastrophic for sharded caches/stores on scale-up/down. Consistent hashing places nodes and keys on a hash ring (0 to 2³²−1); a key maps to the first node clockwise. Adding/removing a node only remaps the ~`K/N` keys between it and its predecessor. Each physical node gets multiple **virtual nodes** on the ring to smooth load distribution. Used in DynamoDB, Cassandra, memcached client sharding, CDN request routing.

## Bloom Filters

Probabilistic set membership: bit array of size m + k independent hash functions. Insert sets k bits; query checks all k. **No false negatives, possible false positives** (tunable via m/k). Cannot delete (without a counting-bloom variant) or enumerate members.

**Practical use case:** a fast pre-filter in front of an expensive lookup — e.g. checking whether an IP/domain/hash is *possibly* in a large threat-intel IOC feed (see [Threat Intelligence Feeds](kb://12-datasets-ai-agent-cybersecurity-2026-threat-intelligence-feeds)) before hitting the real datastore or an enrichment API. A negative is a guaranteed skip; a positive triggers the authoritative check. Also: SSTable lookups in LevelDB/Cassandra to skip disk reads for missing keys, CDN/browser cache existence checks, stream-processing dedup.

## Related

- [Reference Map](kb://01-maps-reference-map)
- [Commands Cheat Sheet](kb://06-reference-commands-cheat-sheet)
- [High-Fidelity Planet Rendering (Godot)](kb://06-reference-high-fidelity-planet-rendering-godot)
- [Threat Intelligence Feeds](kb://12-datasets-ai-agent-cybersecurity-2026-threat-intelligence-feeds)
