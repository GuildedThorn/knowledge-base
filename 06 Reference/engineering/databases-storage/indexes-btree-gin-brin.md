---
summary: "Database indexes speed reads by maintaining alternate access paths, but every index adds write, storage, and planning cost."
status: active
tags: [reference, engineering, databases, indexes]
private: false
---

# Indexes: B-Tree, GIN, GiST, and BRIN

## Purpose

Database indexes speed reads by maintaining alternate access paths, but every index adds write, storage, and planning cost.

## Core Model

- B-tree indexes cover equality, ranges, sorting, and prefix patterns for ordered data.
- GIN indexes invert composite values such as arrays, JSONB, and full-text tokens.
- BRIN indexes summarize block ranges and work well for naturally ordered large tables.

## Engineering Notes

- Index for real predicates, joins, ordering, and cardinality; unused indexes are write amplification.
- Use EXPLAIN ANALYZE to verify plans and row estimates.
- Composite index column order matters: equality and range predicate placement change usefulness.

## Sources

- PostgreSQL - Index types - https://www.postgresql.org/docs/current/indexes-types.html
- PostgreSQL - Multicolumn indexes - https://www.postgresql.org/docs/current/indexes-multicolumn.html
- PostgreSQL - EXPLAIN - https://www.postgresql.org/docs/current/using-explain.html

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
