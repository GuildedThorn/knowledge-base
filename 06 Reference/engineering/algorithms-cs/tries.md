---
summary: "Prefix tree indexing strings by shared character paths for fast lookup, prefix, and autocomplete queries."
status: active
tags: [reference, engineering, algorithms, strings, prefix]
private: false
---

# Tries

## Purpose

Prefix tree indexing strings by shared character paths for fast lookup, prefix, and autocomplete queries.

## Core Model

- Each edge is labeled with one character; a root-to-node path spells a prefix, so strings sharing a prefix share their upper path.
- Nodes carry a terminal flag (or value) marking where a stored key ends, distinguishing a full key from a mere prefix.
- Branching factor equals the alphabet size; a node typically holds a child map or fixed array indexed by symbol.
- No two keys collide by hashing, so ordering is preserved and lexicographic traversal is a simple in-order walk.

## Operations

- Lookup, insert, and delete run in O(k) time for a key of length k, independent of the number of stored keys.
- Prefix queries and autocomplete descend to the prefix node, then enumerate the subtree; this is the trie's signature advantage over hash tables.
- Deletion prunes now-childless, non-terminal nodes back up toward the root to reclaim space.

## Variants and Tradeoffs

- Compressed tries (Patricia/radix trees) merge single-child chains into one edge labeled with a substring, cutting node count and pointer chasing.
- Ternary search tries store three child pointers per node, trading some prefix speed for far lower memory than array-backed nodes.
- Naive tries waste memory on sparse alphabets; radix and TST variants or child hash maps mitigate this.
- Used in routing tables (IP longest-prefix match), spell checkers, and dictionary compression.

## Sources

- Fredkin, Trie Memory (1960) - https://doi.org/10.1145/367390.367400

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
