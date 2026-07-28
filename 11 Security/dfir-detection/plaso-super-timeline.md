---
summary: "Plaso (log2timeline) aggregates artifacts from disk and logs into a unified super timeline for forensic sequencing."
status: active
tags: [security, dfir, plaso, timeline, log2timeline]
private: false
---

# Plaso Super Timeline Analysis

## Purpose

Plaso (log2timeline) aggregates artifacts from disk and logs into a unified super timeline for forensic sequencing.

## Extraction

- `log2timeline.py` runs parsers and plugins across a source (disk image, mounted volume, or directory) and writes events to a storage file.
- Parsers cover a wide artifact range: registry hives, event logs, prefetch, LNK, browser history, filesystem timestamps, and syslog.
- Parser presets (e.g., `win7`, `winxp`) or `--parsers` filters limit extraction to relevant artifacts and cut noise and runtime.
- Output is a plaso storage file (SQLite-backed) holding normalized events, each timestamped in UTC with a source and description.

## Filtering and Analysis

- `psort.py` reads the storage file and exports to formats such as `l2tcsv`, `json`, or Elasticsearch, applying time-slice and content filters.
- Filtering by date range, artifact type, or keyword focuses the timeline on the incident window and reduces millions of events.
- `psteal.py` combines extraction and export in one command for quick single-pass timelines.
- A super timeline interleaves every artifact chronologically, exposing correlations (e.g., execution then file creation) invisible in single sources.
- Timeline explorer or spreadsheet tooling is typically used downstream to pivot on the l2tcsv/json output.

## Sources

- Plaso Documentation - https://plaso.readthedocs.io/
- Plaso GitHub - https://github.com/log2timeline/plaso

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
