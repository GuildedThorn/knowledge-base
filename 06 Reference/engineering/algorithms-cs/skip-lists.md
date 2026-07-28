---
summary: "Probabilistic layered linked list giving expected O(log n) search without explicit rebalancing."
status: active
tags: [reference, engineering, algorithms, probabilistic, ordered]
private: false
---

# Skip Lists

## Purpose

Probabilistic layered linked list giving expected O(log n) search without explicit rebalancing.

## How It Works

- A skip list stacks sorted linked lists: the bottom level holds all elements, and each higher level is a sparse express lane.
- Each inserted node is promoted to level i with probability p (commonly 1/2), so higher levels hold geometrically fewer nodes.
- Level assignment is random and independent of key order, so no rebalancing rotations are ever needed.
- The expected number of levels is O(log n) and expected total space is O(n).

## Search and Insert

- Search starts at the top-left, moving right until the next key would overshoot, then dropping down a level and repeating.
- Insertion locates the position at each level, splices the new node in, and flips coins to decide how high it rises.
- Expected search, insert, and delete are all O(log n); the worst case is O(n) but occurs with vanishing probability.

## Tradeoffs

- Simpler to implement and reason about than balanced trees, with no rotation or color logic.
- Concurrency-friendly: lock-free and fine-grained-locking skip lists are used in Java's ConcurrentSkipListMap and Redis sorted sets.
- Bounds are probabilistic rather than guaranteed, unlike red-black or B-trees.

## Sources

- Pugh, Skip Lists: A Probabilistic Alternative to Balanced Trees (1990) - https://doi.org/10.1145/78973.78977

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
