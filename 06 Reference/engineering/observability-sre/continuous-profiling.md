---
summary: "Always-on fleet-wide profiling that samples CPU, memory, and locks across production to attribute resource cost over time."
status: active
tags: [reference, engineering, sre, profiling, production, cost]
private: false
---

# Continuous Profiling

## Purpose

Always-on fleet-wide profiling that samples CPU, memory, and locks across production to attribute resource cost over time.

## How It Works

- Statistical sampling at a low frequency (e.g. ~100 Hz per CPU) keeps per-host overhead to roughly 1% or less, making always-on profiling in production viable.
- Agents collect stack traces for CPU time, heap allocations, off-CPU/lock contention, and goroutine/thread state, tagging each sample with labels (service, version, host, region).
- Raw stacks are symbolized against debug info (DWARF, or unwound via frame pointers / eBPF), turning addresses into function names and line numbers.
- Samples are folded into flame graphs and stored as time series so cost can be sliced by any label dimension.

## Engineering Notes

- Google-Wide Profiling (GWP) pioneered continuous datacenter-scale profiling, sampling a small fraction of machines continuously to answer "where do our CPU cycles go" across the fleet.
- Modern implementations (Parca, Pyroscope, Grafana) use eBPF to profile unmodified binaries system-wide without per-process instrumentation.
- Storing profiles over time lets you diff releases: a deploy that regresses CPU or allocation cost shows up as a widened flame graph frame.
- Cost attribution ties CPU seconds back to services and code paths, informing capacity planning and efficiency work (dollars per function).
- Symbolization is the hard part for stripped or JIT/interpreted runtimes; debug symbols must be retained or resolved out-of-band.

## Sources

- Google-Wide Profiling Paper - https://research.google/pubs/pub36575/
- Parca Documentation - https://www.parca.dev/docs/overview/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
