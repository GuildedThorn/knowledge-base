---
summary: "Document SSH entry points, agent behavior, key handling, and which systems are intended to be reachable over SSH."
status: active
tags: [network]
---

## Purpose

Document SSH entry points, agent behavior, key handling, and which systems are intended to be reachable over SSH.

## Current Known State

- Shared NixOS service module `services/ssh.nix` enables `programs.ssh.startAgent = true`.
- The `mitm`, `vmware-test`, `scout`, and `nixos` hosts all import the shared SSH service module.
- The pfSense status snapshot shows `22` open on `WAN` and internal interfaces in the visible firewall snapshot, but the exact intent is not yet documented.

## Questions To Resolve

- Which hosts should be reachable only internally versus through VPN
- Whether SSH is intentionally exposed on pfSense `WAN` or just logged traffic around that port
- Which keys, certificates, or smartcards are used for admin access
- Whether bastion-style access exists or should exist

## Tasks

- [ ] Document approved SSH targets and their access paths
- [ ] Document admin key locations and smartcard usage
- [ ] Document whether SSH should be reachable only over VPN for remote admin
- [ ] Document recovery SSH strategy if primary desktop access fails

## Related

- [[01 Maps/Network Map|Network Map]]
- [[Remote Recovery|Remote Recovery]]
- [[02 Systems/NixOS - Shared Modules|NixOS - Shared Modules]]
- [[03 Devices/pfSense Router|pfSense Router]]
