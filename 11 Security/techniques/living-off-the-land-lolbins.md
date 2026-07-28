---
summary: "Living-off-the-land tradecraft abuses trusted binaries, scripts, libraries, and admin tools for execution, transfer, evasion, or discovery."
status: active
tags: [security, technique, lolbas, windows]
private: false
---

# Living off the Land and LOLBins

## Purpose

Living-off-the-land tradecraft abuses trusted binaries, scripts, libraries, and admin tools for execution, transfer, evasion, or discovery.

## Key Ideas

- LOLBAS catalogs Microsoft-signed binaries, scripts, and libraries with unexpected abuse paths and ATT&CK mappings.
- Living-off-the-land is attractive because the binaries are already present, signed, and often allowed by controls.
- Detection should focus on command context, parent process, working directory, network behavior, and rare function use.

## Defensive Use

- Build allowlists around expected administrative workflows, not just executable names.
- Alert on LOLBins performing download, script execution, proxy execution, archive, credential, or child-process behavior outside normal owner groups.

## Sources

- LOLBAS project - https://lolbas-project.github.io/
- LOLBAS GitHub repository - https://github.com/LOLBAS-Project/LOLBAS
- MITRE ATT&CK - System Binary Proxy Execution T1218 - https://attack.mitre.org/techniques/T1218/

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
