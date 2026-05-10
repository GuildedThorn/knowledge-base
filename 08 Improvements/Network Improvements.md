## Purpose

Track unfinished network work across routing, firewalling, DNS, remote access, and documentation.

## Current State

- `pfSense Router` and `Firewall - pfSense` now exist as baseline notes.
- `Network Map` still links to several notes that do not exist yet.
- The pfSense documentation is currently based on a status snapshot, not interface/rule exports.

## Tasks

- [ ] Create `05 Network/WireGuard.md` or remove the placeholder link from `Network Map`
- [ ] Create `05 Network/Tailscale.md` or remove the placeholder link from `Network Map`
- [x] Create `05 Network/DNS.md` or remove the placeholder link from `Network Map`
- [x] Create `05 Network/VLANs.md` or remove the placeholder link from `Network Map`
- [x] Create `05 Network/Routing.md` or remove the placeholder link from `Network Map`
- [x] Create `05 Network/SSH Access.md` or remove the placeholder link from `Network Map`
- [x] Create `05 Network/Remote Recovery.md` or remove the placeholder link from `Network Map`
- [ ] Document pfSense interface-to-switch-port mapping
- [ ] Document pfSense firewall rule intent for `WAN`, `LAN`, `OPT1`, `MGMT`, and `OPT3`
- [ ] Document pfSense NAT and port forward inventory
- [ ] Document pfSense DHCP scopes and static leases
- [ ] Document whether `OPT1` and `OPT3` correspond to VLAN-backed segments or physically separate interfaces
- [ ] Host technitium-dns on mitm (use 127.0.0.1 as the local dns reciever), set `mitm`
  as the main technitium node, and cluster `nixos` to it, and adjust Documentation

## Related

- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[01 Maps/Network Map|Network Map]]
- [[Firewall - pfSense|Firewall - pfSense]]
