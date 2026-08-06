---
summary: "W3C recommendation standardizing traceparent and tracestate HTTP headers so trace context propagates across vendors."
status: active
tags: [reference, engineering, sre, tracing, propagation, standard]
private: false
---

# W3C Trace Context

## Purpose

W3C recommendation standardizing traceparent and tracestate HTTP headers so trace context propagates across vendors.

## traceparent Format

- A single header carrying four hyphen-delimited fields: version, trace-id, parent-id (span-id), and trace-flags.
- trace-id is a 16-byte value and parent-id an 8-byte value, both hex-encoded; the trace-id identifies the whole distributed trace.
- trace-flags is an 8-bit field whose lowest bit (`sampled`) signals that the caller recorded and sampled the trace.
- Fixed, compact format lets any conforming system parse context without vendor-specific knowledge.

## tracestate Vendor Data

- tracestate carries additional vendor-specific key-value pairs alongside traceparent.
- It is an ordered list where the left-most entry is the most recent system to write; entries are opaque to other vendors.
- Lets multiple tracing systems coexist in one request without losing their proprietary state.

## Propagation Across Services

- Each hop reads the incoming traceparent, records a span, then forwards a traceparent with its own span-id as the new parent-id.
- Systems that do not recognize the headers must pass them through unchanged to preserve the chain.
- The standard underpins OpenTelemetry's default HTTP propagator, enabling end-to-end traces across mixed toolchains.

## Sources

- W3C Trace Context - https://www.w3.org/TR/trace-context/
- Trace Context Overview - https://www.w3.org/TR/trace-context/#overview

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
