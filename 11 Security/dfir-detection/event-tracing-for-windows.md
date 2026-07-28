---
summary: "ETW is the kernel-level tracing facility that emits detailed provider events underpinning EDR and forensic telemetry."
status: active
tags: [security, dfir, etw, windows, tracing]
private: false
---

# Event Tracing for Windows (ETW)

## Purpose

ETW is the kernel-level tracing facility that emits detailed provider events underpinning EDR and forensic telemetry.

## Provider, Session, Consumer Model

- Providers instrument code and emit events; they register a GUID and can be enabled at runtime without recompilation.
- Sessions (controllers) enable providers, set keyword/level filters, and route events into buffers backed by memory or an .etl file.
- Consumers subscribe to real-time sessions or read .etl logs to decode and process events.
- The manifest-based model (EventRegister/EventWrite) supersedes the older classic (MOF) provider model.

## Key Security Providers

- Microsoft-Windows-Threat-Intelligence surfaces sensitive kernel calls (memory allocation, remote thread creation) and typically requires PPL (protected process light) for EDR use.
- Microsoft-Windows-DNS-Client records name resolution; Microsoft-Windows-PowerShell logs script block and pipeline activity.
- Microsoft-Windows-Kernel-Process and Kernel-Network provide process and connection telemetry without a driver.

## Consumption for Detection

- EDR products consume ETW in-process or via a real-time session to reconstruct behavior chains that file/registry auditing miss.
- Tools such as logman, wpr, xperf, and SilkETW/SealighterTI configure sessions and collect provider output.
- ETW is subject to tampering (patching, provider unregistration, PPL bypass), so telemetry integrity is a defensive concern.

## Sources

- About Event Tracing - Microsoft Learn - https://learn.microsoft.com/en-us/windows/win32/etw/about-event-tracing
- ETW Providers - https://learn.microsoft.com/en-us/windows/win32/etw/event-tracing-portal

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
