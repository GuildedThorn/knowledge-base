---
summary: "Creating or modifying a Windows service to gain SYSTEM-level execution that survives reboots."
status: active
tags: [security, techniques, service, persistence, privilege-escalation]
private: false
---

# Windows Service Persistence

## Purpose

Creating or modifying a Windows service to gain SYSTEM-level execution that survives reboots.

## How It Works

- Services are registered with the Service Control Manager (SCM) via `sc.exe create`, `CreateService`, or by writing under `HKLM\System\CurrentControlSet\Services`.
- A service configured with `start= auto` launches at boot, typically in the `LocalSystem` context, giving high-privilege persistence.
- Attackers point the `ImagePath` at a malicious binary, or repurpose an existing service by altering its `ImagePath` or `ServiceDll` (svchost-hosted) value.
- Weak service configurations enable abuse: writable service binaries, weak SCM permissions allowing reconfiguration, and unquoted paths containing spaces.
- Unquoted-path abuse plants an executable like `C:\Program.exe` so SCM runs it instead of the intended `C:\Program Files\...` target.

## Detection Notes

- Security Event ID 4697 and System Event ID 7045 record new service installation.
- Audit service binary and registry ACLs; tools like `accesschk` and PowerUp surface writable-binary and unquoted-path weaknesses.
- Alert on `ImagePath` modifications and new services whose binaries sit in user-writable or temp directories.
- Baseline the installed service set so anomalous additions stand out.

## Sources

- MITRE ATT&CK T1543.003 - https://attack.mitre.org/techniques/T1543/003/
- Microsoft Services - https://learn.microsoft.com/en-us/windows/win32/services/services

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
