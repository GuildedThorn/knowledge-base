---
summary: "The systemd structured logging service that collects, indexes, and stores journal records from the whole system."
status: active
tags: [reference, engineering, linux, journald, logging, systemd]
private: false
---

# systemd-journald

## Purpose

The systemd structured logging service that collects, indexes, and stores journal records from the whole system.

## Core Model

- journald collects log data from kernel messages, service stdout/stderr, syslog, and the native journal API.
- Records are structured: each entry is a set of key-value fields (e.g. `_SYSTEMD_UNIT`, `PRIORITY`, `MESSAGE`), not just a text line.
- Trusted fields prefixed with an underscore are added by journald itself and cannot be forged by the sender.
- The journal is indexed, so queries can filter on any field without scanning full log text.
- journalctl is the client for reading, filtering, and following the journal.

## How It Works

- Storage mode (`Storage=`) selects volatile (`/run`, lost on reboot), persistent (`/var/log/journal`), or auto.
- Retention is bounded by size and time limits; journald rotates and vacuums old entries against those caps.
- Filtering supports unit (`-u`), priority (`-p`), boot (`-b`), time ranges, and arbitrary `FIELD=value` matches.
- Records can be forwarded (syslog, console, kmsg) or shipped upstream via journal-remote/upload.

## Operational Notes

- Persistent storage requires `/var/log/journal` to exist; otherwise logs vanish on reboot.
- Rate limiting (`RateLimitInterval`/`Burst`) can silently drop bursty log output; tune it for chatty services.
- `journalctl --verify` checks integrity; forward-secure sealing (FSS) can detect tampering on persistent journals.

## Sources

- systemd docs - systemd-journald.service(8) - https://www.freedesktop.org/software/systemd/man/latest/systemd-journald.service.html
- systemd docs - journalctl(1) - https://www.freedesktop.org/software/systemd/man/latest/journalctl.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
