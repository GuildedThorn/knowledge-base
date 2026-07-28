---
summary: "Injecting and executing code in another process using VirtualAllocEx, WriteProcessMemory, and CreateRemoteThread."
status: active
tags: [security, techniques, injection, process, defense-evasion]
private: false
---

# Process Injection via CreateRemoteThread

## Purpose

Injecting and executing code in another process using VirtualAllocEx, WriteProcessMemory, and CreateRemoteThread.

## How It Works

- The classic sequence opens a target with `OpenProcess`, allocates memory with `VirtualAllocEx`, writes a payload with `WriteProcessMemory`, then starts it with `CreateRemoteThread`.
- For DLL injection the payload is a path string and the thread start routine is `LoadLibrary`; for shellcode the allocation is marked executable and the thread points at the code directly.
- Executing inside a trusted process lets the attacker inherit its identity, network access, and often evade process-based allow-listing.
- The technique underpins defense evasion by hiding activity within legitimate binaries such as explorer.exe or svchost.exe.

## Requirements and Detection Surface

- The injector needs a handle with PROCESS_VM_WRITE, PROCESS_VM_OPERATION, and PROCESS_CREATE_THREAD access.
- RWX allocations and cross-process memory writes are strong signals for EDR.
- EDR products hook or telemeter this API set (VirtualAllocEx, WriteProcessMemory, CreateRemoteThread) to flag remote execution.

## Defensive Use

- Monitor Sysmon Event IDs 8 (CreateRemoteThread) and 10 (ProcessAccess) for cross-process activity.
- Baseline which processes legitimately spawn threads in others; alert on anomalies.
- Hunt for RWX private memory regions and unbacked executable pages in running processes.

## Sources

- MITRE ATT&CK T1055 - https://attack.mitre.org/techniques/T1055/
- Microsoft CreateRemoteThread - https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethread

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
