---
summary: "Track unfinished network work across routing, firewalling, DNS, remote access, and documentation."
status: in-progress
tags: [improvements]
---

## Purpose

Track unfinished network work across routing, firewalling, DNS, remote access, and documentation.

## Current State

- `pfSense Router` and `Firewall - pfSense` exist as baseline notes.
- [[05 Network/Physical Topology|Physical Topology]] now records the known physical links, switches, hosts, and Proxmox guests.
- [[05 Network/Host & IP Inventory|Host & IP Inventory]] is the canonical address inventory.
- The pfSense documentation is currently based on a status snapshot, not interface/rule exports.

## Tasks

- [x] Create `05 Network/WireGuard.md` or remove the placeholder link from `Network Map` — resolved: WireGuard is documented in [[05 Network/WireGuard - Road Warrior|WireGuard - Road Warrior]]; no separate note needed
- [x] Create `05 Network/Tailscale.md` or remove the placeholder link from `Network Map` — resolved: Tailscale is not in use, placeholder removed
- [x] Create `05 Network/DNS.md` or remove the placeholder link from `Network Map`
- [x] Create `05 Network/VLANs.md` or remove the placeholder link from `Network Map`
- [x] Create `05 Network/Routing.md` or remove the placeholder link from `Network Map`
- [x] Create `05 Network/SSH Access.md` or remove the placeholder link from `Network Map`
- [x] Create `05 Network/Remote Recovery.md` or remove the placeholder link from `Network Map`
- [ ] Record the exact Netgear and Cisco switch port numbers; pfSense `igb0`/`igb1` to switch-model mapping is documented
- [ ] Document pfSense firewall rule intent for `WAN`, `LAN`, `OPT1`, `MGMT`, and `OPT3`
- [ ] Document pfSense NAT and port forward inventory
- [ ] Document pfSense DHCP scopes and static leases
- [x] Document whether `OPT1` and `OPT3` correspond to VLAN-backed segments or physically separate interfaces — resolved: no VLANs. `LAN` and `OPT1` are physically separate `1000baseT` ports, `OPT3` is the OpenVPN tunnel. See [[05 Network/VLANs|VLANs]].
- [ ] Host technitium-dns on mitm (use 127.0.0.1 as the local dns reciever), set `mitm`
  as the main technitium node, and cluster `nixos` to it, and adjust Documentation

## Related

- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[01 Maps/Network Map|Network Map]]
- [[Firewall - pfSense|Firewall - pfSense]]
- [[05 Network/DNS|DNS]]
- [[02 Systems/NixOS - Host mitm|Host mitm]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[08 Improvements/Homelab Roadmap|Homelab Roadmap]]
