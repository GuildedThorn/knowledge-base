---
summary: "The industry-standard WAL recovery algorithm using LSNs, redo/undo, and fuzzy checkpoints for crash-consistent durability."
status: active
tags: [reference, engineering, databases, wal, recovery, logging]
private: false
---

# ARIES Write-Ahead Logging and Recovery

## Purpose

The industry-standard WAL recovery algorithm using LSNs, redo/undo, and fuzzy checkpoints for crash-consistent durability.

## WAL Protocol and LSNs

- Write-ahead logging requires that a log record describing a change reach stable storage before the corresponding dirty data page is written back.
- Every log record gets a monotonically increasing Log Sequence Number (LSN); each page stores the pageLSN of the last change applied to it.
- Log records for a transaction are backward-chained via a prevLSN field, letting recovery walk a transaction's updates in reverse.
- Comparing a page's pageLSN to a log record's LSN lets redo skip changes already reflected on the page (idempotent replay).

## Three Recovery Passes

- Analysis: scans forward from the last checkpoint to rebuild the dirty page table and transaction table, identifying losers (uncommitted at crash).
- Redo: repeats history from the earliest recLSN, reapplying all logged changes (even those of losers) to restore the exact pre-crash page state.
- Undo: rolls back loser transactions in reverse LSN order, using the transaction table's lastLSN and prevLSN chains.

## Checkpoints and CLRs

- Fuzzy (non-quiescent) checkpoints record the transaction and dirty page tables without halting activity, bounding how far back analysis must start.
- Undo actions are logged as Compensation Log Records (CLRs), which carry an UndoNext pointer so a crash during rollback never repeats already-undone work.
- CLRs are redo-only and never undone, guaranteeing rollback terminates even across repeated crashes.

## Sources

- Mohan et al. - ARIES (ACM TODS) - https://dl.acm.org/doi/10.1145/128765.128770
- PostgreSQL Documentation - Write-Ahead Logging - https://www.postgresql.org/docs/current/wal-intro.html
- CMU 15-445 Crash Recovery - https://15445.courses.cs.cmu.edu/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
