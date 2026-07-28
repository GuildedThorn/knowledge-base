---
summary: "Runbooks turn operational knowledge into executable diagnosis and mitigation steps for humans under time pressure."
status: active
tags: [reference, engineering, sre, runbooks]
private: false
---

# Runbooks and On-Call Operations

## Purpose

Runbooks turn operational knowledge into executable diagnosis and mitigation steps for humans under time pressure.

## Core Model

- A good runbook states symptom, impact, likely causes, dashboards, commands, rollback/mitigation, and escalation path.
- On-call load is a production reliability signal, not just a staffing problem.
- Runbooks decay unless incidents and drills keep them current.

## Engineering Notes

- Link every paging alert to a runbook with owner and last-reviewed date.
- Prefer safe read-only diagnostics first, then bounded mitigation actions.
- After incidents, update the runbook where the responder hesitated or had to improvise.

## Sources

- Google SRE Book - Being on-call - https://sre.google/sre-book/being-on-call/
- PagerDuty Runbook Automation - https://www.pagerduty.com/resources/learn/what-is-a-runbook/
- Grafana OnCall docs - https://grafana.com/docs/oncall/latest/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
