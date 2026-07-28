---
summary: "Sysmon is a Windows system service that logs high-fidelity process, network, and file events for detection and forensics."
status: active
tags: [security, dfir, sysmon, windows, telemetry]
private: false
---

# Sysmon Endpoint Telemetry

## Purpose

Sysmon is a Windows system service that logs high-fidelity process, network, and file events for detection and forensics.

## Event Catalog

- Sysmon installs as a driver plus service and writes to the `Microsoft-Windows-Sysmon/Operational` event log, surviving reboots.
- Key event IDs include 1 (process create), 3 (network connection), 7 (image/DLL load), 8 (CreateRemoteThread), 10 (process access), and 11 (file create).
- Additional IDs cover registry changes (12-14), named pipes (17-18), WMI subscriptions (19-21), DNS queries (22), and file delete (23-26).
- Process create events carry command line, parent process, integrity level, and computed image hashes.

## Configuration and Correlation

- Behavior is governed by an XML config that whitelists or blacklists per event type using `include`/`exclude` rules and field conditions (`image`, `is`, `contains`, `begin with`).
- `HashAlgorithms` selects MD5/SHA1/SHA256/IMPHASH; hashes enable pivoting to threat-intel feeds and known-bad matching.
- Every event emits a `ProcessGuid`, a durable identifier that correlates activity across event types and time even after PID reuse.
- Community baselines like SwiftOnSecurity's config reduce noise; Sysmon logs pair naturally with Sigma rules and MITRE ATT&CK technique mapping.

## Sources

- Sysmon - Microsoft Learn - https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon
- SwiftOnSecurity Config - https://github.com/SwiftOnSecurity/sysmon-config

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
