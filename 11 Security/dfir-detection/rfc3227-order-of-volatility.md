---
summary: "RFC 3227 sets guidelines for collecting and archiving digital evidence prioritized by data volatility."
status: active
tags: [security, dfir, rfc3227, evidence, acquisition]
private: false
---

# Evidence Collection and Order of Volatility (RFC 3227)

## Purpose

RFC 3227 sets guidelines for collecting and archiving digital evidence prioritized by data volatility.

## Order of Volatility

- Evidence must be captured most-volatile first, because volatile sources decay or vanish as the system runs or powers off.
- The canonical hierarchy: CPU registers and cache; routing table, ARP cache, process table, kernel stats and memory; temporary filesystems; disk; remote logging and monitoring data; physical config and network topology; archival media.
- Capturing memory and network state before touching disk preserves live artifacts (running malware, encryption keys, open connections).

## Collection Procedure and Chain of Custody

- Collect from a trusted, documented toolset; minimize changes to the target and record everything you do and its timestamps.
- Chain of custody must log where, when, and by whom each item was discovered, collected, handled, and stored.
- Keep detailed notes with times; note clock drift between the system clock and a reference (UTC) source.
- Avoid shutting down before collection and avoid running programs that alter access times unless unavoidable.

## Archiving and Integrity

- Compute and record cryptographic hashes of collected images so integrity can be later verified.
- Store evidence on read-only or write-once media where possible and control access to preserve admissibility.
- NIST SP 800-86 complements RFC 3227 with a fuller forensic process: collection, examination, analysis, and reporting.

## Sources

- RFC 3227 - https://www.rfc-editor.org/rfc/rfc3227
- NIST SP 800-86 - https://csrc.nist.gov/pubs/sp/800/86/final

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
