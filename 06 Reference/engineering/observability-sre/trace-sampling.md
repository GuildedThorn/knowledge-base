---
summary: "Head vs tail sampling and probabilistic/rate-limiting policies that control trace volume while preserving useful signal."
status: active
tags: [reference, engineering, sre, tracing, sampling, cost]
private: false
---

# Trace Sampling Strategies

## Purpose

Head vs tail sampling and probabilistic/rate-limiting policies that control trace volume while preserving useful signal.

## Head vs Tail Sampling

- Head sampling decides at trace start, before the outcome is known, so the choice propagates via the sampled flag to all downstream spans.
- Head sampling is cheap and stateless but cannot preferentially keep errors or slow traces it hasn't seen yet.
- Tail sampling buffers all spans of a trace and decides after completion, allowing policies keyed on latency, errors, or attributes.
- Tail sampling requires holding spans in memory and reassembling full traces, adding cost and needing a gateway collector.

## Sampler Types

- Probabilistic (percentage) samplers keep a fixed fraction of traces, e.g. 10%, using a deterministic hash of the trace-id.
- Rate-limiting samplers cap traces per second to bound throughput regardless of traffic spikes.
- Parent-based samplers respect the upstream decision to keep a trace whole; composite samplers combine parent and probabilistic logic.

## Cost vs Fidelity

- Lower sampling rates cut storage and export cost but risk missing rare errors and skewing latency percentiles.
- Tail sampling improves fidelity for the traces that matter (errors, high latency) at the price of collector resources.
- A common pattern is head-sample high for keep-all baseline plus tail policies that retain anomalies.

## Sources

- OpenTelemetry Sampling - https://opentelemetry.io/docs/concepts/sampling/
- OTel Collector Tail Sampling - https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/tailsamplingprocessor

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
