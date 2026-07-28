---
summary: "ShellBags registry keys record folder browsing history and view settings, evidencing accessed directories and removable media."
status: active
tags: [security, dfir, shellbags, user-activity]
private: false
---

# Windows ShellBags Forensics

## Purpose

ShellBags registry keys record folder browsing history and view settings, evidencing accessed directories and removable media.

## Key Structure

- ShellBags live in the per-user `NTUSER.DAT` and `UsrClass.dat` hives under the `BagMRU` and `Bags` keys of the Shell subtree.
- `BagMRU` stores the hierarchical folder tree as nested keys of binary shell item ID lists (PIDLs); `Bags` stores the matching view/layout settings.
- Each PIDL encodes the folder name plus embedded MFT reference and `$STANDARD_INFORMATION` timestamps for the target directory.
- The structure only records folders opened via Explorer, so its presence implies the user navigated to that path.

## Evidence Value

- ShellBags persist even after a folder is deleted, giving evidence of directories that no longer exist on the volume.
- Network share paths (UNC) and removable/USB volume roots appear, showing access to external and remote storage.
- Embedded shell-item timestamps and the key last-write time support timelining of folder access.
- Parse with ShellBags Explorer, which decodes the nested PIDLs into a readable folder tree with resolved timestamps.
- Interpretation caveat: timestamps reflect the target folder's metadata, and automated/programmatic access can also create entries.

## Sources

- ShellBags Explorer (Eric Zimmerman) - https://ericzimmerman.github.io/
- SANS ShellBags Reference - https://www.sans.org/posters/windows-forensic-analysis/

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
