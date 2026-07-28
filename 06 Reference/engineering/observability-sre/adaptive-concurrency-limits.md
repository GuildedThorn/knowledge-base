---
summary: "Adaptive concurrency limits dynamically control in-flight work so services shed load before latency collapse and cascading failure."
status: active
tags: [reference, engineering, sre, resilience, load-shedding]
private: false
---

# Adaptive Concurrency Limits

## Purpose

Adaptive concurrency limiting controls how many requests a service allows in flight at once, using latency feedback to reduce overload without relying on a permanently fixed limit.

## Core Model

- A service has an effective concurrency limit beyond which queueing grows faster than useful throughput.
- Static limits become stale when topology, hardware, traffic mix, downstream health, or code changes.
- Adaptive algorithms probe for available capacity, observe latency, and adjust the allowed in-flight request count.
- The goal is graceful load shedding before the system hits retry storms, thread-pool exhaustion, or cascading failure.

## Design Notes

- Concurrency is not the same as QPS; by Little's Law, in-flight work relates to throughput and latency.
- Limit at ingress and at expensive dependency boundaries.
- Return fast failure when saturated; slow acceptance often causes worse tail latency.
- Track accepted, rejected, completed, timeout, and latency distributions separately.
- Combine with deadlines and retry budgets so rejected work does not instantly reappear as amplified retry load.

## Operational Notes

- Watch p95/p99 latency, rejection rate, queue depth, saturation signals, and downstream error rates.
- Validate behavior under load tests that include dependency latency, partial failure, and recovery.
- Per-endpoint or per-workload limits are usually better than one global process limit.
- Adaptive limiters need sane floors and ceilings; unlimited probing under failure can be dangerous.

## Sources

- Netflix Technology Blog - Performance Under Load / Adaptive Concurrency Limits - https://netflixtechblog.medium.com/performance-under-load-3e6fa9a60581
- Netflix concurrency-limits library - https://github.com/Netflix/concurrency-limits
- Google SRE Book - Handling Overload - https://sre.google/sre-book/handling-overload/
- Google SRE Book - Addressing Cascading Failures - https://sre.google/sre-book/addressing-cascading-failures/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Capacity Planning and Load Testing](kb://06-reference-engineering-observability-sre-capacity-planning-and-load-testing)
- [Timeouts, Retries, Backoff, and Jitter](kb://06-reference-engineering-observability-sre-timeouts-retries-backoff-jitter)
