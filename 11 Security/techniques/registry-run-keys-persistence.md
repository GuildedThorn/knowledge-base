---
summary: "Establishing auto-start persistence via Run/RunOnce registry keys and the Startup folder executed at logon."
status: active
tags: [security, techniques, registry, autostart, persistence]
private: false
---

# Registry Run Keys Persistence

## Purpose

Establishing auto-start persistence via Run/RunOnce registry keys and the Startup folder executed at logon.

## Key Locations

- `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` runs for all users at boot/logon and requires administrative write access.
- `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` runs only for the current user and is writable without elevation.
- `RunOnce` variants execute a single time then delete their value, useful for staged installers.
- The per-user and all-users Startup folders (`shell:startup`, `shell:common startup`) drop shortcuts or executables run at logon.
- Each value is a command line; the name is arbitrary and often mimics a legitimate product.

## Detection Notes

- Sysinternals Autoruns enumerates every autostart extensibility point including all Run key variants and flags unsigned entries.
- Baseline Run key contents and alert on new values, especially those pointing to `%APPDATA%`, `%TEMP%`, or scripting hosts.
- HKCU keys are a low-privilege foothold; HKLM changes imply the attacker already holds admin.
- Registry write events (Sysmon Event ID 12/13) on these paths are high-value telemetry.

## Sources

- MITRE ATT&CK T1547.001 - https://attack.mitre.org/techniques/T1547/001/
- Microsoft Run and RunOnce Keys - https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
