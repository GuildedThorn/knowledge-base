---
summary: "Persistence techniques preserve adversary access across reboots, credential changes, remediation attempts, and service restarts."
status: active
tags: [security, technique, persistence, attack]
private: false
---

# Persistence Patterns

## Purpose

Persistence techniques preserve adversary access across reboots, credential changes, remediation attempts, and service restarts.

## Key Ideas

- ATT&CK persistence spans accounts, autostart extensibility points, services, scheduled tasks, browser extensions, images, firmware, and cloud identities.
- Persistence often overlaps privilege escalation and defense evasion: the same change can restart malware and hide it.
- Cloud and SaaS persistence commonly lives in OAuth apps, service principals, federation settings, API tokens, and roles rather than binaries.

## Defensive Use

- Inventory autostart locations, services, scheduled jobs, identity-provider apps, privileged role assignments, and firmware/boot configuration.
- Detect new or rare persistence objects, then validate business owner and change ticket rather than accepting object existence as proof of legitimacy.

## Sources

- MITRE ATT&CK - Persistence TA0003 - https://attack.mitre.org/tactics/TA0003/
- MITRE ATT&CK - Account Manipulation T1098 - https://attack.mitre.org/techniques/T1098/
- MITRE ATT&CK - Pre-OS Boot T1542 - https://attack.mitre.org/techniques/T1542/

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
