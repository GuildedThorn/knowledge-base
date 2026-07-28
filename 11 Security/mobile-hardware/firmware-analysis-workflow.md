---
summary: "Firmware analysis extracts, identifies, unpacks, and inspects device images for filesystems, secrets, services, vulnerabilities, and update trust."
status: active
tags: [security, hardware, firmware, reversing]
private: false
---

# Firmware Analysis Workflow

## Purpose

Firmware analysis extracts, identifies, unpacks, and inspects device images for filesystems, secrets, services, vulnerabilities, and update trust.

## Key Ideas

- Firmware may contain bootloaders, kernels, filesystems, web interfaces, default credentials, certificates, update scripts, and vendor binaries.
- Workflow starts with acquisition and hash preservation, then binwalk-like carving, filesystem mount/extract, string/config review, and binary analysis.
- Update mechanism security matters as much as found CVEs: signing, rollback, transport, and recovery paths define persistence risk.

## Defensive Use

- Never run extracted services on a trusted network; emulate or isolate components deliberately.
- Record firmware version, device model, extraction method, hashes, and any secrets so remediation can track affected releases.

## Sources

- MITRE ATT&CK - System Firmware T1542.001 - https://attack.mitre.org/techniques/T1542/001/
- NSA - Validate Integrity of Hardware and Software - https://www.nsa.gov/Cybersecurity/Cybersecurity-Advisories-Guidance/
- OWASP Firmware Security Testing Methodology - https://scriptingxss.gitbook.io/firmware-security-testing-methodology/

## Related

- [Mobile & Hardware - Index](kb://11-security-mobile-hardware-mobile-hardware-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
