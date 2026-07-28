---
summary: "Velociraptor is an endpoint DFIR platform using the VQL query language for scalable hunting and evidence collection."
status: active
tags: [security, dfir, velociraptor, vql]
private: false
---

# Velociraptor DFIR Platform

## Purpose

Velociraptor is an endpoint DFIR platform using the VQL query language for scalable hunting and evidence collection.

## VQL and Artifact Model

- VQL (Velociraptor Query Language) is a SQL-inspired language whose plugins and functions expose host state: processes, registry, filesystem, ETW, and prefetch.
- Artifacts are reusable YAML definitions that wrap one or more VQL queries, declare parameters, and return typed rows; they are the unit of collection and hunting.
- Artifacts are categorized as Client (run on endpoints), Server (run on the server), and Event (long-running monitoring queries).
- Notebooks provide post-collection analysis with VQL over collected results.

## Client-Server Hunt Orchestration

- Agents (clients) maintain a persistent TLS connection to the server and poll for tasking; results stream back as artifact collections.
- A hunt broadcasts one or more artifacts to a labeled set of clients, collecting results asynchronously as endpoints check in.
- The GUI and API allow scheduling collections, monitoring hunt progress, and exporting results for offline analysis.

## Live Triage and Remote Collection

- The offline collector builds a standalone binary/config to acquire triage data from hosts without deploying the full agent.
- Remote artifact collection supports on-demand pulls of files, memory-resident data, and forensic parsers (MFT, $UsnJrnl, event logs).
- Event artifacts enable continuous monitoring and real-time detection feeding into the server.

## Sources

- Velociraptor Documentation - https://docs.velociraptor.app/
- Velociraptor GitHub - https://github.com/Velocidex/velociraptor

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
