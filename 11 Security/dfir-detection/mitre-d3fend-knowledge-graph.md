---
summary: "D3FEND is a knowledge graph of defensive cybersecurity techniques linked to the offensive ATT&CK techniques they counter."
status: active
tags: [security, dfir, d3fend, defense, countermeasures]
private: false
---

# MITRE D3FEND Countermeasure Knowledge Graph

## Purpose

D3FEND is a knowledge graph of defensive cybersecurity techniques linked to the offensive ATT&CK techniques they counter.

## Defensive Taxonomy

- D3FEND organizes countermeasures under top-level defensive tactics: Model, Harden, Detect, Isolate, Deceive, Evict (and Restore in later revisions).
- Each tactic contains defensive techniques (e.g. File Analysis, Network Traffic Analysis, Process Segment Execution Prevention) with formal definitions.
- The framework is expressed as an OWL ontology, making techniques, artifacts, and relations queryable as a semantic graph.
- It is inference-based and curated, distinguishing precise defensive semantics from marketing labels.

## Digital Artifacts and Mapping

- A Digital Artifact Ontology models the objects techniques act upon (files, processes, network sessions, credentials), forming the graph's connective tissue.
- Defensive techniques "produce" or "analyze" artifacts, and offensive ATT&CK techniques "produce" the same artifacts, creating the linkage.
- This artifact bridge yields the ATT&CK-to-D3FEND mapping: given an adversary technique, defenders find countermeasures that address the shared artifacts.
- Use cases include capability gap analysis, evaluating security-product claims, and structuring a defense-in-depth architecture.

## Sources

- MITRE D3FEND - https://d3fend.mitre.org/
- D3FEND GitHub - https://github.com/d3fend

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
