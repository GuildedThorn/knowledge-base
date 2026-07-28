---
summary: "Google's Dapper paper introducing low-overhead, always-on distributed request tracing via propagated trace and span context."
status: active
tags: [reference, engineering, sre, tracing, spans, paper]
private: false
---

# Distributed Tracing (Dapper)

## Purpose

Google's Dapper paper introducing low-overhead, always-on distributed request tracing via propagated trace and span context.

## Trace and Span Model

- A trace represents one end-to-end request and is a tree of spans, each span a named unit of work with start and end timestamps.
- Spans carry a span ID and a parent span ID, forming causal parent/child relationships across service boundaries.
- Annotations and key/value tags attach timing events and metadata (RPC names, hosts, errors) to spans.
- Because the model is language- and RPC-framework agnostic, it composes across a large heterogeneous service graph.

## Context Propagation

- A shared trace context (trace ID plus current span ID) travels in-band with the request, injected into RPC metadata and thread-local storage.
- Each hop starts a child span and forwards the context, so the full call tree can be reassembled out-of-band from collected span records.
- This propagation is the foundation later standardized by OpenTracing, OpenCensus, and OpenTelemetry / W3C Trace Context.

## Low Overhead

- Dapper is always-on but uses sampling (only a fraction of requests are fully traced) to bound CPU, memory, and storage cost.
- Sampling plus asynchronous, out-of-band span collection keeps production latency impact negligible.

## Sources

- Dapper Paper - https://research.google/pubs/pub36356/
- Dapper Overview - https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
