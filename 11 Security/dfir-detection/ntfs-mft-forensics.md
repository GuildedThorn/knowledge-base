---
summary: "The NTFS $MFT records every file's metadata, timestamps, and resident data, anchoring disk-based timeline forensics."
status: active
tags: [security, dfir, ntfs, mft, disk-forensics]
private: false
---

# NTFS Master File Table Forensics

## Purpose

The NTFS $MFT records every file's metadata, timestamps, and resident data, anchoring disk-based timeline forensics.

## Record and Attribute Layout

- The $MFT is a metadata file holding one record (typically 1024 bytes) per file or directory on the volume.
- Each record begins with a FILE signature and a fixup array, followed by a sequence of typed attributes.
- Key attributes: $STANDARD_INFORMATION, $FILE_NAME, $DATA, $INDEX_ROOT, and $ATTRIBUTE_LIST.
- Small files store their content resident inside the record; larger files use non-resident data runs pointing to clusters.

## Timestamps

- $STANDARD_INFORMATION and $FILE_NAME each carry four MACB timestamps (Modified, Accessed, Changed/MFT-modified, Born/created).
- $STANDARD_INFORMATION times are user/API writable and thus subject to timestomping; $FILE_NAME times are updated by the kernel and harder to forge.
- Comparing the two attribute sets exposes anti-forensic timestamp manipulation.

## Resident Data and Slack

- Deleted files often persist in the $MFT until their record is reused, aiding recovery.
- Resident data recovery pulls small file contents directly from records without the raw clusters.
- Record and file slack can retain fragments of prior data for analysis.

## Sources

- Master File Table - Microsoft Learn - https://learn.microsoft.com/en-us/windows/win32/fileio/master-file-table
- libfsntfs (Metz) - https://github.com/libyal/libfsntfs

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
