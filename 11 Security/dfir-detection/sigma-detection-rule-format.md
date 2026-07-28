---
summary: "Sigma is a YAML-based generic signature format for describing log-based detections portably across SIEM and query backends."
status: active
tags: [security, dfir, sigma, detection-rules, siem]
private: false
---

# Sigma Detection Rule Format

## Purpose

Sigma is a YAML-based generic signature format for describing log-based detections portably across SIEM and query backends.

## Rule Structure

- Every rule is a YAML document with metadata (`title`, `id`, `status`, `level`, `tags`) plus the core `logsource` and `detection` blocks.
- `logsource` scopes the rule to a data domain via `product`, `category`, and `service` keys (e.g. `product: windows`, `category: process_creation`).
- `detection` holds one or more named search identifiers (maps or lists) and a `condition` expression that combines them with `and`, `or`, `not`, `1 of`, `all of`.
- Maps match fields as AND across keys; list values within a key match as OR.

## Field Modifiers and Conversion

- Value modifiers are appended to field names with `|`: `contains`, `startswith`, `endswith`, `re` (regex), `base64`, `base64offset`, `all`, and CIDR/`gt`/`lt` numeric comparisons.
- `null` and wildcards (`*`, `?`) express presence and pattern matching without regex.
- pySigma is the current conversion engine; it parses rules into an intermediate representation and emits backend-specific queries.
- Backends (via pySigma plugins) target Splunk SPL, Elasticsearch/ES-QL, Microsoft Sentinel KQL, QRadar, and others; pipelines remap field names per schema (e.g. ECS).

## Sources

- SigmaHQ GitHub - https://github.com/SigmaHQ/sigma
- Sigma Specification - https://github.com/SigmaHQ/sigma-specification
- SigmaHQ Site - https://sigmahq.io/

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
