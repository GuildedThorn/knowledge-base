---
summary: "ATT&CK is a curated knowledge base of adversary tactics, techniques, and procedures observed in real-world intrusions."
status: active
tags: [security, dfir, attack, ttp, adversary]
private: false
---

# MITRE ATT&CK Framework

## Purpose

ATT&CK is a curated knowledge base of adversary tactics, techniques, and procedures observed in real-world intrusions.

## Taxonomy

- Tactics represent the adversary's goal for a phase (e.g. Initial Access, Persistence, Lateral Movement, Exfiltration) and act as columns in a matrix.
- Techniques (IDs like `T1059`) describe how a goal is achieved; sub-techniques (`T1059.001`) refine specific implementations such as PowerShell.
- Procedures are concrete observed uses of a technique by named groups or software, grounding the model in reported intrusions.
- Objects link together: Groups, Software (malware/tools), Campaigns, Mitigations, and Data Sources/Components all reference techniques.

## Matrices and Coverage Mapping

- Separate matrices cover Enterprise (Windows, macOS, Linux, cloud, containers, network), Mobile, and ICS environments.
- Data Sources and Data Components indicate which telemetry (e.g. process creation, network traffic) reveals a technique, guiding sensor placement.
- Detections and analytics are mapped to technique IDs so teams can build a coverage heatmap of visibility and gaps.
- The ATT&CK Navigator layers scores and colors onto the matrix; STIX/TAXII feeds distribute the dataset for tooling integration.

## Sources

- MITRE ATT&CK - https://attack.mitre.org/
- ATT&CK Design and Philosophy - https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
