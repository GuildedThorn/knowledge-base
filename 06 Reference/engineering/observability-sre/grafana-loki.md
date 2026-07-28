---
summary: "Horizontally scalable log aggregation that indexes only labels and stores compressed log content in object storage."
status: active
tags: [reference, engineering, sre, logging, logql, object-storage]
private: false
---

# Grafana Loki

## Purpose

Horizontally scalable log aggregation system that indexes only labels and stores compressed log content in object storage.

## Indexing Model

- Unlike full-text engines, Loki indexes only a small set of stream labels (e.g. `job`, `namespace`, `pod`), not the log body.
- A unique combination of labels defines a stream; log lines within a stream are stored as compressed chunks.
- This keeps the index tiny and cheap, but discourages high-cardinality labels which cause stream explosion.
- The design is deliberately Prometheus-like, so the same label selectors apply across metrics and logs.

## Query and Storage

- LogQL mirrors PromQL: a stream selector like `{app="api"}` narrows streams, then filter and parse expressions (`|=`, `|~`, `| json`) refine lines.
- Metric queries over log streams (`rate`, `count_over_time`) turn logs into time series for alerting and dashboards.
- Chunks and index live in object storage (S3, GCS, Azure) via a single-store backend, decoupling compute from durable storage.
- Components (distributor, ingester, querier, compactor) scale independently in the microservices deployment mode.

## Sources

- Grafana Loki Documentation - https://grafana.com/docs/loki/latest/
- LogQL Reference - https://grafana.com/docs/loki/latest/query/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
