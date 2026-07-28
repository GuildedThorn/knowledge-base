---
summary: "Adds global query, HA deduplication, and unlimited object-storage retention on top of vanilla Prometheus instances."
status: active
tags: [reference, engineering, sre, metrics, ha, object-storage]
private: false
---

# Thanos Long-Term Metrics

## Purpose

System that adds global query, HA deduplication, and unlimited object-storage retention on top of vanilla Prometheus instances.

## Core Model

- A Sidecar runs next to each Prometheus, exposing its data over the Thanos StoreAPI and uploading closed TSDB blocks to object storage (S3, GCS, Azure, etc.).
- The Store Gateway serves those historical blocks from the bucket, decoupling long-term retention from local Prometheus disk.
- The Querier fans out to all StoreAPI endpoints (sidecars and gateways) and merges results, giving a single global view across clusters.
- Optional Receive component ingests remote-write directly, useful when sidecar-per-Prometheus is impractical.

## How It Works

- Deduplication uses external labels (e.g. `replica`) so two HA Prometheus replicas scraping the same targets return one clean series at query time.
- The Compactor merges, deduplicates, and compacts blocks in object storage, and applies retention policies per resolution.
- Downsampling produces 5m and 1h resolution aggregates so long-range queries stay fast without scanning raw samples.
- Because storage is an object bucket, retention is effectively unlimited and constrained only by cost.

## Sources

- Thanos Project - https://thanos.io/
- Thanos Getting Started - https://thanos.io/tip/thanos/getting-started.md/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
