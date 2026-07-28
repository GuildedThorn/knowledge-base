---
summary: "Lightweight UDP text protocol and daemon for aggregating application counters, timers, and gauges before flushing to a backend."
status: active
tags: [reference, engineering, sre, metrics, udp, aggregation]
private: false
---

# StatsD Metrics Protocol

## Purpose

Lightweight UDP text protocol and daemon for aggregating application counters, timers, and gauges before flushing to a backend.

## How It Works

- StatsD originated at Etsy as a simple Node.js daemon that listens for metrics sent as plain-text lines, traditionally over connectionless UDP.
- Applications fire fire-and-forget packets; UDP means a metrics outage or slow daemon never blocks or errors the sending application.
- The daemon buffers incoming samples in memory and aggregates them over a fixed flush interval (commonly 10 seconds) before emitting results downstream.
- Flushed aggregates are pushed to a backend such as Graphite, and other backends and forwarders exist through pluggable configuration.

## Core Model

- The line format is `<metric.name>:<value>|<type>`, optionally with a sampling suffix `|@<rate>` to scale down high-frequency counters.
- Counters (`|c`) sum over the flush window and are reported as a total and a per-second rate.
- Gauges (`|g`) hold a last-set value, with `+`/`-` prefixes supported for relative adjustment.
- Timers (`|ms`) collect a distribution over the window, yielding statistics such as mean, upper bounds, and percentiles; sets (`|s`) count unique values.

## Engineering Notes

- Client-side pre-aggregation keeps application overhead minimal and shifts computation into the daemon rather than the metrics store.
- Sampling rates reduce packet volume for hot paths, and the daemon rescales counts to compensate for the dropped samples.
- The DogStatsD extension adds tags and histograms, and many agents (including Telegraf and the Datadog Agent) speak the StatsD wire format.

## Sources

- StatsD Project - https://github.com/statsd/statsd
- Measure Anything, Measure Everything - https://www.etsy.com/codeascraft/measure-anything-measure-everything/

---
## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
