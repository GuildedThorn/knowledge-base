---
summary: "Open-source visualization platform unifying metrics, logs, and traces across many data sources with templating and alerting."
status: active
tags: [reference, engineering, sre, visualization, dashboards, alerting]
private: false
---

# Grafana Dashboards

## Purpose

Open-source visualization and dashboarding platform that unifies metrics, logs, and traces across many data sources with templating and alerting.

## Data Sources and Panels

- Connects to time-series and log backends including Prometheus, Loki, Tempo, Graphite, InfluxDB, Elasticsearch, and SQL databases through pluggable data source plugins.
- Panels are the atomic unit of a dashboard; each runs one or more queries and renders as time series, stat, gauge, table, heatmap, logs, or bar chart.
- A single dashboard can mix data sources, letting one view correlate metrics, logs, and traces (exemplars link a metric point to its trace).
- Transformations post-process query results (join, filter, group by, calculate fields) without changing the underlying query.

## Template Variables

- Variables make dashboards reusable by parameterizing queries; common types are query, custom, interval, datasource, and constant.
- Query variables populate dropdowns from live label values (e.g. `label_values(instance)`), so one dashboard serves every host or service.
- Multi-value and "All" variables expand into regex or list interpolations used inside PromQL/LogQL queries.

## Dashboard-as-Code and Alerting

- Dashboards serialize to JSON and can be version-controlled, provisioned from files, or generated with tools like Grafonnet and Terraform.
- Grafana-managed alerts define rules on any data source, evaluate on a schedule, and route through notification policies to contact points.
- Alert rules support multi-condition expressions, "for" duration to suppress flapping, and labels that drive grouping and silences.

## Sources

- Grafana Documentation - https://grafana.com/docs/grafana/latest/
- Grafana Dashboards Guide - https://grafana.com/docs/grafana/latest/dashboards/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
