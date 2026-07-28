---
summary: "Google's distributed load balancer using consistent hashing and connection tracking to spread flows across backends with minimal disruption."
status: active
tags: [reference, engineering, networking, maglev, loadbalancing, hashing]
private: false
---

# Maglev Software Load Balancer

## Purpose

Google's distributed load balancer using consistent hashing and connection tracking to spread flows across backends with minimal disruption.

## How It Works

- Runs as a userspace process on commodity Linux servers rather than dedicated hardware appliances.
- Upstream routers use ECMP to spread incoming packets equally across a set of equivalent Maglev machines.
- Each Maglev independently selects a backend for a packet's 5-tuple, so any machine handles any flow without shared state on the fast path.
- Kernel-bypass NIC access and per-packet processing let a single machine saturate 10 Gbps line rate.

## Consistent Hashing and Connection Tracking

- Maglev builds a fixed-size lookup table that maps hash buckets to backends, giving near-perfect load balance while remapping few entries when backends change.
- The table-generation algorithm favors minimal disruption: adding or removing a backend reassigns only a small fraction of buckets.
- A local connection-tracking table pins existing flows to their chosen backend, preserving affinity even when the hash table is regenerated.
- Combining consistent hashing with connection tracking keeps established connections stable across membership changes and machine failures.

## Sources

- Maglev: A Fast and Reliable Software Network Load Balancer - USENIX NSDI 2016 - https://www.usenix.org/conference/nsdi16/technical-sessions/presentation/eisenbud

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
