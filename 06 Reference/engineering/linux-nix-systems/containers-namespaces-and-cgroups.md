---
summary: "Linux containers package processes with namespace isolation and cgroup resource control rather than full machine virtualization."
status: active
tags: [reference, engineering, linux, containers]
private: false
---

# Containers, Namespaces, and cgroups

## Purpose

Linux containers package processes with namespace isolation and cgroup resource control rather than full machine virtualization.

## Core Model

- Namespaces isolate views of PIDs, mounts, users, network, IPC, UTS, and cgroups.
- cgroups limit and account resources such as CPU, memory, IO, and process count.
- Container images layer filesystems and metadata; runtimes configure namespaces, mounts, capabilities, and seccomp/LSM policy.

## Engineering Notes

- Do not equate container with security boundary unless hardening is explicit.
- Drop capabilities, avoid privileged mode, restrict host mounts, and set resource limits.
- Understand user namespaces and rootless modes for developer machines and multi-tenant hosts.

## Sources

- Linux namespaces overview - https://man7.org/linux/man-pages/man7/namespaces.7.html
- Linux cgroup v2 docs - https://docs.kernel.org/admin-guide/cgroup-v2.html
- OCI runtime spec - https://github.com/opencontainers/runtime-spec

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
