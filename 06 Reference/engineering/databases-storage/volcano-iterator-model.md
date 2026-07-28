---
summary: "The pull-based open/next/close operator interface that composes query plans into pipelines of tuple-at-a-time operators."
status: active
tags: [reference, engineering, databases, execution, operators, volcano]
private: false
---

# Volcano Iterator Model

## Purpose

The pull-based open/next/close operator interface that composes query plans into pipelines of tuple-at-a-time operators.

## How It Works

- Every physical operator implements a uniform three-method interface: open, next, and close.
- Execution is demand-driven (pull): the root calls next, which recursively pulls tuples up the plan tree.
- One next call returns one tuple, so control flows one tuple at a time through the operator pipeline.
- The uniform interface lets any operator feed any other, making plans freely composable and the engine extensible.

## Pipelining and Parallelism

- Pipelinable operators (select, project) stream tuples without materializing intermediate results.
- Pipeline breakers (sort, hash-build, aggregation) must consume their full input before producing output.
- The exchange operator encapsulates parallelism, letting a serial operator tree run partitioned or replicated across threads.

## Tradeoffs

- One virtual function call per tuple per operator imposes heavy interpretation and branch-misprediction overhead.
- Tuple-at-a-time processing has poor CPU cache and instruction-level parallelism behavior on modern hardware.
- These costs motivated vectorized (batch-at-a-time) execution and query compilation as successors.

## Sources

- Graefe - Volcano: An Extensible and Parallel Query Evaluation System - https://dl.acm.org/doi/10.1109/69.273032
- Graefe - Query Evaluation Techniques for Large Databases - https://dl.acm.org/doi/10.1145/152610.152611
- Neumann - Efficiently Compiling Efficient Query Plans - https://www.vldb.org/pvldb/vol4/p539-neumann.pdf

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
