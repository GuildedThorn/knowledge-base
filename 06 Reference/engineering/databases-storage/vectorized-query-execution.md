---
summary: "Batch-at-a-time execution processing columnar vectors per operator to amortize interpretation cost and exploit SIMD."
status: active
tags: [reference, engineering, databases, vectorized, simd, execution]
private: false
---

# Vectorized Query Execution

## Purpose

Batch-at-a-time execution processing columnar vectors per operator to amortize interpretation cost and exploit SIMD.

## Key Ideas

- Operators process a batch (vector) of many values per next call instead of a single tuple.
- Pioneered by MonetDB/X100; a vector is typically sized to fit comfortably in L1/L2 CPU cache (e.g. ~1024 values).
- Amortizes the per-call function-dispatch and interpretation overhead across the whole batch.
- Inner loops run over primitive-typed arrays, giving the compiler predictable, tight, auto-vectorizable code.

## Engineering Notes

- Primitives are written branch-free where possible; selection vectors carry filter results instead of branching per row.
- Columnar in-memory layout maximizes cache-line utilization and enables SIMD across contiguous values.
- Sequential array access yields regular, hardware-prefetchable memory patterns.

## Vectorized vs Compiled

- Compiled execution (data-centric code generation) fuses operators to eliminate materialization between them.
- Vectorization keeps interpretation but materializes vectors; compilation removes interpretation but loses some pipelining.
- Studies find the two are broadly competitive; the choice trades compile latency against per-tuple efficiency.
- Systems like DuckDB adopt vectorization for its portability and simpler engineering.

## Sources

- Boncz, Zukowski & Nes - MonetDB/X100: Hyper-Pipelining Query Execution - https://www.cidrdb.org/cidr2005/papers/P19.pdf
- Kersten et al. - Everything You Always Wanted to Know About Compiled and Vectorized Queries - https://www.vldb.org/pvldb/vol11/p2209-kersten.pdf
- DuckDB Documentation - https://duckdb.org/docs/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
