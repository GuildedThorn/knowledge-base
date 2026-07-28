---
summary: "Distributed tracing follows a request across services using trace IDs, spans, timing, attributes, and context propagation."
status: active
tags: [reference, engineering, observability, tracing]
private: false
---

# Distributed Tracing

## Purpose

Distributed tracing follows a request across services using trace IDs, spans, timing, attributes, and context propagation.

## Core Model

- A trace is a tree or DAG of spans representing work in services, queues, databases, and clients.
- Context propagation carries trace identity through process and network boundaries.
- Sampling balances observability cost against coverage of rare slow/error paths.

## Engineering Notes

- Propagate trace context at every boundary: HTTP, gRPC, queues, jobs, and browser/mobile clients where relevant.
- Add domain attributes that help triage, but avoid secrets and high-cardinality abuse.
- Correlate traces with logs and metrics through trace_id/span_id and exemplars.

## Sources

- OpenTelemetry traces - https://opentelemetry.io/docs/concepts/signals/traces/
- W3C Trace Context - https://www.w3.org/TR/trace-context/
- Dapper paper - https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
