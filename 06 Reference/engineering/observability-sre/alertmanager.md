---
summary: "Component that deduplicates, groups, silences, and routes Prometheus alerts to receivers with inhibition and notification policies."
status: active
tags: [reference, engineering, sre, alerting, routing, notifications]
private: false
---

# Prometheus Alertmanager

## Purpose

Component that deduplicates, groups, silences, and routes Prometheus alerts to receivers with inhibition and notification policies.

## How It Works

- Prometheus servers evaluate alerting rules and push firing/resolved alerts to Alertmanager over HTTP; Alertmanager owns notification, not detection.
- Alerts carry labels; the routing tree matches on labels to select a receiver and per-node timing (group_wait, group_interval, repeat_interval).
- Grouping bundles related alerts (e.g. all instances of one service) into a single notification, reducing pager noise during broad outages.
- Deduplication collapses identical alerts arriving from multiple redundant Prometheus replicas into one.

## Silences and Inhibition

- Silences mute notifications matching a label set for a bounded time window, used for planned maintenance; they are set via UI or API, not config.
- Inhibition suppresses lower-severity alerts when a related higher-severity alert is already firing (e.g. mute per-instance alerts when a whole-cluster-down alert fires).
- High availability runs Alertmanager as a gossiping cluster so replicas coordinate to send each notification once.

## Operational Notes

- Receivers integrate with email, PagerDuty, Slack, Opsgenie, webhooks, and more; message content is set with Go templating.
- Routing is a tree with a mandatory root receiver; `continue: true` lets an alert match multiple sibling routes.
- Alerting rules live in Prometheus config (`alerting_rules`), including `for` clauses to require a condition to hold before firing.
- Keep routing labels stable; the label set is the join key between rules, routing, silences, and inhibition.

## Sources

- Alertmanager Documentation - https://prometheus.io/docs/alerting/latest/alertmanager/
- Alerting Rules - https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
