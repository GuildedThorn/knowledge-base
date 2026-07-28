---
summary: "In-kernel eBPF programs that safely instrument syscalls, network, and functions to produce low-overhead observability data."
status: active
tags: [reference, engineering, sre, ebpf, kernel, tracing]
private: false
---

# eBPF Observability

## Purpose

In-kernel eBPF programs that safely instrument syscalls, network, and functions to produce low-overhead observability data.

## BPF Programs and Verifier

- eBPF programs are compiled to a compact bytecode, loaded via the `bpf()` syscall, and JIT-compiled to native code in the kernel.
- The in-kernel verifier statically checks each program for safety: bounded loops, valid memory access, and guaranteed termination before it runs.
- Programs communicate with user space through maps (hash, array, ring buffer) that hold aggregated counts, histograms, or events.
- Running in-kernel avoids per-event context switches, keeping overhead low even at high event rates.

## Attachment Points

- kprobes/kretprobes hook arbitrary kernel functions; uprobes/uretprobes hook user-space functions.
- Tracepoints are stable, kernel-defined hooks (syscalls, scheduler, block I/O) preferred over kprobes for durability.
- USDT probes expose statically-defined tracepoints in user applications; XDP and tc hooks instrument the network path.

## Tooling

- BCC provides a Python/C framework and a large collection of ready-made tracing tools.
- bpftrace offers a concise, awk-like high-level language for ad-hoc one-liners and short scripts.
- Higher-level platforms (Cilium, Pixie, Parca) build continuous profiling and network observability on the same primitives.

## Sources

- eBPF Introduction - https://ebpf.io/what-is-ebpf/
- Kernel BPF Documentation - https://docs.kernel.org/bpf/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
