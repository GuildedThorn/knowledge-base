---
summary: "Column-oriented storage that stores attributes contiguously to accelerate analytical scans and enable heavy compression."
status: active
tags: [reference, engineering, databases, columnar, olap, storage]
private: false
---

# Columnar Storage (C-Store)

## Purpose

Column-oriented storage that stores attributes contiguously to accelerate analytical scans and enable heavy compression.

## Core Model

- Values of a single column are stored contiguously rather than interleaving all columns of a row.
- Analytical queries touch few columns over many rows; column layout reads only the needed attributes from disk.
- C-Store organizes data into overlapping projections, each a set of columns sorted on a chosen key.
- Introduced the read-optimized store (RS) plus a write-optimized store (WS) with a tuple mover between them.

## Compression and Materialization

- Contiguous same-type values compress far better than heterogeneous rows: run-length, dictionary, delta, and bit-packing.
- Sorted columns enable run-length encoding and let some operators run directly on compressed data.
- Late materialization defers stitching columns into rows until after predicates prune, minimizing work and I/O.

## Tradeoffs

- Read-optimized column stores excel at OLAP scans and aggregations but are poor for single-row point writes and updates.
- Reconstructing a full row requires gathering across many column files, costly for OLTP-style access.
- Apache Parquet applies these ideas as a portable on-disk columnar file format with per-column encoding.

## Sources

- Stonebraker et al. - C-Store: A Column-oriented DBMS - https://www.vldb.org/archives/website/2005/program/paper/thu/p553-stonebraker.pdf
- Abadi et al. - The Design and Implementation of Modern Column-Oriented Database Systems - https://dl.acm.org/doi/10.1561/1900000024
- Apache Parquet Documentation - https://parquet.apache.org/docs/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
