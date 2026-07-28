---
summary: "Shortcut LNK files and Jump Lists embed target paths, timestamps, and volume data proving file and application access."
status: active
tags: [security, dfir, lnk, jumplists, user-activity]
private: false
---

# Windows LNK and Jump List Forensics

## Purpose

Shortcut LNK files and Jump Lists embed target paths, timestamps, and volume data proving file and application access.

## LNK Structure

- LNK shortcut files follow the MS-SHLLINK binary format and are auto-created in `Recent` when a user opens a file or document.
- Each LNK embeds the target's full path, size, the three `$STANDARD_INFORMATION` MAC timestamps of the target at creation, and a shell item ID list.
- Volume metadata includes the drive serial number, volume label, and drive type, identifying local vs. removable vs. network origin.
- LNK MAC times themselves record first and last access to the target through that shortcut.

## Jump Lists

- Jump Lists persist in `%AppData%\Microsoft\Windows\Recent\AutomaticDestinations` and `CustomDestinations`, named by a per-application AppID hash.
- AutomaticDestinations files are OLE compound (structured storage) containers holding embedded LNK streams plus a DestList MRU ordering stream.
- The DestList stream provides an accurate most-recently-used order and per-entry access counts and timestamps.
- Parse LNK files with LECmd and Jump Lists with JLECmd to resolve targets, volume data, and MRU sequence.
- Entries survive deletion of the original target, evidencing files no longer present.

## Sources

- MS-SHLLINK Spec - https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-shllink/
- LECmd (Eric Zimmerman) - https://github.com/EricZimmerman/LECmd

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
