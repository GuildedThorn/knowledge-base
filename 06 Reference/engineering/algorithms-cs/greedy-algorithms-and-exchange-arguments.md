---
summary: "Greedy algorithms make locally optimal choices; proof usually requires an exchange argument, matroid-like structure, or cut property."
status: active
tags: [reference, engineering, algorithms, greedy]
private: false
---

# Greedy Algorithms and Exchange Arguments

## Purpose

Greedy algorithms make locally optimal choices; proof usually requires an exchange argument, matroid-like structure, or cut property.

## Core Model

- Greedy is correct for interval scheduling, Huffman coding, MST algorithms, and some shortest-path settings.
- A greedy-looking heuristic is not a proof; counterexamples are common.
- Exchange arguments show an optimal solution can be transformed to include the greedy choice.

## Engineering Notes

- Use greedy when the problem has a provable cut/exchange property or when an approximation heuristic is explicitly acceptable.
- Keep heuristic greediness out of correctness-critical systems unless bounded by tests and fallback behavior.
- Document whether an algorithm is exact or heuristic; future maintainers need that distinction.

## Sources

- CLRS - Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- MIT OpenCourseWare - 6.006 Introduction to Algorithms - https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Princeton Algorithms - https://algs4.cs.princeton.edu/home/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
