---
summary: "Forging a process's parent so malicious children appear to descend from a benign, expected process tree."
status: active
tags: [security, techniques, ppid, masquerading, defense-evasion]
private: false
---

# Parent PID Spoofing

## Purpose

Forging a process's parent so malicious children appear to descend from a benign, expected process tree.

## How It Works

- On Windows a process can select an arbitrary parent by passing `PROC_THREAD_ATTRIBUTE_PARENT_PROCESS` to `UpdateProcThreadAttribute`.
- The chosen parent handle is supplied in the `STARTUPINFOEX` structure to `CreateProcess`, which then records that PID as the parent.
- The spoofing process needs a handle to the target parent with `PROCESS_CREATE_PROCESS` rights, typically requiring the parent to be same-or-lower privilege.
- The new process also inherits the security token and session context of the spoofed parent, aiding masquerade.

## Engineering Notes

- Common cover parents are `explorer.exe`, `svchost.exe`, or `services.exe` to blend into expected trees.
- Maps to MITRE ATT&CK T1134.004 (Access Token Manipulation: Parent PID Spoofing).
- A related mitigation-bypass abuse sets `PROCESS_CREATION_MITIGATION_POLICY` via the same attribute list to weaken child hardening.

## Defensive Use

- Correlate the recorded PPID with the actual creator; Windows Event ID 4688 and Sysmon Event ID 1 log both parent image and command line.
- Flag mismatches where a claimed parent never spawns that child (e.g. `explorer.exe` parenting `cmd.exe` running encoded commands).
- Watch for `SeDebugPrivilege` use and cross-process handle opens preceding creation.

## Sources

- MITRE ATT&CK T1134.004 - https://attack.mitre.org/techniques/T1134/004/
- Microsoft UpdateProcThreadAttribute - https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-updateprocthreadattribute

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
