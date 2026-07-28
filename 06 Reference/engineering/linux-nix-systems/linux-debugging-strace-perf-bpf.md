---
summary: "Linux production debugging often starts with syscalls, scheduler/CPU profiles, kernel events, and dynamic tracing."
status: active
tags: [reference, engineering, linux, debugging]
private: false
---

# Linux Debugging with strace, perf, and eBPF

## Purpose

Linux production debugging often starts with syscalls, scheduler/CPU profiles, kernel events, and dynamic tracing.

## Core Model

- strace shows syscall-level behavior and errors.
- perf samples CPU, call stacks, scheduler events, and hardware counters.
- eBPF attaches safe programs to kernel/user probes, tracepoints, sockets, and performance events.

## Engineering Notes

- Use the lowest-impact tool that answers the current question; tracing can change timing.
- Capture command, kernel version, symbols, and workload conditions with every profile.
- For eBPF, verify verifier limits, privileges, kernel support, and production safety.

## Sources

- strace project - https://strace.io/
- Linux perf wiki - https://perf.wiki.kernel.org/index.php/Main_Page
- eBPF documentation - https://ebpf.io/what-is-ebpf/

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
