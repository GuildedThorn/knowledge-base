---
summary: "Container escape risk rises when workloads run privileged, mount host resources, expose runtimes, or lack kernel isolation controls."
status: active
tags: [security, containers, runtime, hardening]
private: false
---

# Container Escape and Runtime Hardening

## Purpose

Container escape risk rises when workloads run privileged, mount host resources, expose runtimes, or lack kernel isolation controls.

## Key Ideas

- Containers share the host kernel; isolation failures are usually about privileges, mounts, namespaces, capabilities, devices, or vulnerable runtime/kernel behavior.
- Dangerous settings include privileged pods, hostPID/hostNetwork, hostPath mounts, broad capabilities, writable root filesystems, and exposed runtime sockets.
- Escape prevention is a policy and platform-control problem, not just image scanning.

## Defensive Use

- Enforce restricted Pod Security Standards, drop Linux capabilities, use seccomp/AppArmor/SELinux, block hostPath where possible, and monitor runtime socket access.
- Patch kernels/runtimes quickly and isolate high-risk workloads onto dedicated nodes.

## Sources

- Kubernetes - Pod Security Standards - https://kubernetes.io/docs/concepts/security/pod-security-standards/
- Kubernetes - Pod Security Admission - https://kubernetes.io/docs/concepts/security/pod-security-admission/
- Microsoft Threat Matrix for Kubernetes - Mitigations - https://microsoft.github.io/Threat-Matrix-for-Kubernetes/mitigations/

## Related

- [Cloud & Container - Index](kb://11-security-cloud-container-cloud-container-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
