---
summary: "Kubernetes attack modeling covers cluster, node, workload, registry, identity, CI/CD, and control-plane abuse paths."
status: active
tags: [security, cloud, kubernetes, containers]
private: false
---

# Kubernetes Threat Matrix

## Purpose

Kubernetes attack modeling covers cluster, node, workload, registry, identity, CI/CD, and control-plane abuse paths.

## Key Ideas

- MITRE ATT&CK for Containers and Microsoft's Kubernetes threat matrix give complementary coverage of containerized environments.
- Threat areas include compromised accounts, exposed API servers, malicious images, secret theft, over-permissive pods, persistence controllers, and resource hijacking.
- Kubernetes changes rapidly; matrix content must be tied to the cluster version and platform in use.

## Defensive Use

- Use RBAC least privilege, Pod Security Admission, network policies, image admission controls, audit logging, secrets hygiene, and restricted API-server exposure.
- Measure coverage by technique: control-plane logs, kubelet/runtime logs, cloud audit, image registry events, and workload runtime telemetry.

## Sources

- MITRE ATT&CK - Containers Matrix - https://attack.mitre.org/matrices/enterprise/containers/
- Microsoft - Kubernetes threat landscape - https://www.microsoft.com/en-us/security/blog/2025/04/23/understanding-the-threat-landscape-for-kubernetes-and-containerized-assets/
- Kubernetes - Pod Security Admission - https://kubernetes.io/docs/concepts/security/pod-security-admission/

## Related

- [Cloud & Container - Index](kb://11-security-cloud-container-cloud-container-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
