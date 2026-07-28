---
summary: "TrickBot and QakBot are modular banking-trojan loader ecosystems that evolved into ransomware delivery infrastructure."
status: active
tags: [security, threat-intel, malware, loader]
private: false
---

# TrickBot and QakBot
[[solarwinds-sunburst]]
## Purpose

TrickBot and QakBot are modular banking-trojan loader ecosystems that evolved into ransomware delivery infrastructure.

## Key Ideas

- Both families began around financial theft and matured into modular access brokers for follow-on payloads.
- Common capabilities include web injects, credential theft, email/thread harvesting, lateral movement support, and encrypted C2.
- Operationally, treat them as high-risk precursors to hands-on-keyboard intrusion and ransomware deployment.

## Defensive Use

- Prioritize detections for Office/script parent-child chains, suspicious service creation, encoded PowerShell, and anomalous outbound C2.
- Contain rapidly: isolate infected hosts, reset exposed credentials, and hunt for second-stage tooling rather than assuming the loader is the whole incident.

## Sources

- MITRE ATT&CK - TrickBot S0266 - https://attack.mitre.org/software/S0266/
- MITRE ATT&CK - QakBot S0650 - https://attack.mitre.org/software/S0650/
- The DFIR Report - QBot infection leading to ransomware - https://thedfirreport.com/

## Related

- [Threat Intel - Index](kb://11-security-threat-intel-threat-intel-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
