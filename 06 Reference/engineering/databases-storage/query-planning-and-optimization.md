---
summary: "A database optimizer estimates costs and chooses physical plans; wrong statistics or query shape can dominate performance."
status: active
tags: [reference, engineering, databases, query-planning]
private: false
---

# Query Planning and Optimization

## Purpose

A database optimizer estimates costs and chooses physical plans; wrong statistics or query shape can dominate performance.

## Core Model

- Plans combine scans, joins, sorts, aggregates, filters, and materialization choices.
- Statistics drive cardinality estimates; bad estimates cause wrong join orders or scan choices.
- EXPLAIN shows planned operations; EXPLAIN ANALYZE shows actual execution.

## Engineering Notes

- Compare estimated rows to actual rows to find statistics/model failures.
- Add indexes, rewrite predicates, update statistics, and reduce row width before reaching for hints or denormalization.
- Profile representative production data; small dev databases hide planner pathologies.

## Sources

- PostgreSQL - Using EXPLAIN - https://www.postgresql.org/docs/current/using-explain.html
- PostgreSQL - Planner statistics - https://www.postgresql.org/docs/current/planner-stats.html
- CMU Database Systems - https://15445.courses.cs.cmu.edu/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
