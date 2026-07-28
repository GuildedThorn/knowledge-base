---
summary: "Spanner combines replication, transactions, SQL, and TrueTime uncertainty bounds to provide externally consistent distributed transactions."
status: active
tags: [reference, engineering, distributed-systems, spanner]
private: false
---

# Spanner and TrueTime

## Purpose

Spanner combines replication, transactions, SQL, and TrueTime uncertainty bounds to provide externally consistent distributed transactions.

## Core Model

- TrueTime exposes a bounded time interval, not a single exact timestamp.
- Commit-wait ensures transaction timestamps are in the past relative to uncertainty bounds.
- Spanner uses Paxos groups for replicated data and two-phase commit across participant groups.

## Engineering Notes

- Externally consistent global transactions are expensive and infrastructure-dependent; do not assume every distributed SQL system has Spanner's clock model.
- Keep multi-region transaction scope narrow and business-justified.
- Latency budgets must include quorum, commit wait, and cross-region network paths.

## Sources

- Google Spanner paper - https://research.google/pubs/spanner-googles-globally-distributed-database/
- Google Cloud Spanner docs - https://cloud.google.com/spanner/docs/true-time-external-consistency
- Calvin paper - https://cs.yale.edu/homes/thomson/publications/calvin-sigmod12.pdf

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
