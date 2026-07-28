---
summary: "Prometheus query language for selecting and aggregating time series, using instant/range vectors, rate functions, and label matchers."
status: active
tags: [reference, engineering, sre, query, promql, aggregation]
private: false
---

# PromQL Query Language

## Purpose

Prometheus query language for selecting and aggregating time series, using instant/range vectors, rate functions, and label matchers.

## Core Model

- Every PromQL expression evaluates to one of four types: instant vector, range vector, scalar, or string.
- An instant vector selector (e.g. `http_requests_total`) returns one sample per matching series at the evaluation timestamp.
- A range vector selector appends a duration in brackets (e.g. `http_requests_total[5m]`), returning a window of samples per series for functions to consume.
- Series are filtered by label matchers using `=`, `!=`, `=~` (regex), and `!~`; the metric name itself is the `__name__` label.

## Key Functions

- `rate()` and `irate()` compute per-second average rates from counter range vectors, correctly handling counter resets.
- `increase()` gives the total counter growth over a range window; both `rate` and `increase` require a range vector input.
- `histogram_quantile()` estimates quantiles (e.g. p95 latency) from `_bucket` series of a histogram metric.
- Aggregation operators (`sum`, `avg`, `max`, `min`, `count`, `topk`, `quantile`) collapse dimensions and accept `by (...)` or `without (...)` clauses to control grouping.

## Engineering Notes

- Rate then aggregate: apply `rate()` to raw counters before `sum by (...)`, never the reverse, or resets corrupt the result.
- Binary operators between vectors match on identical label sets unless `on(...)` / `ignoring(...)` and `group_left` / `group_right` reshape the join.
- Choose the range window as a multiple of the scrape interval (commonly 4x or more) so `rate()` has enough samples.

## Sources

- PromQL Basics - https://prometheus.io/docs/prometheus/latest/querying/basics/
- PromQL Functions - https://prometheus.io/docs/prometheus/latest/querying/functions/

---
## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
