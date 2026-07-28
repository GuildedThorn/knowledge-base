---
summary: "The balanced, block-oriented search tree that underpins most disk-based relational indexes and range scans."
status: active
tags: [reference, engineering, databases, indexing, btree, access-methods]
private: false
---

# B+Tree Indexing

## Purpose

The balanced, block-oriented search tree that underpins most disk-based relational indexes and range scans.

## Structure and Fan-out

- Each node maps to a disk page; internal nodes hold only keys plus child pointers, while all data/record pointers live in leaf nodes.
- High fan-out (hundreds of keys per page) keeps the tree shallow, so a lookup costs only a few page reads even for billions of rows.
- Leaf nodes are linked in a sibling chain, enabling efficient ordered traversal without revisiting internal nodes.
- The tree stays balanced by construction: all leaves sit at the same depth, bounding worst-case lookup cost.

## Insert, Split, and Delete

- Insertion descends to a leaf; if the leaf is full it splits, pushing a separator key up, which may cascade splits toward the root.
- A root split is the only way the tree grows in height, keeping it balanced top-down.
- Deletion may underflow a node below the minimum occupancy, triggering redistribution from a sibling or a merge that can cascade upward.
- Many production engines defer merges and tolerate half-empty pages, relying on vacuum/rebuild rather than strict rebalancing.

## Range Scans and Index Types

- Range and prefix queries walk to a boundary leaf then follow the sibling chain, reading matches in sorted order.
- A clustered (primary) index stores the actual rows in leaf order, so the index is the table; secondary indexes store row locators instead.
- Ordered scans, ORDER BY, and MIN/MAX can be answered directly from B+Tree order, avoiding sorts.

## Sources

- Comer - The Ubiquitous B-Tree (ACM) - https://dl.acm.org/doi/10.1145/356770.356776
- PostgreSQL Documentation - B-Tree Indexes - https://www.postgresql.org/docs/current/btree.html
- CMU 15-445 Tree Indexes - https://15445.courses.cs.cmu.edu/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
