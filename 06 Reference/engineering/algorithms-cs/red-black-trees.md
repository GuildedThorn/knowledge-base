---
summary: "Self-balancing binary search tree using node colors and rotations to guarantee O(log n) search, insert, and delete."
status: active
tags: [reference, engineering, algorithms, balanced-trees, bst]
private: false
---

# Red-Black Trees

## Purpose

Self-balancing binary search tree using node colors and rotations to guarantee O(log n) search, insert, and delete.

## Color Invariants

- Every node is colored red or black; the root and all null leaf sentinels are black.
- No red node has a red child, so red nodes never appear consecutively on any path.
- Every root-to-leaf path passes through the same number of black nodes, called the black-height.
- These invariants bound the longest path at no more than twice the shortest, keeping height O(log n).

## Rotations and Fixups

- Insertion adds a red node, then restores invariants via recoloring and left/right rotations, examining the uncle node's color to pick a case.
- Deletion may remove or displace a black node, creating a "double black" deficit fixed by rotations and recoloring up the tree.
- Both operations perform at most a constant number of rotations (2 for insert, 3 for delete) plus O(log n) recolorings.

## Tradeoffs

- Worst-case bounds are O(log n) for all dictionary operations, without the amortization skip lists rely on.
- Looser balance than AVL trees means fewer rotations on update but slightly taller trees and marginally slower lookups.
- Widely used in practice: Linux kernel schedulers, C++ std::map, and Java TreeMap.

## Sources

- Guibas & Sedgewick, A Dichromatic Framework for Balanced Trees (1978) - https://doi.org/10.1109/SFCS.1978.3
- CLRS, Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
