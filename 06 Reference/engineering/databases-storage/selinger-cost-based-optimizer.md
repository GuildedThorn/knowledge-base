---
summary: "The System R approach to access-path selection using statistics, cost estimation, and dynamic-programming join ordering."
status: active
tags: [reference, engineering, databases, optimizer, query-planning, join-order]
private: false
---

# Cost-Based Query Optimization (Selinger)

## Purpose

The System R approach to access-path selection using statistics, cost estimation, and dynamic-programming join ordering.

## Core Model

- Introduced in the 1979 System R paper; the foundation of nearly every modern relational optimizer.
- Enumerates candidate plans, assigns each an estimated cost, and picks the cheapest rather than following fixed rules.
- Cost combines page I/O and CPU (RSI calls) into a single weighted metric.
- Access paths per table: sequential scan versus available indexes; the optimizer chooses per query.

## Cardinality and Selectivity

- Selectivity is the fraction of rows a predicate passes; it drives every downstream cardinality estimate.
- Default heuristics are used when statistics are absent (e.g. 1/10 for equality, 1/3 for range).
- Estimation errors compound multiplicatively across joins, the dominant source of bad plans.
- Modern engines refine this with histograms, most-common-value lists, and distinct-value counts.

## Join Enumeration

- Join ordering is optimized by bottom-up dynamic programming over subsets of relations.
- "Interesting orders" (sort orders useful to later joins or ORDER BY) are retained even at higher cost to avoid re-sorting.
- The original algorithm considers only left-deep trees to bound the search space.
- Nested-loop, sort-merge, and hash joins are costed as alternative physical operators.

## Sources

- Selinger et al. - Access Path Selection in a Relational DBMS - https://dl.acm.org/doi/10.1145/582095.582099
- PostgreSQL Documentation - Planner/Optimizer - https://www.postgresql.org/docs/current/planner-optimizer.html
- CMU 15-445 Query Optimization - https://15445.courses.cs.cmu.edu/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
