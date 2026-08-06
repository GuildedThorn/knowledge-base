---
summary: Document how the network is segmented in ThornCloud.
status: active
tags: [network]
---

## Purpose

Document how the network is segmented in ThornCloud. Short version: **there are no VLANs.** Segmentation is done with physically separate interfaces on the pfSense router, each carrying its own flat network — not 802.1Q tagging, trunks, or access ports.

## Segments

Two internal Ethernet segments, each on its own physical port of the Netgate XG-2758 (see [[03 Devices/pfSense Router|pfSense Router]]):

| Interface | Physical NIC | Distribution | Purpose |
|---|---|---|---|
| `LAN` | `igb0` | Netgear GS308E | Main workstation LAN |
| `OPT1` | `igb1` | Cisco Catalyst 3560G | Servers, storage, and virtualization |

`OPT3` is an OpenVPN tunnel, not an Ethernet segment or VLAN. Canonical addresses are in [[05 Network/Host & IP Inventory|Host & IP Inventory]].

## Why there are no VLANs

- Each subnet lands on its own physical Ethernet port. Nothing is tagged, so there are no trunk/access ports and no inter-VLAN routing.
- Traffic between LAN and OPT1 is plain **inter-subnet routing** through pfSense, controlled by per-interface firewall rules — see [[Firewall - pfSense|Firewall - pfSense]] and [[Routing|Routing]].
- If VLANs are ever introduced (e.g. to carve out an isolated segment without adding physical ports — the isolation the [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]] wants), record the VLAN IDs, trunk ports, and tagging here at that point.

## Proxmox Bridge Names

- `vmbr0`, `vmbr1`, and `vmbr2` on Mac are Linux bridge names, not VLANs.
- `vmbr0` contains the active `enp9s0` OPT1 uplink.
- `vmbr1` and `vmbr2` are currently empty; `enp10s0` is unused.

## Related

- [[01 Maps/Network Map|Network Map]]
- [[05 Network/Physical Topology|Physical Topology]]
- [[05 Network/Host & IP Inventory|Host & IP Inventory]]
- [[Routing|Routing]]
- [[03 Devices/pfSense Router|pfSense Router]]
- [[Firewall - pfSense|Firewall - pfSense]]
