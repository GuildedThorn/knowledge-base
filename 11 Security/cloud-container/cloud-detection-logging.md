---
summary: "Cloud detection depends on control-plane audit logs, identity events, network flow, workload telemetry, and service-specific data events."
status: active
tags: [security, cloud, detection, logging]
private: false
---

# Cloud Detection and Logging

## Purpose

Cloud detection depends on control-plane audit logs, identity events, network flow, workload telemetry, and service-specific data events.

## Key Ideas

- CloudTrail, Entra/Azure Activity, Google Cloud Audit Logs, Kubernetes audit, and SaaS logs answer different layers of the same incident.
- Management events show control-plane intent; data events are required for object-level access in services like storage.
- Identity context is central: user, role, service principal, workload identity, source IP, user agent, MFA, and assumed-role chain.

## Defensive Use

- Centralize logs into immutable storage, enable data events for critical stores, and write detections for rare API use and impossible role/resource combinations.
- Correlate cloud activity with endpoint and CI/CD logs to find whether an API call came from a human, runner, workload, or attacker.

## Sources

- MITRE ATT&CK - Cloud Matrix - https://attack.mitre.org/matrices/enterprise/cloud/
- AWS CloudTrail documentation - https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html
- MITRE ATT&CK - Cloud Service Metadata DC0070 - https://attack.mitre.org/datacomponents/DC0070/

## Related

- [Cloud & Container - Index](kb://11-security-cloud-container-cloud-container-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
