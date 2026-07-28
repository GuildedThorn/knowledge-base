---
summary: "Windows event triage correlates authentication, process, service, PowerShell, task, Defender, and Sysmon events into an incident timeline."
status: active
tags: [security, dfir, windows, event-logs]
private: false
---

# Windows Event Log Triage

## Purpose

Windows event triage correlates authentication, process, service, PowerShell, task, Defender, and Sysmon events into an incident timeline.

## Key Ideas

- Authentication and process creation anchor most timelines: who logged on, from where, with what type, and what ran afterward.
- Security, System, PowerShell, Defender, TaskScheduler, WMI, and Sysmon channels answer different parts of the same story.
- Event IDs alone are not detections; meaning comes from entity, source/destination, sequence, rarity, and business context.

## Defensive Use

- Enable command-line logging, PowerShell module/script-block logging where appropriate, Sysmon or EDR telemetry, and centralized retention.
- Normalize host clocks and preserve raw events; timeline integrity collapses when logs are partial or time drift is ignored.

## Sources

- Microsoft - Audit logon events - https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-logon-events
- Microsoft Sysmon documentation - https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon
- Splunk Security Content - Windows possible credential dumping - https://research.splunk.com/endpoint/e4723b92-7266-11ec-af45-acde48001122/

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
