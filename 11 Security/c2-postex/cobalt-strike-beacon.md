---
summary: "Cobalt Strike Beacon is a commercial adversary-emulation implant widely abused by intrusion operators for post-exploitation."
status: active
tags: [security, c2, post-exploitation, cobalt-strike]
private: false
---

# Cobalt Strike Beacon

## Purpose

Cobalt Strike Beacon is a commercial adversary-emulation implant widely abused by intrusion operators for post-exploitation.

## Key Ideas

- Beacon supports HTTP(S), DNS, SMB/named-pipe, TCP, and other operational modes through configurable profiles.
- Malleable C2 lets operators alter network indicators, so default-profile IOCs age quickly.
- Post-exploitation capability breadth makes Beacon behavior show up across discovery, credential access, lateral movement, exfiltration, and evasion.

## Defensive Use

- Detect behavior and protocol anomalies: sleep/jitter patterns, suspicious named pipes, injected Beacon memory, rare parent-child chains, and C2 profile mistakes.
- Map observed activity to ATT&CK, then hunt adjacent post-exploitation actions instead of stopping at the Beacon alert.

## Sources

- MITRE ATT&CK - Cobalt Strike S0154 - https://attack.mitre.org/software/S0154/
- Cobalt Strike - Malleable C2 - https://www.cobaltstrike.com/product/features/malleable-c2
- CISA - Cobalt Strike threat context - https://www.cisa.gov/news-events/cybersecurity-advisories

## Related

- [C2 & Post-Ex - Index](kb://11-security-c2-postex-c2-postex-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
