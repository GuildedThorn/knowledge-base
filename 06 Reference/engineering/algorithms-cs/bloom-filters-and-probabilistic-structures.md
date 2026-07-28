---
summary: "Probabilistic data structures trade exactness for compact memory and speed when false positives or approximations are acceptable."
status: active
tags: [reference, engineering, algorithms, probabilistic]
private: false
---

# Bloom Filters and Probabilistic Structures

## Purpose

Probabilistic data structures trade exactness for compact memory and speed when false positives or approximations are acceptable.

## Core Model

- Bloom filters answer set membership with no false negatives and tunable false positives.
- Count-Min Sketch estimates frequencies; HyperLogLog estimates cardinality; reservoir sampling samples streams.
- Hash choice and parameter sizing determine error bounds.

## Engineering Notes

- Put probabilistic filters before expensive authoritative lookups, not after them.
- Document false-positive/false-negative behavior; operators need to know what a result means.
- Use standard implementations for sketches where bias correction and merge semantics are subtle.

## Sources

- Bloom 1970 paper - https://dl.acm.org/doi/10.1145/362686.362692
- Redis - Probabilistic data structures - https://redis.io/docs/latest/develop/data-types/probabilistic/
- Google Bigtable paper - https://research.google/pubs/bigtable-a-distributed-storage-system-for-structured-data/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
