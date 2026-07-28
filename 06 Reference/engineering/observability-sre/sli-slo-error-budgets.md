---
summary: "SRE uses service level indicators, objectives, and error budgets to connect reliability work to user-visible outcomes."
status: active
tags: [reference, engineering, sre, slo]
private: false
---

# SLIs, SLOs, and Error Budgets

## Purpose

SRE uses service level indicators, objectives, and error budgets to connect reliability work to user-visible outcomes.

## Core Model

- An SLI measures a user-relevant property such as availability, latency, correctness, or freshness.
- An SLO sets a target over a window; the error budget is the allowed failure amount.
- Error budgets turn reliability from vague desire into release/risk tradeoff.

## Engineering Notes

- Define SLIs at user journeys and API boundaries, not only host metrics.
- Use burn-rate alerts to catch fast budget exhaustion and slow chronic degradation.
- Review SLOs regularly; bad SLOs either page constantly or hide real user pain.

## Sources

- Google SRE Book - Service Level Objectives - https://sre.google/sre-book/service-level-objectives/
- Google SRE Workbook - SLOs - https://sre.google/workbook/implementing-slos/
- OpenSLO specification - https://openslo.com/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
