---
summary: "Linux operating-system concepts, systemd, containers, Nix language, NixOS modules, flakes, and reproducibility notes."
status: active
tags: [reference, engineering, linux, nix, systems, index]
private: false
---

# Linux, Nix, and Systems - Index

## Purpose

Linux operating-system concepts, systemd, containers, Nix language, NixOS modules, flakes, and reproducibility notes.

## Notes

- [Containers, Namespaces, and cgroups](kb://06-reference-engineering-linux-nix-systems-containers-namespaces-and-cgroups) - Linux containers package processes with namespace isolation and cgroup resource control rather than full machine virtualization.
- [CPU Cache, Branch Prediction, and NUMA](kb://06-reference-engineering-linux-nix-systems-cpu-cache-branch-prediction-and-numa) - CPU performance depends heavily on cache locality, branch predictability, memory ordering, vectorization, and NUMA placement.
- [eBPF Programs, Maps, and Verifier](kb://06-reference-engineering-linux-nix-systems-ebpf-programs-maps-and-verifier) - eBPF runs verified programs at kernel hook points using maps, helpers, program types, and verifier-enforced safety constraints.
- [Flakes, Lockfiles, and Inputs](kb://06-reference-engineering-linux-nix-systems-flakes-lockfiles-and-inputs) - Nix flakes package inputs, outputs, and lockfiles into a reproducible interface for packages, apps, dev shells, and NixOS systems.
- [Home Manager and User Environments](kb://06-reference-engineering-linux-nix-systems-home-manager-and-user-environments) - Home Manager manages user-level packages, dotfiles, services, and application config with Nix modules.
- [io_uring Linux Async I/O](kb://06-reference-engineering-linux-nix-systems-io-uring-linux-async-io) - io_uring is Linux's shared-ring asynchronous I/O interface for submitting operations and receiving completions with fewer syscall transitions.
- [Kubernetes Pod Security Standards](kb://06-reference-engineering-linux-nix-systems-kubernetes-pod-security-standards) - Kubernetes Pod Security Standards define Privileged, Baseline, and Restricted profiles for controlling pod-level privilege and isolation.
- [Linux Debugging with strace, perf, and eBPF](kb://06-reference-engineering-linux-nix-systems-linux-debugging-strace-perf-bpf) - Linux production debugging often starts with syscalls, scheduler/CPU profiles, kernel events, and dynamic tracing.
- [Linux Filesystems, VFS, and Permissions](kb://06-reference-engineering-linux-nix-systems-linux-filesystems-vfs-and-permissions) - Linux filesystems expose persistent and virtual resources through VFS objects, permissions, ownership, mounts, and special file types.
- [Linux Memory Management](kb://06-reference-engineering-linux-nix-systems-linux-memory-management) - Linux memory management combines virtual memory, page tables, demand paging, reclaim, swapping, NUMA, huge pages, and cgroup limits.
- [Linux Processes, Signals, and exec](kb://06-reference-engineering-linux-nix-systems-linux-processes-signals-and-exec) - Linux process control centers on fork/clone, exec, wait, signals, file descriptors, and exit status.
- [Linux Scheduler, cgroups, and Priority](kb://06-reference-engineering-linux-nix-systems-linux-scheduler-cgroups-and-priority) - Linux scheduling uses policies, priorities, CPU affinity, cgroups, and pressure signals to allocate CPU under contention.
- [Nix Language and Derivations](kb://06-reference-engineering-linux-nix-systems-nix-language-and-derivations) - The Nix language builds lazy attribute-set expressions that evaluate to derivations, which describe reproducible build actions.
- [NixOS Modules, Options, and Evaluation](kb://06-reference-engineering-linux-nix-systems-nixos-modules-options-and-evaluation) - NixOS modules merge option declarations and definitions into a system configuration evaluated into activation and service artifacts.
- [Reproducible Builds and Binary Caches](kb://06-reference-engineering-linux-nix-systems-reproducible-builds-and-binary-caches) - Reproducible builds and binary caches let teams verify, share, and deploy build outputs with stronger supply-chain confidence.
- [systemd Timers, journald, and Service Observability](kb://06-reference-engineering-linux-nix-systems-systemd-timers-journald-and-observability) - systemd timers schedule units, while journald captures structured logs and service metadata for local operational visibility.
- [systemd Units, Targets, and Dependencies](kb://06-reference-engineering-linux-nix-systems-systemd-units-targets-and-dependencies) - systemd models services, mounts, sockets, timers, devices, and boot milestones as units with explicit dependencies and ordering.

## Related

- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Engineering Source Corpus](kb://06-reference-engineering-engineering-source-corpus)
- [Reference Map](kb://01-maps-reference-map)
