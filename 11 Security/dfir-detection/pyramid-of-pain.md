---
summary: "The Pyramid of Pain ranks indicator types by how much cost detecting them imposes on an adversary."
status: active
tags: [security, dfir, indicators, threat-hunting]
private: false
---

# Pyramid of Pain

## Purpose

The Pyramid of Pain ranks indicator types by how much cost detecting them imposes on an adversary.

## Indicator Tiers

- Hash values (base): trivial - a single byte change yields a new hash, so blocking them costs the adversary almost nothing.
- IP addresses: easy - rotated cheaply via proxies, VPNs, and hosting churn.
- Domain names: slightly harder - require registration and DNS changes.
- Network/host artifacts: annoying - user-agents, registry keys, file paths tie to specific tooling.
- Tools: challenging - forcing an attacker to find or build new tooling.
- TTPs (apex): tough - tactics, techniques, and procedures reflect ingrained behavior that is expensive to change.

## Adversary Cost

- Cost to the adversary rises with each tier; the higher you detect, the more you disrupt operations.
- Low-tier indicators are abundant but brittle and short-lived; high-tier detections are durable.

## Prioritizing Detections

- Hunt and build detections targeting TTPs and tools, not just hashes and IPs.
- Behavioral analytics (e.g. mapped to MITRE ATT&CK) sit near the apex and force real adversary retooling.
- Low-tier IOCs still have value for cheap blocking and enrichment, but should not anchor a detection program.

## Sources

- Pyramid of Pain - David Bianco - https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html
- SANS Pyramid of Pain - https://www.sans.org/tools/the-pyramid-of-pain/

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
