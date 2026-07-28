---
summary: "EQL is a query language for expressing event relationships and ordered sequences to hunt for behavioral threats."
status: active
tags: [security, dfir, eql, elastic, hunting]
private: false
---

# Elastic Event Query Language (EQL)

## Purpose

EQL is a query language for expressing event relationships and ordered sequences to hunt for behavioral threats.

## Event and Sequence Syntax

- A basic query matches a single event category with a condition, e.g. `process where process.name == "cmd.exe"`.
- The `sequence` keyword matches an ordered series of events, expressing multi-step attacker behavior rather than isolated indicators.
- Wildcards (`like`, `regex`), `in` sets, and function calls (`endsWith`, `cidrMatch`, `wildcard`) refine conditions.
- Sample and `where` filters run against event-based indices with an `@timestamp` and event category field.

## Join Keys and Windowing

- Sequences share state through `by` join keys (such as `process.entity_id` or `host.id`) so steps correlate on the same entity.
- `with maxspan=5m` bounds how far apart matched events may occur, discarding partial sequences that exceed the window.
- An optional `until` clause terminates a sequence early when a cancelling event (like process termination) is seen.

## Behavioral Detection

- Ordered sequences catch patterns like a Word process spawning PowerShell that then makes a network connection.
- Elastic Security ships prebuilt EQL detection rules mapped to MITRE ATT&CK techniques.
- Runs over host telemetry (Elastic Endpoint, Sysmon, Auditbeat) normalized to the Elastic Common Schema (ECS).

## Sources

- EQL Documentation - https://eql.readthedocs.io/
- Elastic EQL Reference - https://www.elastic.co/guide/en/elasticsearch/reference/current/eql.html

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
