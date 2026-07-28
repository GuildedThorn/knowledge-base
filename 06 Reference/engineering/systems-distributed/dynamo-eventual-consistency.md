---
summary: "Dynamo is Amazon's highly available key-value design using consistent hashing, quorums, vector clocks, sloppy quorum, and hinted handoff."
status: active
tags: [reference, engineering, distributed-systems, dynamo]
private: false
---

# Dynamo and Eventual Consistency

## Purpose

Dynamo is Amazon's highly available key-value design using consistent hashing, quorums, vector clocks, sloppy quorum, and hinted handoff.

## Core Model

- Consistent hashing distributes keys and reduces remapping when nodes change.
- N/R/W parameters tune durability, availability, and read/write consistency.
- Vector clocks detect divergent object versions so reconciliation can happen later.

## Engineering Notes

- Eventual consistency is an application contract; clients must tolerate or reconcile conflicts.
- Operational tuning affects correctness surface: sloppy quorum, read repair, anti-entropy, and hinted handoff all matter.
- Use conflict-free data types or explicit merge rules for data that can be concurrently edited.

## Sources

- Dynamo paper - https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
- Amazon Builders Library - https://aws.amazon.com/builders-library/
- Cassandra architecture - https://cassandra.apache.org/doc/latest/cassandra/architecture/overview.html

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
