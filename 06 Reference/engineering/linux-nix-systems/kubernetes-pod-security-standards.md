---
summary: "Kubernetes Pod Security Standards define Privileged, Baseline, and Restricted profiles for controlling pod-level privilege and isolation."
status: active
tags: [reference, engineering, kubernetes, containers, security]
private: false
---

# Kubernetes Pod Security Standards

## Purpose

Pod Security Standards give Kubernetes operators a common language for pod hardening policy: `privileged`, `baseline`, and `restricted`.

## Core Model

- `privileged` is effectively unrestricted and intended for trusted infrastructure workloads.
- `baseline` blocks known privilege-escalation patterns while preserving compatibility for common workloads.
- `restricted` follows stronger pod-hardening expectations and is appropriate for security-sensitive application namespaces when compatible.
- Pod Security Admission enforces these profiles at namespace scope.

## Engineering Notes

- Namespace-level enforcement is simple but coarse; highly mixed namespaces are harder to secure cleanly.
- Windows pods differ from Linux pods; some Linux security-context controls do not apply.
- Sandboxed runtimes such as gVisor or Kata change the isolation model but do not remove the need for explicit policy.
- For production clusters, pin policy versions intentionally instead of inheriting breaking changes accidentally.

## Sources

- Kubernetes docs - Pod Security Standards - https://kubernetes.io/docs/concepts/security/pod-security-standards/
- Kubernetes docs - Pod Security Admission - https://kubernetes.io/docs/concepts/security/pod-security-admission/

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Containers, Namespaces, and cgroups](kb://06-reference-engineering-linux-nix-systems-containers-namespaces-and-cgroups)
- [Container Escape and Runtime Hardening](kb://11-security-cloud-container-container-escape-and-runtime-hardening)
