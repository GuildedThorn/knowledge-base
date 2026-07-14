## Purpose

Document DNS design, upstream resolvers, local DNS services, and host-specific resolution behavior across ThornCloud.

## Current Known State

- `pfSense Router` is configured with `1.1.1.1` as a DNS server in the captured `April 28, 2026` status snapshot.
- The `nixos` workstation, `scout` laptop, `mitm`, `firewall`, `mac`, and `proxmox-guest` hosts in `ThornixOS` all use `1.1.1.1` as `networking.nameservers` directly — there is no local DNS resolver/server role (Technitium) anywhere in the current repo, which corrects an earlier version of this note.
- `nixos` additionally defines static `extraHosts` entries for `pfsense.guildedthorn.arpa`, `proxmox.guildedthorn.arpa`, and `truenas.guildedthorn.arpa` rather than resolving them via a DNS server.
- `websites` uses its upstream gateway (`172.16.25.2`) plus `1.1.1.1` as a fallback, with a similar single static-host override for `truenas.guildedthorn.arpa` (needed for a TLS cert match).
- `proxmox-mitm` uses `8.8.8.8` instead of `1.1.1.1` — the one host that differs.

## Known DNS Consumers

- `pfSense Router`
- `nixos`, `scout`, `mitm`, `mac`, `firewall`, `proxmox-guest`, `websites` (all via `1.1.1.1`)
- `proxmox-mitm` (via `8.8.8.8`)

## Planned

[[08 Improvements/Network Improvements|Network Improvements]] already tracks a concrete plan here: host Technitium DNS on `mitm` (as the main node, `127.0.0.1` as the local receiver) and cluster `nixos` to it. That would replace the scattered static `extraHosts` approach with an actual internal DNS server — this note's "no local resolver exists" finding is the current-state baseline that plan is meant to change.

## Questions To Resolve

- Is pfSense acting only as a gateway, or also as a DNS forwarder/resolver for clients?
- Which host is authoritative for internal `guildedthorn.arpa` names, given resolution is currently done via scattered static `extraHosts` entries rather than a central internal DNS server?
- Why does `proxmox-mitm` use a different upstream resolver (`8.8.8.8`) than every other host?
- Which systems should use local DNS versus public upstream DNS directly?

## Tasks

- [ ] Document whether pfSense provides DNS forwarding or DHCP-advertised DNS to clients
- [ ] Document which host owns internal zone data
- [ ] Document DNS behavior for VPN clients
- [ ] Document split between public DNS, internal DNS, and static host overrides

## Related

- [[01 Maps/Network Map|Network Map]]
- [[03 Devices/pfSense Router|pfSense Router]]
- [[02 Systems/NixOS - Host nixos|NixOS - Host nixos]]
- [[02 Systems/NixOS - Host mitm|NixOS - Host mitm]]
- [[02 Systems/NixOS - Host scout|NixOS - Host scout]]
- [[08 Improvements/Network Improvements|Network Improvements]]
