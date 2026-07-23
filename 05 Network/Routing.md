---
summary: "Document how traffic moves between WAN, LAN, internal subnets, VPN clients, and special-purpose hosts."
status: active
tags: [network]
---

## Purpose

Document how traffic moves between WAN, LAN, internal subnets, VPN clients, and special-purpose hosts. (No VLANs — segmentation is by separate physical interfaces; see [[VLANs|VLANs]].)

## Current Known State

- The pfSense router is the primary edge router and firewall.
- Known internal gateway addresses from pfSense are:
  - `192.168.1.1`
  - `172.16.25.1`
  - `10.0.8.1`
- The `mitm` and `nixos` hosts both expose internal services that likely depend on routed access between segments.

## Routing Questions

- Which subnet is the main user LAN?
- Which subnet is management-only?
- Which subnet is lab, services, guest, or VPN-only?
- Is pfSense the only router, or do any hosts perform additional routed segmentation?

## Tasks

- [ ] Map subnets to purpose and trust level
- [ ] Document default routes and any static routes
- [ ] Document whether VPN clients are routed into all internal networks or only selected ones
- [ ] Document how inter-subnet access (between `192.168.1.0/24` and `172.16.25.0/24`) is controlled

## Related

- [[01 Maps/Network Map|Network Map]]
- [[VLANs|VLANs]]
- [[Firewall - pfSense|Firewall - pfSense]]
- [[03 Devices/pfSense Router|pfSense Router]]
