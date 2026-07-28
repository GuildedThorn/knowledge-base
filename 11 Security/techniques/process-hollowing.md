---
summary: "Creating a suspended benign process, unmapping its image, and replacing it with malicious code to masquerade execution."
status: active
tags: [security, techniques, injection, masquerading, defense-evasion]
private: false
---

# Process Hollowing

## Purpose

Creating a suspended benign process, unmapping its image, and replacing it with malicious code to masquerade execution.

## How It Works

- Attacker calls `CreateProcess` with the `CREATE_SUSPENDED` flag on a legitimate binary (often `svchost.exe`, `explorer.exe`), so no thread runs yet.
- `NtUnmapViewOfSection` (or `ZwUnmapViewOfSection`) frees the memory holding the original executable image at its base address.
- `VirtualAllocEx` reserves memory, and `WriteProcessMemory` writes the malicious PE headers and sections into the hollowed target.
- The thread's `EAX`/`RCX` entry point is patched via `SetThreadContext` and the PEB image base updated to point at the injected code.
- `ResumeThread` starts execution; the process metadata (path, PID owner) still reflects the benign host.

## Detection Notes

- Look for a process whose in-memory image differs from the on-disk file backing it (image/section mismatch).
- The `CREATE_SUSPENDED` + `NtUnmapViewOfSection` + `SetThreadContext` API sequence in one process is a strong signal.
- Memory regions marked RWX or private-committed pages holding a PE header where the module should be file-backed indicate hollowing.
- EDR can flag base-address writes to another process before its first thread resumes.

## Sources

- MITRE ATT&CK T1055.012 - https://attack.mitre.org/techniques/T1055/012/
- Microsoft NtUnmapViewOfSection - https://learn.microsoft.com/en-us/windows/win32/api/winternl/

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
