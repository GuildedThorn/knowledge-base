---
summary: "DLL sideloading abuses trusted executables and Windows library search behavior to run attacker-controlled DLL code."
status: active
tags: [security, technique, dll, evasion]
private: false
---

# DLL Sideloading and Search Order Hijacking

## Purpose

DLL sideloading abuses trusted executables and Windows library search behavior to run attacker-controlled DLL code.

## Key Ideas

- Sideloading places a malicious DLL where a legitimate executable will load it by name or search order.
- The technique often gives malicious code the reputation, path, or signature context of a trusted application.
- Search-order hijacking and phantom DLL hijacking are related variants under ATT&CK Hijack Execution Flow.

## Defensive Use

- Baseline DLL load paths for trusted applications and alert on DLLs loaded from user-writable, temp, download, or unexpected working directories.
- Prefer explicit library paths, safe DLL search settings, application allowlisting, and package integrity checks.

## Sources

- MITRE ATT&CK - Hijack Execution Flow: DLL T1574.001 - https://attack.mitre.org/techniques/T1574/001/
- Microsoft - Dynamic-link library search order - https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order
- Microsoft ASR rules reference - https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
