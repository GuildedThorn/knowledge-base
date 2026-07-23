---
summary: Document how the network is segmented in ThornCloud.
status: active
tags: [network]
---

## Purpose

Document how the network is segmented in ThornCloud. Short version: **there are no VLANs.** Segmentation is done with physically separate interfaces on the pfSense router, each carrying its own flat `/24` — not 802.1Q tagging, trunks, or access ports.

## Segments

Two internal LAN subnets, each on its own physical port of the Netgate XG-2758 (see [[03 Devices/pfSense Router|pfSense Router]]):

| Interface | Subnet | Gateway | Media |
|---|---|---|---|
| `LAN` | `192.168.1.0/24` | `192.168.1.1` | `1000baseT` |
| `OPT1` | `172.16.25.0/24` | `172.16.25.1` | `1000baseT` |

The only other routed internal address is the remote-access tunnel — a VPN subnet, not a LAN segment:

| Interface | Subnet | Gateway | Notes |
|---|---|---|---|
| `OPT3` | `10.0.8.0/24` | `10.0.8.1` | OpenVPN (`ThornVPN` / ThornCloud Private Network, UDP 1194) |

`WAN` is `64.53.182.82` (10Gbase-SR). A `MGMT` interface exists on the box but is currently unassigned.

## Why there are no VLANs

- Each subnet lands on its own physical `1000baseT` port. Nothing is tagged, so there are no trunk/access ports and no inter-VLAN routing.
- Traffic between `192.168.1.0/24` and `172.16.25.0/24` is plain **inter-subnet routing** through pfSense, controlled by per-interface firewall rules — see [[Firewall - pfSense|Firewall - pfSense]] and [[Routing|Routing]].
- If VLANs are ever introduced (e.g. to carve out an isolated segment without adding physical ports — the isolation the [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]] wants), record the VLAN IDs, trunk ports, and tagging here at that point.

## Known hosts by subnet

- **`192.168.1.0/24` (LAN):** pfSense `.1`, pfSense management `.74`, `mac` host placeholder `.2` (TODO, not yet deployed).
- **`172.16.25.0/24` (OPT1):** pfSense gateway `.1`, `mitm`/LAN reference `.2`, TrueNAS `.4`, `soc` `.51`, plus the `websites` host.

## To reconcile

- The `proxmox` hypervisor's `systemd-networkd` config carries `vlan10`/`vlan30` interface names bridged into `vmbr0`/`vmbr1` (see [[03 Devices/Mac Pro 5,1|Mac Pro 5,1]]). These are **host-local names only** and do not reflect any 802.1Q VLAN segmentation on the network. Rename or remove them so they stop implying VLANs that don't exist.

## Related

- [[01 Maps/Network Map|Network Map]]
- [[Routing|Routing]]
- [[03 Devices/pfSense Router|pfSense Router]]
- [[Firewall - pfSense|Firewall - pfSense]]
