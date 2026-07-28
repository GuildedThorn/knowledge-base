---
summary: "Brendan Gregg's visualization that aggregates sampled stack traces into a hierarchical view of where CPU time is spent."
status: active
tags: [reference, engineering, sre, profiling, cpu, visualization]
private: false
---

# Flame Graphs

## Purpose

Brendan Gregg's visualization that aggregates sampled stack traces into a hierarchical view of where CPU time is spent.

## Stack Sampling and Folding

- A profiler samples the running stack at a fixed frequency (e.g. 99 Hz) across the target process.
- Identical stacks are collapsed into "folded" lines with a count, so repeated call paths merge into one bar.
- The folded output is rendered to SVG, independent of the sampler that produced it (perf, DTrace, eBPF, language profilers).

## Reading Width and Depth

- The x-axis is not time: bar width is proportional to how often a frame appeared in samples, i.e. its share of CPU.
- The y-axis is stack depth, with callers below and callees stacked above them.
- Wide plateaus at the top indicate leaf functions consuming CPU directly; wide frames below aggregate their children.
- Ordering is alphabetical (to maximize merging), not chronological, so left-to-right position carries no meaning.

## Variants

- CPU flame graphs show on-CPU time; off-CPU flame graphs visualize blocked/waiting time from scheduler tracing.
- Differential flame graphs color-code the delta between two profiles to spot regressions.
- Icicle graphs invert the layout (root at top) for top-down reading.

## Sources

- Flame Graphs - https://www.brendangregg.com/flamegraphs.html
- The Flame Graph (ACM Queue) - https://queue.acm.org/detail.cfm?id=2927301

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
