---
summary: "Backups matter only when restore is tested; PITR combines base backups with write-ahead logs to recover to a chosen point."
status: active
tags: [reference, engineering, databases, backup]
private: false
---

# Backup, Restore, and PITR

## Purpose

Backups matter only when restore is tested; PITR combines base backups with write-ahead logs to recover to a chosen point.

## Core Model

- Logical backups capture data definitions and rows; physical backups copy storage files and WAL.
- Point-in-time recovery replays WAL from a base backup until a target timestamp/LSN.
- RPO and RTO define how much data loss and downtime the business accepts.

## Engineering Notes

- Test restores on a schedule and record restore time, missing dependencies, and access requirements.
- Store backups in separate credentials/failure domains with immutability where possible.
- Monitor backup freshness, WAL archiving lag, restore integrity, and retention expiry.

## Sources

- PostgreSQL - Backup and restore - https://www.postgresql.org/docs/current/backup.html
- PostgreSQL - Continuous archiving and PITR - https://www.postgresql.org/docs/current/continuous-archiving.html
- Google SRE Book - Data integrity - https://sre.google/sre-book/data-integrity/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
