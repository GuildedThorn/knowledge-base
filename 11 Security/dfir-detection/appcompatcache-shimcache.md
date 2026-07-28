---
summary: "Shimcache records program paths and metadata the OS tracks for application compatibility, evidencing prior execution."
status: active
tags: [security, dfir, shimcache, execution-evidence]
private: false
---

# AppCompatCache (Shimcache) Analysis

## Purpose

Shimcache records program paths and metadata the OS tracks for application compatibility, evidencing prior execution.

## Cache Location and Structure

- Stored in the SYSTEM registry hive under `ControlSet\Control\Session Manager\AppCompatCache`, parsed from the last-loaded control set.
- The cache is written to the registry only at shutdown, so recent entries in a live system persist in kernel memory until then.
- Entry format and field layout differ per OS version (XP, Win7, Win8, Win10/11), requiring version-aware parsers such as AppCompatCacheParser.
- Capacity is bounded (roughly 96 entries on XP, 512+ on later Windows), so older records age out.

## Fields and Interpretation

- Each entry stores the full file path, the file's `$STANDARD_INFORMATION` last-modified timestamp, and on some versions a size or execution flag.
- Older Windows versions carried an explicit "InsertFlag"/execution flag; Windows 10+ removed the reliable execution indicator.
- Presence in the cache proves the OS enumerated the binary (e.g., appeared in a browsed folder), which is NOT proof it executed.
- The recorded timestamp is the file's modification time, not the execution time, so it must not be read as a run time.
- Order of entries reflects most-recent-first insertion, useful for relative sequencing but not absolute timing.

## Sources

- Mandiant AppCompatCache Whitepaper - https://cloud.google.com/blog/topics/threat-intelligence/caching-out-the-val/
- AppCompatCacheParser - https://github.com/EricZimmerman/AppCompatCacheParser

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
