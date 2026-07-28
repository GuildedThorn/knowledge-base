---
summary: "Google SRE guidance to monitor latency, traffic, errors, and saturation as the core signals of a user-facing system's health."
status: active
tags: [reference, engineering, sre, monitoring, signals]
private: false
---

# The Four Golden Signals

## Purpose

Google SRE guidance to monitor latency, traffic, errors, and saturation as the core signals of a user-facing system's health.

## The Signals

- Latency: the time to serve a request. Successful and failed requests must be measured separately, since fast errors otherwise mask real latency.
- Traffic: demand on the system, expressed in a service-specific unit such as HTTP requests per second, sessions, or transactions.
- Errors: the rate of failed requests, counting explicit failures (HTTP 500s), implicit ones (wrong content, policy violation), and slow-but-successful responses.
- Saturation: how full the most constrained resource is (CPU, memory, I/O, queue depth); systems degrade before hitting 100%, so target a utilization threshold.

## Why They Generalize

- The four signals apply to almost any request-driven service without deep knowledge of its internals, making them a strong default for user-facing systems.
- They map to what users actually experience: is it working (errors), is it fast (latency), can it keep up (traffic and saturation).
- Saturation is forward-looking; rising saturation predicts imminent latency and error growth, giving lead time to react.

## Mapping Signals to Alerts

- Alert on symptoms users feel (elevated latency or error rate) rather than on every underlying cause, reducing pager noise.
- Use latency percentiles, not averages, so a slow tail is visible even when the mean looks healthy.
- Saturation drives capacity and predictive alerts; combine with error-budget burn rates for multi-window alerting.

## Sources

- SRE Book: Monitoring Distributed Systems - https://sre.google/sre-book/monitoring-distributed-systems/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
