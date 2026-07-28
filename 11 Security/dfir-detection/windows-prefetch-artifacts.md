---
summary: "Windows Prefetch files record program execution history including run counts, timestamps, and referenced files."
status: active
tags: [security, dfir, prefetch, execution-evidence, windows]
private: false
---

# Windows Prefetch Artifacts

## Purpose

Windows Prefetch files record program execution history including run counts, timestamps, and referenced files.

## File Format and Versions

- Prefetch files live in C:\Windows\Prefetch as NAME-HASH.pf, where the hash derives from the executable path.
- The header carries a format version: 17 (XP/2003), 23 (Vista/7), 26 (Windows 8.1), 30 (Windows 10/11).
- Windows 10/11 compress prefetch data with the MAM (Xpress Huffman) algorithm, requiring decompression before parsing.
- Files are created to speed application launch, making them a reliable side-effect record of execution.

## Timestamps and Run Count

- Each file records a run count and up to eight last-run timestamps (older versions store only the single most recent).
- The prefetch file's own creation time approximates first execution; its last-modified time tracks the most recent run.
- Presence of a .pf file is strong evidence a program ran, even if the executable was later deleted.

## Referenced Files

- Prefetch stores a list of files and directories the program loaded during startup (DLLs, config, data files).
- These references reveal working directories, dependencies, and loaded artifacts useful for reconstructing activity.
- Tools like PECmd parse all of this, including decompression and volume information, for timeline building.

## Sources

- libscca (Metz) - https://github.com/libyal/libscca
- PECmd (Eric Zimmerman) - https://github.com/EricZimmerman/PECmd

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
