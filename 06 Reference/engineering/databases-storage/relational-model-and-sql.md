---
summary: "The relational model represents data as relations and uses declarative queries so optimizers can choose execution plans."
status: active
tags: [reference, engineering, databases, sql]
private: false
---

# Relational Model and SQL

## Purpose

The relational model represents data as relations and uses declarative queries so optimizers can choose execution plans.

## Core Model

- Relations are sets of tuples with attributes; SQL tables are the practical language-layer representation.
- Declarative SQL states what result is needed, not the exact physical plan.
- Keys, constraints, joins, projection, selection, aggregation, and normalization shape relational design.

## Engineering Notes

- Use constraints as executable data contracts, not only application validation.
- Prefer set-based queries and measured plans over row-by-row application loops.
- Document schema meaning close to migrations so query authors understand cardinality and invariants.

## Sources

- Codd relational model paper - https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf
- PostgreSQL SQL language - https://www.postgresql.org/docs/current/sql.html
- CMU Database Systems lectures - https://15445.courses.cs.cmu.edu/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
