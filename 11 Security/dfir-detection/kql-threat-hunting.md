---
summary: "KQL is the query language behind Microsoft Sentinel and Defender for slicing large telemetry sets during hunts."
status: active
tags: [security, dfir, kql, kusto, hunting]
private: false
---

# Kusto Query Language for Threat Hunting

## Purpose

KQL is the query language behind Microsoft Sentinel and Defender for slicing large telemetry sets during hunts.

## Tabular Operators and Pipelines

- Queries begin with a table and pipe (`|`) results through successive operators, each consuming and emitting a tabular result.
- Core filters and shapers: `where`, `project`, `extend`, `sort`, `take`, and `distinct`.
- KQL is read-optimized and case-sensitive by default; `has` and `contains` differ in tokenization and performance.
- Time filtering with `where TimeGenerated > ago(24h)` should come early to prune data before heavier operations.

## Joins, Aggregation, and Time Series

- `summarize` aggregates with functions like `count()`, `dcount()`, `make_set()`, and `arg_max()`, grouped `by` fields.
- `join` correlates tables on keys; `bin()` buckets timestamps for `summarize` over time windows.
- `make-series` produces evenly-spaced series for anomaly detection with `series_decompose_anomalies()`.
- `let` statements name reusable subqueries and scalar values within a hunt.

## Hunting Patterns

- Microsoft Defender advanced hunting exposes tables like `DeviceProcessEvents`, `DeviceNetworkEvents`, and `IdentityLogonEvents`.
- Sentinel unifies logs across sources; queries can be promoted directly into analytics rules.
- Frequency and rare-event analysis (`summarize count() by ...` then filter) surfaces outliers indicating compromise.

## Sources

- KQL Reference - Microsoft Learn - https://learn.microsoft.com/en-us/kusto/query/
- Advanced Hunting KQL - https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-query-language

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
