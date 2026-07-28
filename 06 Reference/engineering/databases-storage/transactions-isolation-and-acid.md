---
summary: "Transactions group reads and writes under atomicity, consistency, isolation, and durability, with isolation levels defining concurrency anomalies."
status: active
tags: [reference, engineering, databases, transactions]
private: false
---

# Transactions, Isolation, and ACID

## Purpose

Transactions group reads and writes under atomicity, consistency, isolation, and durability, with isolation levels defining concurrency anomalies.

## Core Model

- Atomicity means all-or-nothing commit; durability means committed data survives required failures.
- Isolation levels trade concurrency against anomalies such as dirty reads, non-repeatable reads, phantoms, write skew, and serialization failures.
- MVCC and locking are common implementation strategies with different read/write interactions.

## Engineering Notes

- Choose isolation by invariant, not habit; money, inventory, and workflow state may need stronger guarantees.
- Handle serialization/deadlock retries as a normal application path.
- Keep transactions short and avoid network calls while holding database locks.

## Sources

- PostgreSQL - Transaction isolation - https://www.postgresql.org/docs/current/transaction-iso.html
- PostgreSQL - MVCC - https://www.postgresql.org/docs/current/mvcc.html
- Berenson et al. - A Critique of ANSI SQL Isolation Levels - https://www.microsoft.com/en-us/research/publication/a-critique-of-ansi-sql-isolation-levels/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
