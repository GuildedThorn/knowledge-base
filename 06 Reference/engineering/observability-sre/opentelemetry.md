---
summary: "CNCF standard and SDKs for generating and exporting traces, metrics, and logs via a vendor-neutral collector and protocol."
status: active
tags: [reference, engineering, sre, telemetry, otlp, instrumentation]
private: false
---

# OpenTelemetry

## Purpose

CNCF standard and SDKs for generating and exporting traces, metrics, and logs through a vendor-neutral collector and protocol.

## Signals and API/SDK

- Defines three signals: traces (spans of causally-linked work), metrics (aggregated measurements), and logs (timestamped records), unified by shared resource and context.
- The API is a thin, stable instrumentation surface; the SDK provides the configurable implementation (samplers, processors, exporters).
- Separating API from SDK lets libraries instrument against the API with no runtime cost until an application wires up an SDK.
- Context propagation carries trace and baggage state across process and thread boundaries.

## OTLP and the Collector

- OTLP (OpenTelemetry Protocol) is the native wire format, transported over gRPC or HTTP with Protobuf payloads.
- The Collector is a standalone binary with receivers, processors, and exporters, run as an agent (per-host) or gateway (centralized).
- The Collector decouples telemetry producers from vendor backends, enabling batching, filtering, and re-routing without touching app code.

## Auto vs Manual Instrumentation

- Auto-instrumentation uses language agents or bytecode/monkey-patch hooks to capture common frameworks (HTTP, DB, gRPC) with no code changes.
- Manual instrumentation adds custom spans, attributes, and metrics for domain-specific logic.
- Semantic conventions standardize attribute names (e.g. `http.request.method`) so data is portable across backends.

## Sources

- OpenTelemetry Documentation - https://opentelemetry.io/docs/
- OpenTelemetry Specification - https://opentelemetry.io/docs/specs/otel/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
