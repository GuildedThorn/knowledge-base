---
summary: "Vendor-neutral standard for transmitting metrics, formalizing the Prometheus text format with typed samples, exemplars, and units."
status: active
tags: [reference, engineering, sre, standard, exposition, exemplars]
private: false
---

# OpenMetrics Exposition Format

## Purpose

Vendor-neutral standard for transmitting metrics, formalizing the Prometheus text format with typed samples, exemplars, and units.

## Core Model

- OpenMetrics is an open specification, developed under the CNCF, that standardizes how metrics are exposed and transmitted over the wire.
- It is built directly on and remains largely wire-compatible with the Prometheus text exposition format, aiming to make that de facto format a formal standard.
- Metrics are organized into families sharing a name, `TYPE`, `HELP`, and optional `UNIT` metadata line, with samples carrying label sets.
- Supported types include counter, gauge, histogram, summary, info, stateset, and gaugehistogram.

## Key Ideas

- Counter samples use an explicit `_total` suffix and may carry a `_created` timestamp marking when the series began.
- Exemplars attach a sample to an external reference such as a trace ID, enabling metric-to-trace correlation for exemplar-aware backends.
- A `UNIT` metadata field names the measurement unit, encouraging consistent, self-describing metrics.
- Both a text format (UTF-8, `application/openmetrics-text`) and a protobuf format are defined; the exposition ends with an explicit `# EOF` marker.

## Engineering Notes

- Prometheus can scrape OpenMetrics endpoints and negotiates the format via the HTTP `Accept` header during content negotiation.
- Because it extends the Prometheus format, most existing exporters and client libraries need only incremental changes to emit compliant output.
- Exemplar support is the main practical addition over the classic Prometheus format for teams unifying metrics and distributed tracing.

## Sources

- OpenMetrics Project - https://openmetrics.io/
- OpenMetrics Specification - https://github.com/OpenObservability/OpenMetrics/blob/main/specification/OpenMetrics.md

---
## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
