---
summary: "The standard isolation levels and the phenomena they prevent, plus the classic critique that redefined them by anomaly."
status: active
tags: [reference, engineering, databases, isolation, anomalies, transactions]
private: false
---

# ANSI SQL Isolation Levels

## Purpose

The standard isolation levels and the phenomena they prevent, with the classic critique that redefined them by anomaly.

## Levels and Phenomena

- The SQL standard defines four levels: Read Uncommitted, Read Committed, Repeatable Read, and Serializable.
- Each level is specified by the read phenomena it forbids: dirty read (reading uncommitted data), non-repeatable read (a re-read sees a changed row), and phantom (a re-run predicate sees new rows).
- Read Committed forbids dirty reads; Repeatable Read also forbids non-repeatable reads; Serializable forbids all three.
- The standard's phenomenon definitions are ambiguously worded, allowing multiple interpretations of what each level guarantees.

## The Critique and Snapshot Isolation

- Berenson et al. showed the ANSI phenomena are underspecified and proposed stricter anomaly-based definitions to disambiguate them.
- Snapshot isolation does not fit the ANSI hierarchy cleanly: it prevents dirty, non-repeatable, and phantom reads yet still allows write skew and read-only anomalies.
- Many engines map their labels loosely: PostgreSQL's Repeatable Read is actually snapshot isolation; Oracle's Serializable is snapshot isolation.
- Adya's later work formalized isolation via dependency graphs, giving implementation-independent definitions that cover MVCC systems.

## Sources

- Berenson et al. - A Critique of ANSI SQL Isolation Levels - https://www.microsoft.com/en-us/research/publication/a-critique-of-ansi-sql-isolation-levels/
- PostgreSQL Documentation - Transaction Isolation - https://www.postgresql.org/docs/current/transaction-iso.html
- Adya - Weak Consistency: A Generalized Theory and Optimistic Implementations - https://pmg.csail.mit.edu/papers/adya-phd.pdf

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
