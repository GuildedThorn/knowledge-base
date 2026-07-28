---
summary: "Lateral movement uses credentials, remote services, admin tools, and trust relationships to expand access after initial compromise."
status: active
tags: [security, post-exploitation, lateral-movement, attack]
private: false
---

# Lateral Movement Patterns

## Purpose

Lateral movement uses credentials, remote services, admin tools, and trust relationships to expand access after initial compromise.

## Key Ideas

- Common paths include SMB/admin shares, RDP, WinRM, WMI, PsExec-like service creation, SSH, cloud role assumption, and SaaS delegated access.
- The movement method often reveals what credential material the actor has: password, hash, ticket, token, key, or role.
- Defenders should model movement across identity, endpoint, network, and cloud control planes.

## Defensive Use

- Correlate new logons, remote service creation, file copy, administrative protocol use, and source/destination role anomalies.
- Use tiering, firewall segmentation, just-in-time admin, and credential isolation to reduce where stolen credentials work.

## Sources

- MITRE ATT&CK - Lateral Movement TA0008 - https://attack.mitre.org/tactics/TA0008/
- MITRE ATT&CK - Remote Services T1021 - https://attack.mitre.org/techniques/T1021/
- Microsoft - Securing privileged access - https://learn.microsoft.com/en-us/security/privileged-access-workstations/privileged-access-access-model

## Related

- [C2 & Post-Ex - Index](kb://11-security-c2-postex-c2-postex-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
