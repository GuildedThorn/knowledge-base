## Purpose

Development and staging/testing host.

## Identity

## Production
- Hostname: `proxmox`
- OS: `Proxmox 9.1.4`

## Development
 - Hostname: proxmox
 - OS: `nixOS 26.05`
## Hardware Specs

- CPU: `2x Intel Xeon X5690`
- GPU: `AMD Radeon RX 580 8 GB`
- Memory: `128 GB DDR3 ECC @ 1333 MHz`
- Storage: `1 TB Samsung 870 Evo`

Proxmox Specific Notes
- Have development, and production tags
- WAN is tied to enp9s0, LAN, And OPT1 are all private interfaces bound to pfsense vm

## Things of note

TODO:

 - [ ] Seperate pfsense firewall for development and production

## Related

- [[01 Maps/Devices Map|Devices Map]]
- [[90 Templates/Setup Note Template|Setup Note Template]]
- [[09 Observability/SIEM and SOC - Planned Architecture|SIEM and SOC - Planned Architecture]] (proposed host for the planned Kali Purple VM)
