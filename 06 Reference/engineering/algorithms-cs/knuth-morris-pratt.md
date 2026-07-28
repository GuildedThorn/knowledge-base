---
summary: "Linear-time string matching using a failure function to avoid re-examining text characters."
status: active
tags: [reference, engineering, algorithms, string-matching, prefix-function]
private: false
---

# Knuth-Morris-Pratt Algorithm

## Purpose

Linear-time string matching using a failure function to avoid re-examining text characters.

## Prefix / Failure Function

- KMP precomputes a failure function over the pattern: for each position, the length of the longest proper prefix that is also a suffix of the pattern up to that point.
- On a mismatch, this value tells the algorithm how far the pattern can shift without missing a potential match, reusing already-matched characters.
- The failure function is built in O(m) time for a pattern of length m by a self-matching scan of the pattern against itself.

## Linear Scan

- The text is scanned left to right with a single pointer that never moves backward.
- On a mismatch at pattern position j, the algorithm falls back to failure[j-1] instead of restarting, so text characters are never re-read.
- Matching the whole text of length n therefore takes O(n) comparisons after preprocessing.

## Correctness and Complexity

- Total time is O(n + m) and extra space is O(m) for the failure table, independent of alphabet size.
- The no-backtracking property makes KMP suitable for streaming input where the text cannot be rewound.
- Knuth, Morris, and Pratt (1977) formalized the algorithm and its linear bound, resolving the worst-case quadratic behavior of naive matching.

## Sources

- Knuth, Morris & Pratt, Fast Pattern Matching in Strings (1977) - https://doi.org/10.1137/0206024

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
