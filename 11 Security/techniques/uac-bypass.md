---
summary: "Elevating from medium to high integrity without a prompt by abusing auto-elevating binaries and hijacked registry paths."
status: active
tags: [security, techniques, uac, privilege-escalation, defense-evasion]
private: false
---

# User Account Control Bypass

## Purpose

Elevating from medium to high integrity without a prompt by abusing auto-elevating binaries and hijacked registry paths.

## Core Model

- UAC runs admin users' processes at medium integrity by default; elevation to high integrity normally requires a consent prompt.
- Certain signed Microsoft binaries carry `autoElevate=true` in their manifest and elevate silently when launched from a trusted directory, without prompting.
- If such a binary reads a writable per-user registry key or loads a hijackable DLL during startup, a medium-integrity process can plant a payload that the elevated binary then executes at high integrity.

## Common Vectors

- `fodhelper.exe` and `computerdefaults.exe` query `HKCU\Software\Classes\ms-settings\Shell\Open\command`, a user-writable key with no elevation needed to modify.
- `eventvwr.exe` historically resolved `HKCU\Software\Classes\mscfile\shell\open\command`, hijacking the MMC launch.
- UACME catalogs dozens of these method variants across Windows versions for research and testing.

## Mitigation

- Set UAC to "Always notify," which forces a secure-desktop prompt even for auto-elevating binaries.
- Removing users from the local Administrators group eliminates the silent-elevation path entirely.
- Monitor for medium-integrity processes writing to `ms-settings`/`mscfile` command keys followed by an auto-elevate binary launch.

## Sources

- MITRE ATT&CK T1548.002 - https://attack.mitre.org/techniques/T1548/002/
- UACME - https://github.com/hfiref0x/UACME
- Microsoft User Account Control - https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
