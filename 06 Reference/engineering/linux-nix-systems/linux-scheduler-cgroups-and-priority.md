---
summary: "Linux scheduling uses policies, priorities, CPU affinity, cgroups, and pressure signals to allocate CPU under contention."
status: active
tags: [reference, engineering, linux, scheduler]
private: false
---

# Linux Scheduler, cgroups, and Priority

## Purpose

Linux scheduling uses policies, priorities, CPU affinity, cgroups, and pressure signals to allocate CPU under contention.

## Core Model

- CFS targets fair CPU time among runnable tasks using virtual runtime.
- Real-time scheduling policies can starve normal work if misconfigured.
- cgroup v2 controls CPU, memory, IO, pids, and delegation for services and containers.

## Engineering Notes

- Use systemd/cgroup limits for services instead of ad-hoc nice/ulimit alone.
- Monitor CPU saturation with run queue, pressure stall information, throttling, and latency, not only utilization.
- Be careful with real-time priorities on desktops and audio/VR systems; one runaway task can degrade the whole machine.

## Sources

- Linux kernel scheduler docs - https://docs.kernel.org/scheduler/
- Linux cgroup v2 docs - https://docs.kernel.org/admin-guide/cgroup-v2.html
- systemd.resource-control - https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
