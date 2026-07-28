---
summary: "Sorting is the foundation for searching, joins, deduplication, ranking, external processing, and many data-processing pipelines."
status: active
tags: [reference, engineering, algorithms, sorting]
private: false
---

# Sorting Algorithms

## Purpose

Sorting is the foundation for searching, joins, deduplication, ranking, external processing, and many data-processing pipelines.

## Core Model

- Comparison sorting has an Omega(n log n) lower bound in the general case.
- Quicksort is fast in practice but needs pivot care; mergesort is stable and external-sort friendly; heapsort gives O(1) extra space but weaker locality.
- Counting/radix/bucket sorts beat comparison lower bounds only when key domains or digit models are constrained.

## Engineering Notes

- Choose stable sort when preserving original order for equal keys matters.
- For huge data, external merge sort and streaming runs beat in-memory assumptions.
- Prefer library sorts unless the domain gives a strong reason to exploit key structure.

## Sources

- CLRS - Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- MIT OpenCourseWare - 6.006 Introduction to Algorithms - https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Princeton Algorithms - https://algs4.cs.princeton.edu/home/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
