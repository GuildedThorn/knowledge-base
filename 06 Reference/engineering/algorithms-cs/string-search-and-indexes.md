---
summary: "String algorithms support search, autocomplete, diffing, genomics, compilers, log scanning, and text indexing."
status: active
tags: [reference, engineering, algorithms, strings]
private: false
---

# String Search and Indexes

## Purpose

String algorithms support search, autocomplete, diffing, genomics, compilers, log scanning, and text indexing.

## Core Model

- KMP uses prefix-function structure to avoid rescanning text.
- Tries support prefix queries; suffix arrays/trees support substring queries; automata support multi-pattern matching.
- Unicode changes basic assumptions: code units, code points, grapheme clusters, normalization, and culture-sensitive comparison differ.

## Engineering Notes

- Use mature libraries for Unicode, regex, and tokenization unless the domain is deliberately constrained.
- For many patterns, use Aho-Corasick-style automata rather than repeated independent scans.
- Normalize input before indexing when canonical equivalence matters.

## Sources

- CLRS - Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- MIT OpenCourseWare - 6.006 Introduction to Algorithms - https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Princeton Algorithms - https://algs4.cs.princeton.edu/home/
- Unicode Standard Annex #15 - Normalization Forms - https://www.unicode.org/reports/tr15/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
