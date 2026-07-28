---
summary: "Open standard that condenses response-time measurements into a 0-1 user-satisfaction score using a target threshold T."
status: active
tags: [reference, engineering, sre, latency, user-experience, metric]
private: false
---

# Apdex Score

## Purpose

Open standard that condenses response-time measurements into a 0-1 user-satisfaction score using a target threshold T.

## Core Model

- Apdex (Application Performance Index) buckets each sampled response time relative to a target threshold T set by the operator.
- Satisfied: response time <= T. Tolerating: response time between T and 4T. Frustrated: response time > 4T (or the request failed/errored).
- The threshold F for frustrated requests is fixed by the spec at 4 x T, so choosing T alone defines all three bands.

## Score Computation

- Apdex_T = (Satisfied count + Tolerating count / 2) / total samples.
- The result is a decimal from 0 (all frustrated) to 1 (all satisfied), conventionally reported to two decimals with the T value, e.g. Apdex(0.5) = 0.90.
- Because tolerating requests count as half, the score cleanly maps a latency distribution to a single user-centric number.

## Tradeoffs

- Simplicity is the strength: one number communicates experience to non-engineers, unlike a raw percentile.
- The choice of T is subjective and dominates the score; too-lax a T flatters the service, too-strict a T makes it look broken.
- Apdex discards distribution shape and cannot distinguish a uniformly-slow service from one with a heavy tail once bucketed.
- It complements, rather than replaces, latency percentiles (p50/p95/p99) and SLOs, which retain more detail.

## Sources

- Apdex Alliance - https://www.apdex.org/
- Apdex Technical Specification - https://www.apdex.org/wp-content/uploads/2020/09/ApdexTechnicalSpecificationV11_000.pdf

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
