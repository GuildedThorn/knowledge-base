---
summary: Mac Pro 5,1 NixOS and Proxmox hypervisor hosting the websites and SOC virtual machines on ThornCloud OPT1.
status: active
tags: [devices]
---

## Purpose

NixOS and Proxmox VE hypervisor for ThornCloud services.

## Identity

- NixOS hostname: `mac`
- Network identity: see [[05 Network/Host & IP Inventory|Host & IP Inventory]]
- Operating system: NixOS with Proxmox VE enabled

## Hardware Specs

- CPU: `2x Intel Xeon X5690`
- GPU: `AMD Radeon RX 580 8 GB`
- Memory: `128 GB DDR3 ECC @ 1333 MHz`
- Storage: `1 TB Samsung 870 Evo`

## Network

- Connected to the physical OPT1 network through the Cisco Catalyst 3560G.
- `enp9s0` is attached to `vmbr0`; `vmbr0` carries the host management address and guest traffic.
- `enp10s0` is unused.
- `vmbr1` and `vmbr2` are empty bridges.
- There are no VLANs and pfSense is a separate physical router, not a VM on this host.

## Hosted Workloads

- `websites` — production GuildedThorn.com VM
- `soc` — SIEM and observability VM

## Related

- [[01 Maps/Devices Map|Devices Map]]
- [[05 Network/Physical Topology|Physical Topology]]
- [[05 Network/Host & IP Inventory|Host & IP Inventory]]
- [[09 Observability/SIEM and SOC - Architecture|SIEM and SOC - Architecture]]
