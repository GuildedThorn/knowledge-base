---
summary: "The Sleuth Kit is an open library of disk and file-system forensic tools, with Autopsy as its investigative GUI."
status: active
tags: [security, dfir, sleuthkit, autopsy, disk-forensics]
private: false
---

# The Sleuth Kit and Autopsy

## Purpose

The Sleuth Kit is an open library of disk and file-system forensic tools, with Autopsy as its investigative GUI.

## Layered Tool Model

- Tools are named by layer prefix: `mm*` for volume/partition, `fs*` for file-system metadata, `blk*` for data-unit blocks, `i*` for inode/metadata, and `f*`/`j*` for file-name and journal layers.
- `fls` lists file and directory names, including deleted entries recoverable from unallocated metadata.
- `istat` dumps metadata for a given inode; `icat` streams the content of the blocks it points to.
- `blkls` extracts unallocated space, feeding carvers when metadata pointers are gone.

## File-System Parsing and Carving

- Supports NTFS, FAT/exFAT, ext2/3/4, HFS+, ISO9660, YAFFS2, and UFS through a common abstraction layer.
- Timeline generation via `fls -m` plus `mactime` builds a MAC (modified/accessed/changed) chronology.
- Deleted-file recovery relies on residual inode pointers; full carving of overwritten metadata needs external tools like PhotoRec.

## Autopsy Workflow

- Organizes evidence into cases and data sources, running ingest modules (hash lookup, keyword search, EXIF, web artifacts) in parallel.
- Central hash database flags known-bad and filters known-good (NSRL) files.
- Results, tags, and reports export to HTML, Excel, and portable case formats for collaboration.

## Sources

- The Sleuth Kit - https://www.sleuthkit.org/
- Autopsy - https://www.autopsy.com/
- Sleuth Kit GitHub - https://github.com/sleuthkit/sleuthkit

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
