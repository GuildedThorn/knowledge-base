---
summary: "Sigma is a portable YAML detection-rule format for expressing log analytics across SIEM backends."
status: active
tags: [security, dfir, detection, sigma]
private: false
---

# Sigma Detection Engineering

## Purpose

Sigma is a portable YAML detection-rule format for expressing log analytics across SIEM backends.

## Key Ideas

- Sigma separates detection intent from backend query syntax, allowing rules to convert to Splunk, Elasticsearch, Sentinel, Loki, and other targets.
- Rule quality depends on logsource mapping, field normalization, false-positive notes, ATT&CK tags, and test data.
- Generic, threat-hunting, emerging-threat, compliance, and placeholder rules serve different operational roles.

## Defensive Use

- Keep Sigma rules in Git, lint and convert in CI, and replay sample logs before deployment.
- Track rule lifecycle status and tune by data source rather than weakening the detection logic globally.

## Sources

- SigmaHQ - Sigma overview - https://sigmahq.io/sigma/
- Sigma documentation - Getting Started - https://sigmahq.io/docs/
- Sigma specification - https://sigmahq.io/sigma-specification/

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
