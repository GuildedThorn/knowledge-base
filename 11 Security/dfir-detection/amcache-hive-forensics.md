---
summary: "Amcache.hve stores program metadata including SHA-1 hashes and first-execution times used to trace binary activity."
status: active
tags: [security, dfir, amcache, execution-evidence]
private: false
---

# Amcache Hive Forensics

## Purpose

Amcache.hve stores program metadata including SHA-1 hashes and first-execution times used to trace binary activity.

## Structure and Entries

- Amcache.hve is a standalone registry hive located at `C:\Windows\AppCompat\Programs\Amcache.hve`, populated by the Application Experience service.
- On Windows 8/8.1 the file entries live under the `Root\File` key; Windows 10+ reorganized them under `Root\InventoryApplicationFile`.
- Entries record the full file path, file size, PE compile time, publisher/version strings, and the volume GUID the file resided on.
- Program entries (`InventoryApplication`) capture installed software with install dates and publisher metadata.

## Metadata and Interpretation

- The SHA-1 hash stored per file entry enables direct correlation with threat intelligence and hash reputation lookups, valuable for renamed or deleted binaries.
- Timestamps vary by field: the registry key last-write time approximates when the entry was recorded, not necessarily execution.
- Interpretation is version-specific; older references treating Amcache as pure execution evidence overstate it, as inventory scans also populate entries.
- Use AmcacheParser to normalize the differing schemas and separate file entries from program/driver entries.

## Sources

- ANSSI Analysis of the AmCache - https://cyber.gouv.fr/uploads/2019/01/anssi-coriin_2019-analysis_amcache.pdf
- AmcacheParser - https://github.com/EricZimmerman/AmcacheParser

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
