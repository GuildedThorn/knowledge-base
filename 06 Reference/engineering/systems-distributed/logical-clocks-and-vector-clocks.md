---
summary: "Logical clocks capture ordering without relying on synchronized wall clocks; vector clocks detect causality and concurrency."
status: active
tags: [reference, engineering, distributed-systems, clocks]
private: false
---

# Logical Clocks and Vector Clocks

## Purpose

Logical clocks capture ordering without relying on synchronized wall clocks; vector clocks detect causality and concurrency.

## Core Model

- Lamport clocks give a total-ish ordering consistent with happens-before but cannot detect concurrency.
- Vector clocks store per-node counters and can tell whether events are ordered or concurrent.
- Hybrid logical clocks combine physical time with logical counters for practical timestamp ordering.

## Engineering Notes

- Use logical clocks for causality, conflict detection, and debugging distributed traces.
- Do not treat NTP-synchronized wall-clock timestamps as proof of causality.
- Vector clocks grow with participant count, so production systems often bound, summarize, or replace them with domain-specific versions.

## Sources

- Lamport - Time, Clocks, and the Ordering of Events - https://lamport.azurewebsites.net/pubs/time-clocks.pdf
- Dynamo paper - https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
- CockroachDB - Hybrid logical clocks - https://www.cockroachlabs.com/blog/living-without-atomic-clocks/

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
