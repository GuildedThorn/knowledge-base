---
summary: "CNCF log processors that collect, parse, buffer, and route logs and metrics through a unified pluggable pipeline."
status: active
tags: [reference, engineering, sre, logging, pipeline, forwarding]
private: false
---

# Fluentd and Fluent Bit

## Purpose

CNCF log processors that collect, parse, buffer, and route logs and metrics through a unified pluggable pipeline.

## Pipeline Model

- Events flow through input plugins, optional filter and parser plugins, and output plugins, matched by tag routing.
- Records are structured as a tag, timestamp, and JSON-like key/value map, so downstream systems receive consistent events.
- Filters enrich, redact, or reshape records; parsers turn unstructured lines (regex, JSON, LTSV) into fields.
- A broad plugin ecosystem routes to Elasticsearch, Loki, S3, Kafka, and cloud logging backends.

## Buffering and Reliability

- Buffers stage records in memory or on file, flushing in configurable chunks to smooth bursts and backpressure.
- Failed flushes are retried with exponential backoff, and persistent file buffers survive process restarts.

## Fluentd vs Fluent Bit

- Fluentd is Ruby/C-based, feature-rich, and plugin-heavy, suited to aggregator roles handling many sources.
- Fluent Bit is a lightweight C agent with a small memory footprint, ideal as a per-node/edge collector and DaemonSet in Kubernetes.
- A common pattern uses Fluent Bit as the forwarder feeding a central Fluentd aggregator.

## Sources

- Fluentd Documentation - https://docs.fluentd.org/
- Fluent Bit Documentation - https://docs.fluentbit.io/manual

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
