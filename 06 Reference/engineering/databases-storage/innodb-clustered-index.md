---
summary: "MySQL's default engine organizing tables as clustered B+Trees with secondary indexes, undo logs, and the buffer pool."
status: active
tags: [reference, engineering, databases, innodb, mysql, clustered-index]
private: false
---

# InnoDB Storage Engine and Clustered Indexes

## Purpose

MySQL's default engine organizing tables as clustered B+Trees with secondary indexes, undo logs, and the buffer pool.

## Storage Layout

- InnoDB stores every table as a clustered index: the primary key B+Tree holds the full row in its leaf nodes, so rows are physically ordered by primary key.
- If no primary key is declared, InnoDB uses the first non-null unique index, or synthesizes a hidden 6-byte row ID as the clustering key.
- Secondary indexes store the indexed columns plus the primary key value, not a physical row pointer; a secondary lookup that needs other columns does a second probe into the clustered index.
- Because rows live in the primary index, a wide or randomly ordered primary key inflates every secondary index and causes page splits on insert.

## Transactions and MVCC

- InnoDB implements MVCC via undo logs: old row versions are kept in the undo tablespace so read views can reconstruct the version visible to their transaction.
- The redo log provides crash recovery and durability, while the undo log provides rollback and consistent reads; purge threads later remove undo no longer needed by any snapshot.
- The buffer pool caches data and index pages; the change buffer defers and merges secondary-index modifications for pages not currently in memory.
- Row-level locking plus MVCC lets readers proceed without blocking writers under the default repeatable-read isolation.

## Sources

- MySQL Documentation - InnoDB Storage Engine - https://dev.mysql.com/doc/refman/8.0/en/innodb-storage-engine.html
- MySQL Documentation - Clustered and Secondary Indexes - https://dev.mysql.com/doc/refman/8.0/en/innodb-index-types.html
- MySQL Documentation - InnoDB Multi-Versioning - https://dev.mysql.com/doc/refman/8.0/en/innodb-multi-versioning.html

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
