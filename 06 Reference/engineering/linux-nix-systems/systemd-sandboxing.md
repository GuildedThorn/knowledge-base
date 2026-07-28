---
summary: "The security directives in systemd.exec that confine services using namespaces, seccomp, and capability limits."
status: active
tags: [reference, engineering, linux, systemd, hardening, sandbox]
private: false
---

# systemd Service Sandboxing

## Purpose

The security directives in systemd.exec that confine services using namespaces, seccomp, and capability limits.

## Core Model

- systemd exposes per-unit sandboxing directives in the `[Service]` section, backed by kernel isolation primitives.
- Filesystem confinement uses mount namespaces: `ProtectSystem=` remounts system paths read-only, `ProtectHome=` hides home directories.
- `PrivateTmp=`, `PrivateDevices=`, and `PrivateNetwork=` give the service isolated tmp, a minimal `/dev`, and a network namespace.
- Capability limits (`CapabilityBoundingSet=`, `AmbientCapabilities=`) drop privileges the service never needs.
- `SystemCallFilter=` applies a seccomp allow/deny list to restrict the syscalls the service may invoke.

## How It Works

- Each directive maps to a kernel mechanism (namespaces, seccomp-bpf, capability bounding sets, no-new-privileges).
- Directives compose: a hardened unit typically stacks filesystem, network, syscall, and capability restrictions together.
- `SystemCallFilter=@system-service` plus `SystemCallArchitectures=native` is a common baseline that blocks obscure and cross-arch calls.
- Restrictions are enforced at exec time on the service's processes and their children.

## Operational Notes

- `systemd-analyze security <unit>` scores a unit's exposure and lists which hardening directives are unset.
- Over-tight filters cause opaque failures (EPERM, killed by SIGSYS); test incrementally and check the journal.
- Sandboxing is defense-in-depth, not a substitute for least-privilege service design and dependency minimization.

## Sources

- systemd docs - systemd.exec(5) - https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html
- systemd docs - systemd-analyze(1) - https://www.freedesktop.org/software/systemd/man/latest/systemd-analyze.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
