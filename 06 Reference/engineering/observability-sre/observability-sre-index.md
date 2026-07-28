---
summary: "SRE, observability, alerting, traces, metrics, logs, incident management, capacity, and operations notes."
status: active
tags: [reference, engineering, sre, observability, index]
private: false
---

# Observability and SRE - Index

## Purpose

SRE, observability, alerting, traces, metrics, logs, incident management, capacity, and operations notes.

## Notes

- [Adaptive Concurrency Limits](kb://06-reference-engineering-observability-sre-adaptive-concurrency-limits) - Adaptive concurrency limits dynamically control in-flight work so services shed load before latency collapse and cascading failure.
- [Alerting on Symptoms](kb://06-reference-engineering-observability-sre-alerting-on-symptoms) - Good alerts fire on user-visible symptoms and actionable risk, not every internal cause or noisy metric threshold.
- [Capacity Planning and Load Testing](kb://06-reference-engineering-observability-sre-capacity-planning-and-load-testing) - Capacity planning estimates resource headroom and scaling limits; load testing verifies them under controlled workload models.
- [Chaos Engineering](kb://06-reference-engineering-observability-sre-chaos-engineering) - Chaos engineering tests system resilience by injecting controlled failure and validating that expected protections actually work.
- [Cloudflare 2019 WAF Outage](kb://06-reference-engineering-observability-sre-cloudflare-2019-waf-outage) - Cloudflare's 2019 WAF outage shows how unsafe regex, global rollout, and operational coupling can create a global CPU-exhaustion incident.
- [Distributed Tracing](kb://06-reference-engineering-observability-sre-distributed-tracing) - Distributed tracing follows a request across services using trace IDs, spans, timing, attributes, and context propagation.
- [Incident Management and Postmortems](kb://06-reference-engineering-observability-sre-incident-management-and-postmortems) - Incident management coordinates detection, roles, communication, mitigation, and learning without turning postmortems into blame sessions.
- [Logs, Loki, and Structured Logging](kb://06-reference-engineering-observability-sre-logs-loki-and-structured-logging) - Structured logs preserve event details for investigation while label/index choices determine cost and query performance.
- [OpenTelemetry Collector](kb://06-reference-engineering-observability-sre-opentelemetry-collector) - The OpenTelemetry Collector receives, processes, and exports telemetry, giving teams a vendor-neutral control point.
- [Prometheus Metrics](kb://06-reference-engineering-observability-sre-metrics-prometheus) - Prometheus collects time-series metrics through pull-based scraping, labels, PromQL, recording rules, and alerting rules.
- [Runbooks and On-Call Operations](kb://06-reference-engineering-observability-sre-runbooks-and-oncall) - Runbooks turn operational knowledge into executable diagnosis and mitigation steps for humans under time pressure.
- [SLIs, SLOs, and Error Budgets](kb://06-reference-engineering-observability-sre-sli-slo-error-budgets) - SRE uses service level indicators, objectives, and error budgets to connect reliability work to user-visible outcomes.
- [Timeouts, Retries, Backoff, and Jitter](kb://06-reference-engineering-observability-sre-timeouts-retries-backoff-jitter) - Timeouts, retries, exponential backoff, and jitter prevent small distributed-system failures from becoming synchronized overload.

## Related

- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Engineering Source Corpus](kb://06-reference-engineering-engineering-source-corpus)
- [Reference Map](kb://01-maps-reference-map)
