---
summary: "Process injection hides execution inside another process to evade process-based defenses or inherit access from the target process."
status: active
tags: [security, technique, attack, process-injection]
private: false
---

# Process Injection

## Purpose

Process injection hides execution inside another process to evade process-based defenses or inherit access from the target process.

## Key Ideas

- ATT&CK splits injection into sub-techniques such as DLL injection, process hollowing, thread execution hijacking, APC injection, and proc-memory abuse.
- The core pattern is cross-process memory manipulation plus a transfer of execution into the target process.
- Injection is a behavior family; the same labels appear across malware, C2 frameworks, and legitimate debuggers.

## Defensive Use

- Collect process-access telemetry, image loads, memory allocation/protection changes, and suspicious parent-child/process ancestry.
- Alert on unusual access into sensitive processes and unsigned code executing inside normally signed/high-value processes.

## Sources

- MITRE ATT&CK - Process Injection T1055 - https://attack.mitre.org/techniques/T1055/
- MITRE ATT&CK - DLL Injection T1055.001 - https://attack.mitre.org/techniques/T1055/001/
- Microsoft ASR rules reference - https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
