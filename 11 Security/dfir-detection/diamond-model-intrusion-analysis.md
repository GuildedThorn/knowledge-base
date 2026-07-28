---
summary: "The Diamond Model links adversary, capability, infrastructure, and victim to structure and pivot across intrusion analysis."
status: active
tags: [security, dfir, diamond-model, intrusion-analysis]
private: false
---

# Diamond Model of Intrusion Analysis

## Purpose

The Diamond Model links adversary, capability, infrastructure, and victim to structure and pivot across intrusion analysis.

## Core Features

- Every event is a diamond with four vertices: adversary, capability, infrastructure, and victim.
- Edges express relationships: an adversary uses a capability over infrastructure against a victim.
- The adversary vertex splits into operator (who acts) and customer (who benefits), useful for attribution.
- Capability captures tools and techniques; infrastructure covers the physical/logical assets (C2 domains, IPs, email) used to deliver and control them.

## Meta-Features and Pivoting

- Meta-features annotate events: timestamp, phase, result, direction, methodology, and resources.
- Analysts pivot along any vertex to discover related events - e.g. from one C2 IP to other victims sharing it.
- Confidence values weight each feature and edge, keeping assessments explicit and revisable.

## Threads and Campaigns

- Ordered events chained by adversary intent form activity threads (often aligned to the kill chain).
- Threads sharing features are clustered into activity groups, enabling campaign-level tracking and analytic pivoting across intrusions.

## Sources

- The Diamond Model Paper - https://www.threatintel.academy/wp-content/uploads/2020/07/diamond-model.pdf
- DTIC Record - https://apps.dtic.mil/sti/citations/ADA586960

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
