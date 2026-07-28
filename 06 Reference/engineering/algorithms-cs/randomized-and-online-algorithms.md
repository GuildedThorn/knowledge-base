---
summary: "Randomized and online algorithms handle uncertainty by using probability, competitive analysis, or decisions without full future knowledge."
status: active
tags: [reference, engineering, algorithms, randomized]
private: false
---

# Randomized and Online Algorithms

## Purpose

Randomized and online algorithms handle uncertainty by using probability, competitive analysis, or decisions without full future knowledge.

## Core Model

- Randomized algorithms use randomness to simplify design or improve expected performance.
- Online algorithms make decisions as inputs arrive and are often judged by competitive ratio.
- Hashing, load balancing, sampling, caches, and streaming analytics use these ideas in production.

## Engineering Notes

- Make randomness testable with injectable seeds where deterministic reproduction matters.
- For online systems, compare against offline optimal only when that model is relevant to operations.
- Track tail behavior, not just expected value, for latency-sensitive systems.

## Sources

- MIT OCW - Randomized Algorithms - https://ocw.mit.edu/courses/6-856j-randomized-algorithms-fall-2002/
- CLRS - Introduction to Algorithms - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- The Algorithm Design Manual - https://www.algorist.com/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
