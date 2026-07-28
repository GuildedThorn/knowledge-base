---
summary: "An unprivileged, stackable LSM letting a process sandbox itself by restricting filesystem and network access."
status: active
tags: [reference, engineering, linux, landlock, sandbox, lsm]
private: false
---

# Landlock LSM

## Purpose

An unprivileged, stackable LSM letting a process sandbox itself by restricting filesystem and network access.

## Core Model

- A process builds a *ruleset* declaring the access rights it wants to allow, then adds rules and enforces the ruleset on itself and its children.
- Requires no root: any process can restrict itself, and restrictions are inherited and cannot be lifted, only further tightened (monotonic).
- Rulesets are stacked: multiple independent policies apply cumulatively, so a nested sandbox can only remove access, never regain it.
- Filesystem rights are path-based and cover actions such as read, write, execute, create, remove, and directory reparenting; recent ABIs add TCP bind/connect network rules.

## How It Works

- Three syscalls drive it: `landlock_create_ruleset` (defines handled access rights), `landlock_add_rule` (attaches a rule to a path fd or port), and `landlock_restrict_self` (enforces it, after `prctl(PR_SET_NO_NEW_PRIVS)`).
- ABI is versioned; query the supported version with `landlock_create_ruleset(NULL, 0, LANDLOCK_CREATE_RULESET_VERSION)`.
- Best-effort enforcement is idiomatic: mask requested rights down to what the running kernel supports so the program degrades gracefully on older kernels rather than failing.

## Sources

- Landlock official site - https://landlock.io/
- Linux kernel docs - Landlock - https://docs.kernel.org/userspace-api/landlock.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
