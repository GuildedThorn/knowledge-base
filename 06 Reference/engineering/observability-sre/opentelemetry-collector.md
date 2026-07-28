---
summary: "The OpenTelemetry Collector receives, processes, and exports telemetry, giving teams a vendor-neutral control point."
status: active
tags: [reference, engineering, observability, opentelemetry]
private: false
---

# OpenTelemetry Collector

## Purpose

The OpenTelemetry Collector receives, processes, and exports telemetry, giving teams a vendor-neutral control point.

## Core Model

- Collector pipelines combine receivers, processors, exporters, and extensions.
- It can run as an agent, gateway, sidecar, or managed component.
- Processors handle batching, filtering, memory limits, sampling, resource detection, and attribute transforms.

## Engineering Notes

- Use collectors to centralize vendor export, redaction, sampling, and routing policy.
- Set memory_limiter and batch processors before sending high-volume telemetry.
- Version collector configs and test them like production infrastructure.

## Sources

- OpenTelemetry Collector docs - https://opentelemetry.io/docs/collector/
- OpenTelemetry Collector configuration - https://opentelemetry.io/docs/collector/configuration/
- OpenTelemetry specification - https://opentelemetry.io/docs/specs/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
