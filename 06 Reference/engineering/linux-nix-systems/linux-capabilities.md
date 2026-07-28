---
summary: "The partitioning of root privilege into distinct capabilities carried in per-thread and file capability sets."
status: active
tags: [reference, engineering, linux, capabilities, privilege, security]
private: false
---

# Linux Capabilities

## Purpose

The partitioning of root privilege into distinct capabilities carried in per-thread and file capability sets.

## Capability Sets

- Privilege is split into ~40 units (e.g. `CAP_NET_BIND_SERVICE`, `CAP_NET_ADMIN`, `CAP_SYS_ADMIN`, `CAP_DAC_OVERRIDE`).
- Each thread holds five sets: **permitted** (upper bound of usable caps), **effective** (currently active for permission checks), **inheritable** (preserved across exec into a file's inheritable set), **bounding** (a mask limiting what can ever be gained), and **ambient** (inheritable caps preserved across a non-privileged exec).
- A capability must be in the effective set for a check to pass; a thread may raise permitted caps into effective at will.

## File Capabilities

- Executables carry capabilities in the `security.capability` extended attribute, avoiding setuid-root binaries.
- File sets are permitted and inheritable plus an effective bit; a set-effective bit makes granted caps immediately active on exec.
- File capabilities allow a program to gain only the specific privileges it needs (e.g. `CAP_NET_RAW` for `ping`).

## Transitions Across exec

- New permitted = (file-permitted) OR (file-inheritable AND thread-inheritable), all masked by the bounding set, plus ambient.
- Ambient capabilities let unprivileged processes pass caps across exec of a file with no file caps.
- `CAP_SETPCAP` governs modifying the bounding set and granting inheritable caps; `SECBIT_NOROOT` disables the legacy "root gets all caps" behavior.

## Sources

- man7 - capabilities(7) - https://man7.org/linux/man-pages/man7/capabilities.7.html
- man7 - execve(2) - https://man7.org/linux/man-pages/man2/execve.2.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
