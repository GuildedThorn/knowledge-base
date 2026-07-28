---
summary: "Fault injection manipulates voltage, clock, electromagnetic, optical, or environmental conditions to disturb hardware execution or checks."
status: active
tags: [security, hardware, fault-injection, embedded]
private: false
---

# Fault Injection and Hardware Attacks

## Purpose

Fault injection manipulates voltage, clock, electromagnetic, optical, or environmental conditions to disturb hardware execution or checks.

## Key Ideas

- The goal is often to skip a security check, corrupt a comparison, bypass a boot decision, or leak a key through induced misbehavior.
- Attacks depend on physical access, timing precision, target repeatability, and observability of success.
- Secure elements and boot ROMs are common targets because one successful fault can undermine higher software layers.

## Defensive Use

- Use redundant checks, temporal/randomized execution, glitch detectors, secure elements, constant-time crypto, and tamper-aware design where the threat model justifies it.
- For assessments, record physical setup, timing windows, firmware version, and whether results are reproducible.

## Sources

- NewAE ChipWhisperer documentation - https://chipwhisperer.readthedocs.io/
- MITRE CWE - Fault Injection - https://cwe.mitre.org/data/definitions/1319.html
- Riscure - Fault injection resources - https://www.riscure.com/security-tools/inspector-fi/

## Related

- [Mobile & Hardware - Index](kb://11-security-mobile-hardware-mobile-hardware-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
