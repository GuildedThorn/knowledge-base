---
summary: "Sliver is an open-source cross-platform C2 framework whose legitimate red-team design is increasingly mirrored in adversary tradecraft."
status: active
tags: [security, c2, post-exploitation, sliver]
private: false
---

# Sliver C2 Framework

## Purpose

Sliver is an open-source cross-platform C2 framework whose legitimate red-team design is increasingly mirrored in adversary tradecraft.

## Key Ideas

- Sliver supports multiple transport options including HTTP(S), DNS, mTLS, and WireGuard-like workflows.
- Its Go implementation and operator ecosystem make binary traits and network profiles different from older Beacon-centric detections.
- Open-source C2 frameworks compress the time between public capability and criminal abuse.

## Defensive Use

- Hunt for unusual Go implants, rare TLS/JA3 patterns, DNS C2 behavior, suspicious service/process names, and post-exploitation modules.
- Validate detections against authorized red-team infrastructure so internal exercises do not create unmanaged noise.

## Sources

- MITRE ATT&CK - Sliver S0633 - https://attack.mitre.org/software/S0633/
- Sliver documentation - https://sliver.sh/docs
- Bishop Fox - Sliver project - https://github.com/BishopFox/sliver

## Related

- [C2 & Post-Ex - Index](kb://11-security-c2-postex-c2-postex-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
