---
summary: "NIST zero trust architecture shifts access control from implicit network trust to explicit identity, device, policy, and resource-centered decisions."
status: active
tags: [reference, security, architecture, zero-trust, nist]
private: false
---

# Zero Trust Architecture - NIST

## Purpose

Zero Trust Architecture is a security model where access is continuously evaluated based on identity, device posture, policy, resource sensitivity, and context instead of implicit trust from network location.

## Core Model

- Protect resources, not just network segments.
- Authenticate and authorize subjects and devices before resource sessions.
- Minimize implicit trust based on LAN, VPN, ownership, or perimeter location.
- Use policy decision and enforcement points to mediate access.
- Continuously improve policy with telemetry, inventory, and risk signals.

## Implementation Areas

- Identity, credential, and access management.
- Device inventory and endpoint health.
- Microsegmentation or software-defined perimeter controls.
- Application/service identity for cloud-native systems.
- Security analytics and policy feedback loops.

## Engineering Notes

- Zero trust is not a product; it is an architecture and migration path.
- Start with asset inventory and critical-resource prioritization.
- Identity-only zero trust is incomplete if device health, resource context, and telemetry are ignored.
- Legacy systems usually require phased adoption.

## Sources

- NIST SP 800-207 - Zero Trust Architecture - https://csrc.nist.gov/pubs/sp/800/207/final
- NIST NCCoE - Implementing a Zero Trust Architecture - https://pages.nist.gov/zero-trust-architecture/index.html
- NIST NCCoE project page - https://www.nccoe.nist.gov/projects/implementing-zero-trust-architecture

## Related

- [Security Map](kb://01-maps-security-map)
- [Cloud Detection and Logging](kb://11-security-cloud-container-cloud-detection-logging)
- [SIEM and SOC - Architecture](kb://09-observability-siem-and-soc-architecture)
