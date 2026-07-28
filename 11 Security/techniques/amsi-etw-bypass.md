---
summary: "AMSI and ETW bypasses attempt to blind Windows script and telemetry inspection by patching, disabling, or evading instrumentation paths."
status: active
tags: [security, technique, windows, evasion]
private: false
---

# AMSI and ETW Bypass

## Purpose

AMSI and ETW bypasses attempt to blind Windows script and telemetry inspection by patching, disabling, or evading instrumentation paths.

## Key Ideas

- AMSI gives security products visibility into script and content buffers before execution; ETW provides structured event telemetry from providers.
- Bypasses tend to target in-process patching, reflection, provider tampering, obfuscation, downgrade paths, or execution surfaces not instrumented the same way.
- A bypass should be modeled as telemetry impairment: the question is what independent sensor still sees the behavior.

## Defensive Use

- Monitor for suspicious memory modification of PowerShell/CLR/AMSI-related modules, constrained language downgrades, and script-block logging gaps.
- Layer command-line, module-load, process, EDR, and network signals so one disabled channel does not become an investigation blind spot.

## Sources

- Microsoft - Antimalware Scan Interface - https://learn.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal
- Microsoft - Event Tracing - https://learn.microsoft.com/en-us/windows/win32/etw/about-event-tracing
- MITRE ATT&CK - Impair Defenses T1562 - https://attack.mitre.org/techniques/T1562/

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
