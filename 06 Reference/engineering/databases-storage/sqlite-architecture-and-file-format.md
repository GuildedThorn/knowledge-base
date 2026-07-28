---
summary: "SQLite compiles SQL to bytecode executed by a virtual machine and persists databases as page-oriented single-file structures."
status: active
tags: [reference, engineering, databases, sqlite, storage]
private: false
---

# SQLite Architecture and File Format

## Purpose

SQLite is an embedded relational database engine. Its architecture is useful for understanding compiler-style SQL execution, virtual-machine databases, page formats, and application-file design.

## Core Model

- SQL text is compiled into bytecode.
- A virtual database engine executes the bytecode.
- The database usually lives in one main file.
- Pages are the basic on-disk unit.
- Rollback journals or WAL files provide crash recovery and transaction durability.
- B-trees store table and index data.

## Design Lessons

- An embedded DB can be a library, not a client/server system.
- A stable file format can make the database itself an application document format.
- SQL compilation and bytecode execution separate parsing/planning from runtime behavior.
- Single-file storage simplifies deployment but shifts concurrency and filesystem semantics into the engine.

## Engineering Notes

- SQLite is strong for local state, application files, edge devices, tests, and low-admin deployments.
- It is not a drop-in replacement for a multi-writer networked database.
- WAL mode changes concurrency and recovery behavior; understand the operational files, not just the `.db`.

## Sources

- SQLite - Architecture of SQLite - https://www.sqlite.org/arch.html
- SQLite - Database File Format - https://www.sqlite.org/fileformat.html
- SQLite - SQLite As An Application File Format - https://www.sqlite.org/appfileformat.html

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Relational Model and SQL](kb://06-reference-engineering-databases-storage-relational-model-and-sql)
- [Indexes: B-Tree, GIN, GiST, and BRIN](kb://06-reference-engineering-databases-storage-indexes-btree-gin-brin)
