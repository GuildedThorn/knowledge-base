---
summary: "Stuxnet is the canonical public case of malware bridging Windows intrusion tradecraft into industrial-control sabotage."
status: active
tags: [security, threat-intel, ics, malware]
private: false
---

# Stuxnet

## Purpose

Stuxnet is the canonical public case of malware bridging Windows intrusion tradecraft into industrial-control sabotage.

## Key Ideas

- Stuxnet combined Windows propagation, rootkit behavior, signed drivers, and PLC-specific manipulation against industrial systems.
- Its significance is not one trick but the full kill chain: enterprise compromise, engineering-station access, controller logic tampering, and deception.
- Modern ICS defense still uses Stuxnet as a reference point for why IT and OT cannot be modeled independently.

## Defensive Use

- Separate engineering workstations from general enterprise networks and monitor removable media, project-file changes, and controller logic updates.
- Maintain signed/known-good baselines for PLC logic and watch for operator-view deception, not just host compromise.

## Sources

- MITRE ATT&CK - Stuxnet S0603 - https://attack.mitre.org/software/S0603/
- MITRE ATT&CK ICS - Rootkit T0851 - https://attack.mitre.org/techniques/T0851/
- Symantec - W32.Stuxnet Dossier - https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en

## Related

- [Threat Intel - Index](kb://11-security-threat-intel-threat-intel-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
