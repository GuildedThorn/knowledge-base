---
summary: "Shellcode analysis reconstructs small position-independent payloads that resolve APIs, stage network access, or bootstrap larger malware."
status: active
tags: [security, reversing, shellcode, malware-analysis]
private: false
---

# Shellcode Analysis

## Purpose

Shellcode analysis reconstructs small position-independent payloads that resolve APIs, stage network access, or bootstrap larger malware.

## Key Ideas

- Shellcode is usually compact, position independent, and designed to run with minimal imports or loader support.
- Common patterns include PEB walking, API hashing, stack strings, decoder stubs, syscall use, and staged download/decrypt logic.
- Context matters: shellcode embedded in documents, exploit payloads, beacons, and loaders may have different assumptions.

## Defensive Use

- Capture the containing exploit or loader context, not only the extracted bytes.
- Emulate or debug safely, document API-resolution logic, and convert stable decoder/config features into signatures.

## Sources

- Practical Malware Analysis - shellcode analysis - https://nostarch.com/malware
- MITRE ATT&CK - Shellcode T1620 Reflective Code Loading - https://attack.mitre.org/techniques/T1620/
- YARA documentation - https://yara.readthedocs.io/en/latest/

## Related

- [Reversing - Index](kb://11-security-reversing-reversing-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
