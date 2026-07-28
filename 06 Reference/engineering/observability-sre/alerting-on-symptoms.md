---
summary: "Good alerts fire on user-visible symptoms and actionable risk, not every internal cause or noisy metric threshold."
status: active
tags: [reference, engineering, sre, alerting]
private: false
---

# Alerting on Symptoms

## Purpose

Good alerts fire on user-visible symptoms and actionable risk, not every internal cause or noisy metric threshold.

## Core Model

- Symptom alerts ask whether users are hurt; cause alerts help diagnosis but should rarely page alone.
- Page alerts need urgency, actionability, and ownership.
- Burn-rate alerts detect SLO budget exhaustion across multiple windows.

## Engineering Notes

- Every paging alert should have a runbook and an owner.
- Remove or downgrade alerts that consistently require no action.
- Keep dashboards for diagnosis separate from paging policy.

## Sources

- Google SRE Book - Monitoring distributed systems - https://sre.google/sre-book/monitoring-distributed-systems/
- Prometheus alerting docs - https://prometheus.io/docs/alerting/latest/overview/
- Grafana alerting docs - https://grafana.com/docs/grafana/latest/alerting/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
