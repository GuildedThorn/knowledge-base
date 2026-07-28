---
summary: "eBPF runs verified programs at kernel hook points using maps, helpers, program types, and verifier-enforced safety constraints."
status: active
tags: [reference, engineering, linux, ebpf, observability, networking]
private: false
---

# eBPF Programs, Maps, and Verifier

## Purpose

eBPF lets Linux systems attach small verified programs to kernel and userspace events for observability, networking, security, and performance work.

## Core Model

- Programs attach to hook points such as kprobes, tracepoints, uprobes, XDP, tc, cgroups, and LSM hooks.
- Program type determines context, allowed helpers, return meaning, and safety rules.
- Maps store state shared between eBPF programs and userspace.
- The verifier checks programs before load to prevent unsafe memory access and uncontrolled execution.
- JIT compilation can translate eBPF bytecode into native machine code.

## Engineering Notes

- eBPF is powerful because it puts logic near the event source.
- The verifier is the boundary between useful kernel extensibility and crashing the machine.
- Observability programs should control cardinality, map growth, and event volume.
- Security controls using eBPF need careful bypass analysis and kernel-version testing.

## Sources

- eBPF Docs - https://docs.ebpf.io/
- eBPF Docs - eBPF on Linux - https://docs.ebpf.io/linux/
- Linux Kernel Documentation - BPF - https://www.kernel.org/doc/html/v6.4/bpf/index.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Linux Debugging with strace, perf, and eBPF](kb://06-reference-engineering-linux-nix-systems-linux-debugging-strace-perf-bpf)
- [OpenTelemetry Collector](kb://06-reference-engineering-observability-sre-opentelemetry-collector)
