---
summary: "The cost and control of label cardinality in metric systems, where unbounded label values explode series count and storage."
status: active
tags: [reference, engineering, sre, cardinality, labels, tsdb]
private: false
---

# High-Cardinality Time Series

## Purpose

The cost and control of label cardinality in metric systems, where unbounded label values explode series count and storage.

## Cardinality Explosion Causes

- Each unique combination of a metric name and its label values is a distinct time series; total cardinality is the product of the cardinalities of the labels.
- Labels with unbounded value sets are the main culprit: user IDs, email addresses, full URLs, request IDs, timestamps, and raw error messages.
- Multiplicative growth is the trap: two moderate labels (say 100 endpoints and 100 status codes) combine into 10,000 series per metric.
- High cardinality drives memory, index size, and query cost in the TSDB and can destabilize ingestion (Prometheus keeps active series in memory).

## Label Design Rules

- Keep the value set of every label small and bounded; a label should partition data into a handful of groups, not identify individuals.
- Do not put anything with unbounded or user-controlled values into a label; carry that context in logs or traces instead of metrics.
- Follow naming conventions: base unit in the metric name, `_total` suffix for counters, and labels for dimensions you will actually aggregate over.

## Aggregation and Drop Strategies

- Aggregate away expensive dimensions at scrape or recording-rule time so stored series stay bounded.
- Use relabeling to drop or replace high-cardinality labels before ingestion, or bucket continuous values into ranges.
- Monitor your own cardinality (e.g. per-metric series counts, `scrape_samples`) and set limits so a single bad label cannot overwhelm the store.

## Sources

- Prometheus Instrumentation: Do Not Overuse Labels - https://prometheus.io/docs/practices/instrumentation/#do-not-overuse-labels
- Prometheus Metric and Label Naming - https://prometheus.io/docs/practices/naming/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
