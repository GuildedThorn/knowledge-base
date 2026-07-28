---
summary: "YARA rules describe malware or file traits with strings, byte patterns, modules, metadata, and boolean conditions."
status: active
tags: [security, reversing, yara, detection]
private: false
---

# YARA Rule Writing

## Purpose

YARA rules describe malware or file traits with strings, byte patterns, modules, metadata, and boolean conditions.

## Key Ideas

- Good rules balance stability and specificity: family logic, config structure, unique code bytes, or protocol constants beat generic strings.
- Metadata should capture author, date, description, reference, sample hash basis, and known false-positive constraints.
- Rules can use text strings, hex patterns, regex, file-size limits, PE/module fields, and boolean logic.

## Defensive Use

- Test against malicious samples and a large clean corpus; rule usefulness depends on false-positive behavior.
- Prefer one purpose per rule and version changes when source samples or logic change.

## Sources

- YARA documentation - https://yara.readthedocs.io/en/latest/
- VirusTotal - YARA Rules API - https://docs.virustotal.com/reference/yara-rule
- VirusTotal - Crowdsourced YARA rules - https://docs.virustotal.com/reference/list-crowdsourced-yara-rules

## Related

- [Reversing - Index](kb://11-security-reversing-reversing-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
