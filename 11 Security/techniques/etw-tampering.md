---
summary: "Disabling or blinding Event Tracing for Windows providers to suppress the telemetry that EDR and logging rely on."
status: active
tags: [security, techniques, etw, defense-evasion, telemetry]
private: false
---

# ETW Tampering

## Purpose

Disabling or blinding Event Tracing for Windows providers to suppress the telemetry that EDR and logging rely on.

## Core Model

- Event Tracing for Windows is the kernel and user-mode plumbing that carries events from providers to consumers such as EDR agents, Sysmon, and the event log.
- Many EDR products consume the Microsoft-Windows-Threat-Intelligence ETW provider for in-memory and syscall visibility, making ETW a high-value target.
- Blinding ETW does not stop the malicious action; it removes the evidence trail that would otherwise surface it.

## How It Works

- Patching `EtwEventWrite` (or `NtTraceEvent`) in `ntdll.dll` to return immediately drops all events from the current process without disabling the provider globally.
- Session-level tampering removes providers from an active trace session or stops the session outright via `EnableTraceEx2`/logman.
- Registry manipulation under `HKLM\SYSTEM\CurrentControlSet\Control\WMI\Autologger` and provider `Enabled` values can disable logging across reboots.

## Detection

- Watch for user-mode patches to `ntdll` ETW stubs, unexpected edits to Autologger registry keys, and trace sessions being stopped or providers being removed.
- A sudden drop in expected event volume from a host or process is itself a detection signal; protect ETW-consuming agents with tamper protection.

## Sources

- MITRE ATT&CK T1562.006 - https://attack.mitre.org/techniques/T1562/006/
- Microsoft Event Tracing - https://learn.microsoft.com/en-us/windows/win32/etw/event-tracing-portal

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
