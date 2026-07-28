---
summary: "Zeek observes network traffic and produces rich structured logs and scriptable events for hunting and forensics."
status: active
tags: [security, dfir, zeek, network, monitoring]
private: false
---

# Zeek Network Security Monitor

## Purpose

Zeek observes network traffic and produces rich structured logs and scriptable events for hunting and forensics.

## Event-Driven Architecture

- Zeek (formerly Bro) passively parses traffic into a stream of high-level events rather than matching packet signatures.
- An event engine handles protocol analysis; a policy-script interpreter reacts to events with user-defined logic.
- It records what happened on the network as metadata, giving analysts context rather than raw alerts alone.
- Clusters distribute load across worker nodes with a manager and proxy for high-throughput links.

## Core Logs

- `conn.log` is the connection summary spine, keyed by a `uid` that ties records across every other log.
- Protocol logs include `dns.log`, `http.log`, `ssl.log`, `x509.log`, `smtp.log`, and `files.log`.
- `notice.log` records policy-defined observations of interest; `weird.log` captures protocol anomalies.
- Logs are structured TSV by default and easily shipped to a SIEM or converted to JSON.

## Scripting Language

- Zeek's Turing-complete scripting language defines new detections by handling events and maintaining state.
- Built-in frameworks cover intelligence matching, notices, file extraction, and summary statistics (`sumstats`).
- The community package manager (`zkg`) distributes reusable detection scripts and integrations.

## Sources

- Zeek - https://zeek.org/
- Zeek Documentation - https://docs.zeek.org/

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
