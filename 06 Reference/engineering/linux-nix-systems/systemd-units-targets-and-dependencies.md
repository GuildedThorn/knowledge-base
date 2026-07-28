---
summary: "systemd models services, mounts, sockets, timers, devices, and boot milestones as units with explicit dependencies and ordering."
status: active
tags: [reference, engineering, systemd, linux]
private: false
---

# systemd Units, Targets, and Dependencies

## Purpose

systemd models services, mounts, sockets, timers, devices, and boot milestones as units with explicit dependencies and ordering.

## Core Model

- Unit dependencies such as Requires, Wants, BindsTo, PartOf, Before, and After express requirement and ordering relationships.
- Targets group units into boot or operational states.
- Service Type, ExecStart, Restart, User, WorkingDirectory, environment, sandboxing, and resource controls shape runtime behavior.

## Engineering Notes

- Separate requirement from ordering: `Wants=` does not imply `After=`.
- Prefer systemd sandboxing and resource controls over custom wrapper scripts.
- Use `systemd-analyze critical-chain`, `journalctl -u`, and `systemctl show` to debug startup behavior.

## Sources

- systemd.unit manual - https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html
- systemd.service manual - https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html
- systemd.special manual - https://www.freedesktop.org/software/systemd/man/latest/systemd.special.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
