---
summary: "Sorted array of a string's suffixes enabling fast substring search and text indexing."
status: active
tags: [reference, engineering, algorithms, strings, indexing]
private: false
---

# Suffix Arrays

## Purpose

Sorted array of a string's suffixes enabling fast substring search and text indexing.

## Core Model

- Stores the starting indices of all suffixes of a string in lexicographic order, using O(n) integers rather than an explicit suffix tree.
- A substring query becomes a binary search over the sorted suffixes, since every occurrence of a pattern is a prefix of some contiguous range of suffixes.
- The Longest Common Prefix (LCP) array records the shared prefix length between adjacent suffixes, accelerating search and enabling many string statistics.

## Engineering Notes

- Naive construction sorts suffixes in O(n log^2 n) or O(n log n); linear-time algorithms (DC3/skew, SA-IS) build it in O(n).
- Binary-search substring queries run in O(m log n) for pattern length m, improvable to O(m + log n) with the LCP array.
- More cache- and space-efficient than suffix trees; a suffix array plus LCP array supports most suffix-tree operations.
- Underpins full-text indexes, the Burrows-Wheeler transform, and bioinformatics sequence search.

## Sources

- Manber & Myers, Suffix Arrays: A New Method for On-Line String Searches (1993) - https://doi.org/10.1137/0222058

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
