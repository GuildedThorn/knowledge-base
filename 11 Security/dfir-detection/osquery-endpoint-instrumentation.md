---
summary: "osquery exposes operating system state as a SQL-queryable relational schema for hunting and fleet visibility."
status: active
tags: [security, dfir, osquery, endpoint, sql]
private: false
---

# osquery Endpoint Instrumentation

## Purpose

osquery exposes operating system state as a SQL-queryable relational schema for hunting and fleet visibility.

## Virtual-Table Schema

- osquery represents the OS as SQLite virtual tables: `processes`, `listening_ports`, `users`, `kernel_modules`, and hundreds more.
- Analysts query live state with standard SQL, joining tables to answer questions like which process owns a listening socket.
- Cross-platform coverage spans Linux, macOS, and Windows, with some tables OS-specific.
- `osqueryi` gives an interactive shell; `osqueryd` runs as a scheduling daemon for continuous monitoring.

## Scheduled Packs and Diffs

- Query packs bundle scheduled queries that `osqueryd` runs at set intervals across a fleet.
- Results log in differential mode by default, emitting only added/removed rows since the last run to cut noise and volume.
- Output streams to files or a logger plugin, feeding SIEMs and management platforms like Fleet or Kolide.
- Snapshot mode emits full result sets when point-in-time state is needed instead of diffs.

## File Integrity and Events

- Evented tables (`process_events`, `socket_events`, `file_events`) capture activity over time via audit/BPF/ETW backends.
- File integrity monitoring watches configured paths and records checksum changes in `file_events`.
- Requires enabling the corresponding publishers (e.g. Linux Audit or BPF) in the daemon configuration.

## Sources

- osquery - https://osquery.io/
- osquery Documentation - https://osquery.readthedocs.io/
- osquery GitHub - https://github.com/osquery/osquery

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
