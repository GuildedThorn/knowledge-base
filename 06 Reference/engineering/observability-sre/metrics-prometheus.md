---
summary: "Prometheus collects time-series metrics through pull-based scraping, labels, PromQL, recording rules, and alerting rules."
status: active
tags: [reference, engineering, observability, prometheus]
private: false
---

# Prometheus Metrics

## Purpose

Prometheus collects time-series metrics through pull-based scraping, labels, PromQL, recording rules, and alerting rules.

## Core Model

- Metrics are numeric time series with labels; label cardinality controls storage and query cost.
- Counters, gauges, histograms, and summaries model different measurement types.
- PromQL calculates rates, aggregations, joins, quantiles from histograms, and alert expressions.

## Engineering Notes

- Keep labels bounded and meaningful; user IDs, request IDs, and raw URLs are cardinality hazards.
- Use histograms for latency SLOs and aggregate by service/route/status where possible.
- Use recording rules for expensive repeated queries and dashboard stability.

## Sources

- Prometheus documentation - https://prometheus.io/docs/introduction/overview/
- Prometheus metric types - https://prometheus.io/docs/concepts/metric_types/
- Prometheus best practices - https://prometheus.io/docs/practices/naming/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
