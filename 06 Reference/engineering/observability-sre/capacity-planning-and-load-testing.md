---
summary: "Capacity planning estimates resource headroom and scaling limits; load testing verifies them under controlled workload models."
status: active
tags: [reference, engineering, sre, capacity]
private: false
---

# Capacity Planning and Load Testing

## Purpose

Capacity planning estimates resource headroom and scaling limits; load testing verifies them under controlled workload models.

## Core Model

- Useful models include arrival rate, concurrency, service time, queueing, saturation, and bottleneck resource.
- Load tests should represent request mix, data shape, cache state, dependencies, and ramp patterns.
- Tail latency rises sharply near saturation because queues form.

## Engineering Notes

- Define success criteria before tests: latency percentiles, error rate, throughput, saturation, and recovery behavior.
- Test steady-state, spikes, cold start, dependency slowdown, and overload protection.
- Keep production safeguards: isolated environments, rate limits, kill switches, and stakeholder notice.

## Sources

- Google SRE Book - Addressing cascading failures - https://sre.google/sre-book/addressing-cascading-failures/
- k6 documentation - https://grafana.com/docs/k6/latest/
- Little's Law overview - https://en.wikipedia.org/wiki/Little%27s_law

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
