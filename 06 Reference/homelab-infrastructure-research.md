---
summary: "Homelab infrastructure research topics: backups, routing, monitoring, identity, secrets, segmentation, and recovery."
status: active
tags: [reference, homelab, infrastructure, operations]
private: false
---

# Homelab Infrastructure Research

## Purpose

Reusable research map for hardening and operating a homelab like a small production environment without importing enterprise complexity blindly.

## Topic Areas

- Backups: 3-2-1 strategy, restore testing, snapshots, offsite copies, ransomware resistance.
- Network: VLANs, firewall policy, DNS, DHCP, WireGuard, remote recovery, serial/OOB access.
- Identity: SSH keys, SSO where justified, MFA, local break-glass accounts, least privilege.
- Secrets: age/sops, hardware tokens, sealed backups, rotation process.
- Observability: Prometheus/Grafana, logs, uptime checks, alert routing, capacity dashboards.
- Virtualization: Proxmox, NixOS hosts, immutable/reproducible rebuilds, VM snapshots.
- Security: segmentation, management-plane isolation, patching, vulnerability feeds, service exposure review.

## Engineering Notes

- Restore tests are more important than backup volume count.
- Management interfaces belong on restricted networks.
- Remote access should fail closed but preserve a recovery path.
- Keep the "source of truth" explicit: Nix configs, inventory notes, DNS records, firewall rules, and secrets metadata should agree.

## Sources

- NIST SP 800-207 - Zero Trust Architecture - https://csrc.nist.gov/pubs/sp/800/207/final
- Kubernetes docs - Pod Security Standards - https://kubernetes.io/docs/concepts/security/pod-security-standards/
- Google SRE Book - Monitoring Distributed Systems - https://sre.google/sre-book/monitoring-distributed-systems/
- Google SRE Book - Postmortem Culture - https://sre.google/sre-book/postmortem-culture/

## Related

- [Network Map](kb://01-maps-network-map)
- [Observability Map](kb://01-maps-observability-map)
- [Homelab Roadmap](kb://08-improvements-homelab-roadmap)
