---
summary: "Document how traffic moves between WAN, LAN, internal subnets, VPN clients, and special-purpose hosts."
status: active
tags: [network]
---

## Purpose

Document how traffic moves between WAN, LAN, internal subnets, VPN clients, and special-purpose hosts. (No VLANs — segmentation is by separate physical interfaces; see [[VLANs|VLANs]].)

## Current Known State

- pfSense is the primary edge router and the only confirmed router between physical internal segments.
- LAN is the main workstation segment, distributed from pfSense `igb0` through the Netgear GS308E.
- OPT1 is the services and virtualization segment, distributed from pfSense `igb1` through the Cisco Catalyst 3560G.
- Mac/Proxmox and TrueNAS attach directly to OPT1. The `websites` and `soc` guests are hosted by Mac and use OPT1 addressing.
- OpenVPN and WireGuard provide separate remote-access tunnel networks.
- Canonical interface, subnet, gateway, and host addresses are in [[05 Network/Host & IP Inventory|Host & IP Inventory]].

## Forwarding Behavior

- LAN and OPT1 are physically separate, flat Layer 2 networks; there is no 802.1Q tagging.
- Traffic between LAN and OPT1 must traverse pfSense and is subject to the rule set on the interface where it enters.
- Same-subnet traffic is switched directly and does not traverse pfSense.
- Traffic between the `websites` and `soc` VMs may be switched internally by Proxmox without reaching the Cisco switch.
- Internet-bound traffic uses pfSense as the default gateway and exits WAN.

## Questions To Resolve

- [ ] Document default routes and any static routes
- [ ] Document whether VPN clients are routed into all internal networks or only selected ones
- [ ] Document how inter-subnet access (between `192.168.1.0/24` and `172.16.25.0/24`) is controlled
- [ ] Confirm whether `mitm` performs any additional routing or is only an application proxy

## Related

- [[01 Maps/Network Map|Network Map]]
- [[05 Network/Physical Topology|Physical Topology]]
- [[05 Network/Host & IP Inventory|Host & IP Inventory]]
- [[VLANs|VLANs]]
- [[Firewall - pfSense|Firewall - pfSense]]
- [[03 Devices/pfSense Router|pfSense Router]]
