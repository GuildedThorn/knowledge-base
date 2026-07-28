---
summary: "Data modeling turns business invariants into tables, keys, relationships, constraints, and intentional denormalization."
status: active
tags: [reference, engineering, databases, modeling]
private: false
---

# Normalization and Data Modeling

## Purpose

Data modeling turns business invariants into tables, keys, relationships, constraints, and intentional denormalization.

## Core Model

- Normalization reduces update anomalies by separating facts into relations with clear dependencies.
- Denormalization trades consistency complexity for read performance or simpler access patterns.
- Keys and constraints are the durable expression of domain identity and invariant rules.

## Engineering Notes

- Model identities and lifecycles before columns: what exists independently, what changes, and what must be unique.
- Use denormalization only with ownership and rebuild/repair plans.
- Keep migrations and model docs together; implicit schema meaning leaks into application code otherwise.

## Sources

- Codd relational model paper - https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf
- PostgreSQL - Constraints - https://www.postgresql.org/docs/current/ddl-constraints.html
- Martin Fowler - Data modeling - https://martinfowler.com/tags/data%20modeling.html

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
