---
summary: "LockBit is a ransomware-as-a-service ecosystem whose affiliates vary widely but converge on credential abuse, data theft, and fast encryption."
status: active
tags: [security, threat-intel, ransomware, lockbit]
private: false
---

# LockBit Ransomware

## Purpose

LockBit is a ransomware-as-a-service ecosystem whose affiliates vary widely but converge on credential abuse, data theft, and fast encryption.

## Key Ideas

- LockBit is affiliate-driven: intrusion paths and tooling differ by operator, so defensive coverage must target behaviors instead of fixed IOCs.
- Frequently observed themes include VPN/RDP abuse, public-facing application exploitation, PowerShell/batch discovery, credential dumping, exfiltration, and EDR tampering.
- The business model combines encryption with leak-site extortion and secondary pressure on victims.

## Defensive Use

- Map controls to CISA's ATT&CK tables: valid accounts, external services, credential dumping, event-log clearing, exfil staging, and defense impairment.
- Harden remote access, enforce MFA, restrict local admin sprawl, monitor backup deletion, and test restore paths before an incident.

## Sources

- CISA AA23-165A - Understanding Ransomware Threat Actors: LockBit - https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- MITRE ATT&CK - LockBit 2.0 S1199 - https://attack.mitre.org/software/S1199/
- CISA StopRansomware Guide - https://www.cisa.gov/stopransomware/ransomware-guide

## Related

- [Threat Intel - Index](kb://11-security-threat-intel-threat-intel-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
