---
summary: "Database internals, storage engines, indexing, transactions, SQL, schema design, and recovery notes."
status: active
tags: [reference, engineering, databases, storage, index]
private: false
---

# Databases and Storage - Index

## Purpose

Database internals, storage engines, indexing, transactions, SQL, schema design, and recovery notes.

## Notes

- [Backup, Restore, and PITR](kb://06-reference-engineering-databases-storage-backup-restore-and-pitr) - Backups matter only when restore is tested; PITR combines base backups with write-ahead logs to recover to a chosen point.
- [Buffer Pools and Caches](kb://06-reference-engineering-databases-storage-buffer-pools-and-caches) - Database buffer pools cache pages and mediate disk I/O; cache policy determines whether working sets stay hot or churn.
- [Columnar Storage and OLAP](kb://06-reference-engineering-databases-storage-columnar-storage-and-olap) - Columnar systems store values by column to accelerate scans, compression, vectorized execution, and analytical aggregation.
- [Event Sourcing Storage Model](kb://06-reference-engineering-databases-storage-event-sourcing-storage-model) - Event sourcing stores immutable domain events as the source of truth and derives current state by replaying or projecting them.
- [FoundationDB Unbundled Transactional KV](kb://06-reference-engineering-databases-storage-foundationdb-unbundled-transactional-kv) - FoundationDB is a distributed transactional key-value store with a disaggregated transaction, log, and storage architecture.
- [Indexes: B-Tree, GIN, GiST, and BRIN](kb://06-reference-engineering-databases-storage-indexes-btree-gin-brin) - Database indexes speed reads by maintaining alternate access paths, but every index adds write, storage, and planning cost.
- [LSM Trees and RocksDB](kb://06-reference-engineering-databases-storage-lsm-trees-and-rocksdb) - Log-structured merge trees optimize write-heavy workloads by buffering writes and compacting sorted files over time.
- [Normalization and Data Modeling](kb://06-reference-engineering-databases-storage-normalization-and-data-modeling) - Data modeling turns business invariants into tables, keys, relationships, constraints, and intentional denormalization.
- [PostgreSQL MVCC and Vacuum](kb://06-reference-engineering-databases-storage-postgres-mvcc-vacuum) - PostgreSQL MVCC keeps multiple row versions so readers and writers can proceed concurrently, then vacuum cleans dead tuples.
- [Query Planning and Optimization](kb://06-reference-engineering-databases-storage-query-planning-and-optimization) - A database optimizer estimates costs and chooses physical plans; wrong statistics or query shape can dominate performance.
- [RAMP-TAO Read-Atomic Transactions](kb://06-reference-engineering-databases-storage-ramp-tao-read-atomic-transactions) - RAMP-TAO layers read-atomic transaction semantics onto TAO while preserving the performance profile of a read-optimized eventually consistent graph store.
- [Relational Model and SQL](kb://06-reference-engineering-databases-storage-relational-model-and-sql) - The relational model represents data as relations and uses declarative queries so optimizers can choose execution plans.
- [Schema Migrations and Evolution](kb://06-reference-engineering-databases-storage-schema-migrations-and-evolution) - Schema evolution coordinates application deployments, data backfills, compatibility, and rollback paths.
- [SQLite Architecture and File Format](kb://06-reference-engineering-databases-storage-sqlite-architecture-and-file-format) - SQLite compiles SQL to bytecode executed by a virtual machine and persists databases as page-oriented single-file structures.
- [TAO Social Graph Store](kb://06-reference-engineering-databases-storage-tao-social-graph-store) - TAO is Meta's read-optimized distributed graph store for serving social graph objects and associations at massive scale.
- [Transactions, Isolation, and ACID](kb://06-reference-engineering-databases-storage-transactions-isolation-and-acid) - Transactions group reads and writes under atomicity, consistency, isolation, and durability, with isolation levels defining concurrency anomalies.

## Related

- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Engineering Source Corpus](kb://06-reference-engineering-engineering-source-corpus)
- [Reference Map](kb://01-maps-reference-map)
