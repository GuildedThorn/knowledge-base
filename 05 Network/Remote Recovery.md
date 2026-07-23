---
summary: "Document how to recover access to ThornCloud systems when normal desktop, web, or service access breaks."
status: active
tags: [network]
---

## Purpose

Document how to recover access to ThornCloud systems when normal desktop, web, or service access breaks.

## Recovery Paths To Track

- VPN access through pfSense OpenVPN
- SSH access to NixOS hosts
- serial console access for systems that support it
- direct pfSense management access
- local console fallback on workstation and laptop systems

## Current Known State

- pfSense exposes an OpenVPN service named `ThornCloud Private Network` on `UDP4:1194`.
- The vault already has `Serial Console Setup`.
- Multiple NixOS hosts import the shared SSH module.
- The `scout` laptop and `nixos` workstation both have enough tooling to act as admin machines.

## Tasks

- [ ] Define the preferred remote recovery path for each major system
- [ ] Document what to do if pfSense is up but downstream services are not
- [ ] Document what to do if pfSense itself is unreachable
- [ ] Document which systems have serial-console-capable recovery paths
- [ ] Document minimum travel or on-site kit needed for recovery work

## Related

- [[01 Maps/Network Map|Network Map]]
- [[SSH Access|SSH Access]]
- [[Serial Console Setup|Serial Console Setup]]
- [[03 Devices/pfSense Router|pfSense Router]]
