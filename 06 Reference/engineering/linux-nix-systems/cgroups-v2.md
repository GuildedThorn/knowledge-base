---
summary: "The unified cgroup v2 hierarchy for accounting and limiting CPU, memory, and I/O across process groups."
status: active
tags: [reference, engineering, linux, cgroups, resource-limits, kernel]
private: false
---

# Control Groups v2 (cgroups)

## Purpose

The unified cgroup v2 hierarchy for accounting and limiting CPU, memory, and I/O across process groups.

## Core Model

- cgroups partition processes into a hierarchical tree; controllers attached to that tree account for and constrain resource use per subtree.
- Unlike v1's multiple per-controller hierarchies, v2 uses a single unified hierarchy so every controller shares the same tree, removing v1's ambiguity when a process sat in different places per resource.
- Each cgroup exposes a `cgroup.controllers` (available) and `cgroup.subtree_control` (enabled for children) interface; controllers propagate down the tree.

## Constraints and Rules

- The "no internal process" rule: a non-root cgroup with controllers enabled for its children may not itself contain processes, keeping resource distribution well-defined between competing subtrees and leaf tasks.
- Delegation lets an unprivileged owner manage a subtree by granting write access to its `cgroup.procs` and `cgroup.subtree_control`, enabling rootless containers and systemd user slices.
- Membership is by process, and threads of a process normally share a cgroup (with an opt-in threaded mode for thread-granular control).

## Operational Notes

- Key knobs: `cpu.max` (quota/period), `cpu.weight` (proportional share), `memory.max`/`memory.high`, and `io.max`/`io.weight`.
- Pressure Stall Information (PSI) files (`cpu.pressure`, `memory.pressure`, `io.pressure`) report time tasks stalled on each resource, useful for detecting contention.
- systemd is the dominant cgroup manager on modern distros, mapping units to slices and scopes.

## Sources

- Linux kernel docs - Control Group v2 - https://docs.kernel.org/admin-guide/cgroup-v2.html
- man7 - cgroups(7) - https://man7.org/linux/man-pages/man7/cgroups.7.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
