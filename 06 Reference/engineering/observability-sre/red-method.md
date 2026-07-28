---
summary: "Service-level monitoring pattern tracking Rate, Errors, and Duration for each request-driven service in a microservice architecture."
status: active
tags: [reference, engineering, sre, monitoring, microservices, methodology]
private: false
---

# The RED Method

## Purpose

Service-level monitoring pattern tracking Rate, Errors, and Duration for each request-driven service in a microservice architecture.

## Rate, Errors, Duration

- Rate: the number of requests per second the service is handling, measuring demand on that service.
- Errors: the number (or rate) of those requests that failed, typically split out as a ratio of failed to total.
- Duration: the distribution of time each request takes, tracked as latency percentiles rather than a single average.
- The three metrics are derived from the same request stream, so a single instrumentation point per service yields all of RED.

## Relation to USE and Golden Signals

- RED is the workload-oriented complement to the resource-oriented USE method: RED watches the service, USE watches the machine.
- It is effectively the Four Golden Signals minus saturation, focused on the request path of a service.
- Because every microservice is measured the same way, RED gives a uniform mental model and consistent dashboards across a fleet.

## Per-Service Dashboards

- A standard RED dashboard row per service shows request rate, error rate/ratio, and a latency-percentile panel (p50/p90/p99).
- Uniformity lets on-call engineers reason about any service without learning bespoke metrics, speeding triage.
- Errors and duration are the symptom signals to alert on; rate provides context for interpreting them.

## Sources

- The RED Method - https://grafana.com/blog/2018/08/02/the-red-method-how-to-instrument-your-services/
- The RED Method: A New Approach to Monitoring Microservices - https://thenewstack.io/monitoring-microservices-red-method/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
