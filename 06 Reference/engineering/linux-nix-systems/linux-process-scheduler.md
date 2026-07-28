---
summary: "How the Linux kernel picks which runnable task runs next, from CFS virtual runtime to the EEVDF replacement scheduler."
status: active
tags: [reference, engineering, linux, scheduler, kernel, fairness]
private: false
---

# The Linux Process Scheduler (CFS and EEVDF)

## Purpose

How the Linux kernel picks which runnable task runs next, from CFS virtual runtime to the EEVDF replacement scheduler.

## CFS Design

- The Completely Fair Scheduler (default from 2.6.23) models an idealized "perfectly multitasking" CPU, tracking each task's `vruntime` (virtual runtime) and always picking the runnable task with the smallest `vruntime`.
- Runnable tasks are held in a per-CPU red-black tree keyed by `vruntime`, giving O(log n) enqueue/dequeue and O(1) leftmost-node selection.
- The `nice` value maps to a weight; `vruntime` advances inversely to weight, so lower-nice (higher-priority) tasks accumulate virtual time more slowly and get a larger CPU share.
- Per-CPU runqueues are kept balanced by periodic and idle load balancing across scheduling domains.

## EEVDF Transition

- EEVDF (Earliest Eligible Virtual Deadline First) replaced CFS as the default in kernel 6.6 (2023), addressing latency-sensitivity CFS handled only via heuristics.
- Each task has a lag (its accrued fair-share deficit or surplus); a task is "eligible" only when its lag is non-negative.
- Among eligible tasks, EEVDF runs the one with the earliest virtual deadline, computed from the task's requested time slice, giving explicit latency control.

## Operational Notes

- Real-time policies (SCHED_FIFO, SCHED_RR) sit above the fair class and always preempt normal tasks.
- The `sched_latency` and per-task slice tunables shape how finely CPU time is divided under contention.

## Sources

- Linux kernel docs - CFS Scheduler - https://docs.kernel.org/scheduler/sched-design-CFS.html
- Linux kernel docs - Scheduler index - https://docs.kernel.org/scheduler/index.html
- LWN - An EEVDF CPU scheduler for Linux - https://lwn.net/Articles/925371/

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
