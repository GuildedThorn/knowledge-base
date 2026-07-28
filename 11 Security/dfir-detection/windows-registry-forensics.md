---
summary: "The Windows Registry hives store configuration, autostart, and user-activity keys central to endpoint forensics."
status: active
tags: [security, dfir, registry, hives, windows]
private: false
---

# Windows Registry Forensics

## Purpose

The Windows Registry hives store configuration, autostart, and user-activity keys central to endpoint forensics.

## Hive Files and Structure

- System hives live in C:\Windows\System32\config: SYSTEM, SOFTWARE, SECURITY, SAM, plus DEFAULT.
- Per-user hives are NTUSER.DAT (HKCU) and UsrClass.dat, stored in each user's profile.
- On-disk hives use a regf signature and are organized into hbin blocks holding key (nk), value (vk), and subkey-list cells.
- Every registry key carries a LastWrite timestamp, a critical forensic anchor for change timing.

## Autostart and Persistence

- Autostart extensibility points (ASEPs) are prime persistence locations: Run, RunOnce, Services, Winlogon, and Image File Execution Options.
- The SYSTEM hive holds services, the current control set, and mounted device history (MountedDevices, USBSTOR).
- Comparing baseline ASEPs against a suspect system surfaces malicious persistence entries.

## User Activity

- NTUSER.DAT keys reconstruct user behavior: RecentDocs, RunMRU, TypedPaths, and UserAssist (program run counts/times).
- ShellBags record folder browsing and window layout, evidencing access to specific directories.
- Tools like RegRipper automate extraction of these keys into analyst-ready output.

## Sources

- Registry Hives - Microsoft Learn - https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives
- libregf (Metz) - https://github.com/libyal/libregf
- RegRipper - https://github.com/keydet89/RegRipper3.0

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
