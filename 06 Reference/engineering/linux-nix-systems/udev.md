---
summary: "The userspace device manager that populates /dev and applies rules as kernel devices appear and disappear."
status: active
tags: [reference, engineering, linux, udev, devices, hotplug]
private: false
---

# udev Device Management

## Purpose

The userspace device manager that populates /dev and applies rules as kernel devices appear and disappear.

## How It Works

- The kernel emits `uevents` over a netlink socket whenever devices are added, removed, or changed; `systemd-udevd` listens and processes them in userspace.
- udev creates and removes device nodes under `/dev`, sets their ownership and permissions, and can create symlinks and export properties for other services.
- Rules are read from `.rules` files under `/usr/lib/udev/rules.d` and `/etc/udev/rules.d`, processed in lexical order by filename across both directories.
- Each rule is a comma-separated list of match keys (`ACTION`, `SUBSYSTEM`, `ATTR{}`, `KERNEL`) and assignment keys (`NAME`, `SYMLINK`, `MODE`, `OWNER`, `RUN`).
- Device information for writing rules is inspected with `udevadm info` and events are traced live with `udevadm monitor`.

## Engineering Notes

- Persistent names decouple configuration from unstable kernel enumeration order; stable identifiers such as `ID_SERIAL`, `by-id`, and `by-path` symlinks are generated for disks and other hardware.
- Predictable network interface naming (e.g. `enp3s0`) is produced by udev's `net_id` builtin rather than the legacy `eth0` scheme.
- `RUN+=` can trigger helper programs, but long-running processes must be launched as systemd units, not directly from rules.
- `udevadm control --reload` reloads rules; `udevadm trigger` re-fires events to re-apply them to existing devices.

## Sources

- systemd docs - udev(7) - https://www.freedesktop.org/software/systemd/man/latest/udev.html
- man7 - udev(7) - https://man7.org/linux/man-pages/man7/udev.7.html

---
## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
