---
summary: "Hash tables trade ordered traversal for expected constant-time lookup, insertion, and deletion under a good hash distribution."
status: active
tags: [reference, engineering, algorithms, hashing]
private: false
---

# Hash Tables and Hashing

## Purpose

Hash tables trade ordered traversal for expected constant-time lookup, insertion, and deletion under a good hash distribution.

## Core Model

- Separate chaining and open addressing handle collisions with different memory/cache behavior.
- Load factor controls resize pressure and collision cost.
- Hash quality and adversarial input matter; randomized or hardened hash functions are used in exposed maps.

## Engineering Notes

- Use maps for exact-key lookups, sets for membership, and ordered maps when range queries or sorted output matter.
- Avoid mutating keys while they are in a hash table.
- For public inputs, consider collision attacks and use platform-provided hardened hashing where available.

## Sources

- CLRS - Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- MIT OpenCourseWare - 6.006 Introduction to Algorithms - https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Princeton Algorithms - https://algs4.cs.princeton.edu/home/
- Wikipedia - Universal hashing overview - https://en.wikipedia.org/wiki/Universal_hashing

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
