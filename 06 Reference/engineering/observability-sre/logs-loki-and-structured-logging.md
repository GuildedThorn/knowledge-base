---
summary: "Structured logs preserve event details for investigation while label/index choices determine cost and query performance."
status: active
tags: [reference, engineering, observability, logging]
private: false
---

# Logs, Loki, and Structured Logging

## Purpose

Structured logs preserve event details for investigation while label/index choices determine cost and query performance.

## Core Model

- Logs are high-cardinality event streams; metrics are aggregate time series; traces are request paths.
- Loki indexes labels and stores log content separately, making label discipline central.
- Structured fields make logs queryable without fragile text parsing.

## Engineering Notes

- Use stable low-cardinality labels for service, environment, level, component, and tenant where appropriate.
- Put request IDs, user IDs, error codes, and domain fields in structured log bodies, not Loki labels unless bounded.
- Sample noisy success logs but keep errors and security/audit events reliably retained.

## Sources

- Grafana Loki documentation - https://grafana.com/docs/loki/latest/
- OpenTelemetry logs - https://opentelemetry.io/docs/concepts/signals/logs/
- Google SRE Book - Monitoring distributed systems - https://sre.google/sre-book/monitoring-distributed-systems/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
