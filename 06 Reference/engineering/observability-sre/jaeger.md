---
summary: "CNCF distributed tracing backend for collecting, storing, and visualizing spans to analyze latency and service dependencies."
status: active
tags: [reference, engineering, sre, tracing, backend, cncf]
private: false
---

# Jaeger

## Purpose

CNCF distributed tracing backend for collecting, storing, and visualizing spans to analyze latency and service dependencies.

## Architecture

- Collector receives spans (natively via OTLP), validates and processes them, then writes to storage.
- Query service reads spans from storage and serves the UI and API for retrieval and visualization.
- Storage is pluggable: Cassandra, Elasticsearch/OpenSearch, or in-memory/Badger for small deployments.
- Modern Jaeger (v2) is built on the OpenTelemetry Collector framework, consolidating the older agent/collector split.

## Span Ingestion

- Accepts OTLP over gRPC and HTTP; legacy Jaeger and Zipkin formats remain supported for migration.
- Spans are grouped by trace-id into complete traces spanning multiple services.
- Sampling can be client-driven or steered by remote sampling configuration served from the collector.

## Dependency and Latency Analysis

- The UI renders traces as Gantt-style timelines, exposing per-span duration and where latency accumulates.
- Aggregated span data yields a service dependency graph showing call relationships and traffic.
- Comparing traces and drilling into span tags helps isolate slow calls, errors, and fan-out amplification.

## Sources

- Jaeger Documentation - https://www.jaegertracing.io/docs/
- Jaeger Architecture - https://www.jaegertracing.io/docs/latest/architecture/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
