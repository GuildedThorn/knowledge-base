---
summary: "The NTFS $UsnJrnl logs a rolling record of file create, delete, and rename operations for activity reconstruction."
status: active
tags: [security, dfir, usn-journal, ntfs, disk-forensics]
private: false
---

# NTFS USN Change Journal

## Purpose

The NTFS $UsnJrnl logs a rolling record of file create, delete, and rename operations for activity reconstruction.

## Record Structure

- The journal resides in the `$Extend\$UsnJrnl` metadata file; the `$J` alternate data stream holds the sparse, append-only record stream.
- Each USN record carries the file reference number, parent directory reference number, file name, timestamp, and a reason flag bitmask.
- Reason flags encode the operation type: `DATA_OVERWRITE`, `FILE_CREATE`, `FILE_DELETE`, `RENAME_OLD_NAME`, `RENAME_NEW_NAME`, `CLOSE`, and others.
- The journal is size-capped and wraps, so the oldest records are overwritten; typical retention is hours to days on busy volumes.

## Reconstructing Activity

- Because deletions are logged with the file name and parent reference, USN records evidence files that no longer exist on disk.
- Correlating parent reference numbers against the MFT reconstructs the full path even after the entry is removed.
- Rename pairs (OLD_NAME then NEW_NAME) reveal staging, masquerading, or ransomware extension changes.
- Parse with MFTECmd, which resolves USN entries against the `$MFT` to output timelined, path-resolved events.
- Sequential USN numbers give reliable ordering even when timestamps are manipulated.

## Sources

- Change Journals - Microsoft Learn - https://learn.microsoft.com/en-us/windows/win32/fileio/change-journals
- MFTECmd (Eric Zimmerman) - https://github.com/EricZimmerman/MFTECmd

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
