## Purpose

Document VLAN usage, trunks, access ports, and which network segments map to which interfaces in ThornCloud.

## Current Known State

- An undocumented host (likely the `proxmox` hypervisor — see [[03 Devices/Mac Pro 5,1|Mac Pro 5,1]]) uses `systemd-networkd` with:
  - `vlan10`
  - `vlan30`
  - bridges `vmbr0` and `vmbr1`
- `vlan10` is attached to `enp42s0`.
- `vlan30` is attached to `enp45s0f3u4u3i5`.
- `vlan30` is bridged into `vmbr0`.
- On pfSense, internal routed interfaces currently visible are:
  - `LAN` at `192.168.1.1`
  - `OPT1` at `172.16.25.1`
  - `OPT3` at `10.0.8.1`

## What Is Still Unclear

- Which pfSense interfaces are VLAN-backed versus physically separate interfaces
- Which switch ports are trunks versus access ports
- Whether `OPT1` and `OPT3` correspond to the same VLAN IDs seen on the host above
- Which device groups live on each segment
- Confirming which physical host actually owns the `vlan10`/`vlan30`/`vmbr0`/`vmbr1` config described above

## Tasks

- [ ] Map VLAN IDs to subnets and interface names
- [ ] Record trunk ports and the switches they land on
- [ ] Record access ports and expected endpoint types
- [ ] Link VLANs to firewall policy and inter-VLAN routing rules
- [ ] Identify or carve out an isolated segment for purple-team exercise targets, needed before [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]] can start its network-visibility and attack-simulation phases

## Related

- [[01 Maps/Network Map|Network Map]]
- [[Routing|Routing]]
- [[03 Devices/pfSense Router|pfSense Router]]
