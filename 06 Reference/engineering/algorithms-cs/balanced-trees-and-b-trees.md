---
summary: "Balanced search trees guarantee logarithmic operations; B-trees optimize search trees for block/page-oriented storage."
status: active
tags: [reference, engineering, algorithms, trees]
private: false
---

# Balanced Trees and B-Trees

## Purpose

Balanced search trees guarantee logarithmic operations; B-trees optimize search trees for block/page-oriented storage.

## Core Model

- AVL, red-black, and similar trees rebalance after updates to avoid linear-height degeneration.
- B-trees and B+ trees store many keys per node so one disk/page read covers many comparisons.
- Database indexes usually use B+ tree variants because leaves form sorted linked ranges.

## Engineering Notes

- Use hash maps for point lookups, trees for ordered scans/ranges, and B-tree structures for storage engines.
- Database index design is workload design: equality, range, order-by, cardinality, and write cost all matter.
- In memory, cache locality can make flat sorted arrays competitive for small collections.

## Sources

- CLRS - Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- MIT OpenCourseWare - 6.006 Introduction to Algorithms - https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Princeton Algorithms - https://algs4.cs.princeton.edu/home/
- PostgreSQL - Index types - https://www.postgresql.org/docs/current/indexes-types.html

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
