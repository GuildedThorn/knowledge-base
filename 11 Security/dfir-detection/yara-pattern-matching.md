---
summary: "YARA is a rule language for identifying and classifying malware and files by textual and binary pattern signatures."
status: active
tags: [security, dfir, yara, malware, signatures]
private: false
---

# YARA Pattern Matching

## Purpose

YARA is a rule language for identifying and classifying malware and files by textual and binary pattern signatures.

## Rule Anatomy

- A rule declares an optional `meta` section, a `strings` section defining patterns, and a mandatory `condition` boolean expression.
- Strings come in three forms: text strings (`"..."`), hex strings (`{ E2 34 ?? C8 }` with wildcards and jumps), and regular expressions (`/pattern/`).
- The `condition` references string identifiers (`$a`, `$b`) and supports counts (`#a`), offsets (`@a`), `at`, `in`, `filesize`, and quantifiers like `2 of ($a*)` or `all of them`.
- Rules can inherit and reference other rules by name, enabling composition.

## String Modifiers and Scanning

- Text-string modifiers include `nocase`, `wide` (UTF-16), `ascii`, `fullword`, `xor`, and `base64` to catch encoded variants.
- Regex strings support standard operators plus the same `nocase`/`wide` modifiers; anchoring reduces false positives and cost.
- The scanner runs against files, directories, or a live process/PID, reading memory to catch unpacked or injected payloads absent from disk.
- Modules (`pe`, `elf`, `math`, `hash`, `dotnet`) expose structured fields and entropy for richer conditions; external variables parameterize rules at scan time.

## Sources

- YARA Documentation - https://yara.readthedocs.io/
- YARA Project - https://virustotal.github.io/yara/
- YARA GitHub - https://github.com/VirusTotal/yara

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
