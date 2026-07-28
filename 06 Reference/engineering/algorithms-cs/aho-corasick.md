---
summary: "Multi-pattern string matcher building a trie with failure links to find all keywords in one pass."
status: active
tags: [reference, engineering, algorithms, string-matching, automaton]
private: false
---

# Aho-Corasick Algorithm

## Purpose

Multi-pattern string matcher building a trie with failure links to find all keywords in one pass.

## How It Works

- Builds a keyword trie (goto function) over the set of patterns; each edge consumes one input character toward an accepting state.
- Adds failure links pointing each node to the longest proper suffix that is also a trie prefix, so a mismatch falls back without rescanning input.
- Output links (dictionary links) chain accepting states so all patterns ending at a position, including nested ones, are reported.
- Scans the text once left to right, following goto edges and falling back along failure links on mismatch.

## Engineering Notes

- Preprocessing is O(sum of pattern lengths); search is O(n + z) where n is text length and z is the number of matches reported.
- Failure links are computed with a breadth-first traversal of the trie, analogous to the KMP failure function generalized to many patterns.
- Used in intrusion detection (Snort-style rule matching), antivirus signature scanning, and bibliographic/keyword search.

## Sources

- Aho & Corasick, Efficient String Matching: An Aid to Bibliographic Search (1975) - https://doi.org/10.1145/360825.360855

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
