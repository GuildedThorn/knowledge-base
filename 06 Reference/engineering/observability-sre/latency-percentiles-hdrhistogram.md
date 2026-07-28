---
summary: "Techniques for recording latency distributions and tail percentiles accurately using high-dynamic-range histograms, not averages."
status: active
tags: [reference, engineering, sre, latency, histograms, percentiles]
private: false
---

# Latency Percentiles and HdrHistogram

## Purpose

Techniques for accurately recording latency distributions and tail percentiles using high-dynamic-range histograms rather than averages.

## Why Averages Hide Tails

- A mean collapses the distribution to one number and is dominated by the common case, so it says almost nothing about the slow tail users feel.
- Latency is rarely normally distributed; it is long-tailed, so p99 and p99.9 can be orders of magnitude larger than the median.
- Fan-out amplifies tails: a request touching many services is as slow as its slowest dependency, so rare per-service tail latency becomes common end-to-end.
- Report percentiles (p50, p90, p99, p99.9) and a max, not averages, to characterize user-visible latency.

## HDR Histogram Buckets

- HdrHistogram records values across a configurable dynamic range at constant relative precision, using logarithmically sized buckets with fixed sub-bucket resolution.
- It bounds memory and gives fixed-cost, lossless recording so any quantile can be read back after the fact.
- Histograms are mergeable across instances and time windows, unlike pre-computed percentiles which cannot be averaged.

## Coordinated Omission and Quantile Estimation

- Coordinated omission: when a slow request stalls a load generator, subsequent requests are never sent, so the worst latencies are silently dropped and percentiles look better than reality.
- HdrHistogram offers correction by expected interval, back-filling the samples that omission would have hidden.
- Server-side quantile estimation from bucketed histograms (e.g. Prometheus `histogram_quantile`) is approximate; accuracy depends on bucket boundaries near the percentile of interest.

## Sources

- HdrHistogram - http://hdrhistogram.org/
- How NOT to Measure Latency (Gil Tene) - https://www.infoq.com/presentations/latency-response-time/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
