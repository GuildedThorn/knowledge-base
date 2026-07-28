---
summary: "Chaos engineering tests system resilience by injecting controlled failure and validating that expected protections actually work."
status: active
tags: [reference, engineering, sre, chaos]
private: false
---

# Chaos Engineering

## Purpose

Chaos engineering tests system resilience by injecting controlled failure and validating that expected protections actually work.

## Core Model

- Experiments start from a steady-state hypothesis.
- Failure injection can target instances, zones, dependencies, latency, packet loss, CPU, disk, memory, or credentials.
- Blast radius controls determine whether experiments are safe enough for production.

## Engineering Notes

- Start with game days and staging experiments before production automation.
- Abort automatically when SLOs or guardrails are threatened.
- Turn findings into reliability fixes, not just impressive outage simulations.

## Sources

- Principles of Chaos Engineering - https://principlesofchaos.org/
- Netflix - Chaos Engineering - https://netflixtechblog.com/tagged/chaos-engineering
- Google SRE Workbook - Testing for reliability - https://sre.google/workbook/testing-reliability/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
