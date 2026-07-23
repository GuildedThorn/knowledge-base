---
summary: "Primary edge router and firewall for ThornCloud, handling WAN connectivity, internal network segmentation, firewalling, and OpenVPN access."
status: active
tags: [devices]
---

## Purpose

Primary edge router and firewall for ThornCloud, handling WAN connectivity, internal network segmentation, firewalling, and OpenVPN access.

## Identity

- Hostname: `pfsense.guildedthorn.arpa`
- Management IP: `192.168.1.74`
- LAN IP: `192.168.1.1`
- Platform: `Netgate XG-2758`
- Serial: `0908161085`
- Netgate Device ID: `ea008528ef5a76897829`
- OS: `pfSense Plus 26.03-RELEASE (amd64)`
- Base OS: `FreeBSD 16.0-CURRENT`
- Build date: `Wednesday, April 1, 2026 12:20:00 CDT`

## Hardware Specs

- CPU: `Intel Atom C2758 @ 2.40 GHz`
- Core count: `8 CPUs`
- Memory: `16325 MiB`
- Swap: `32767 MiB`
- Disk: `77 GB` root volume
- Boot method: `BIOS`
- BIOS vendor: `coreboot`
- BIOS version: `ADI_RCC-01.00.00.09-16M-nodebug`
- BIOS release date: `Friday, February 12, 2016`

## Crypto and Security Features

- AES-NI: active
- IPsec-MB: active
- QAT: inactive
- Hardware crypto: `AES-CBC`, `AES-CCM`, `AES-GCM`, `AES-ICM`, `AES-XTS`, `ChaCha20-Poly1305`
- Kernel PTI: enabled
- MDS mitigation: inactive

## Interfaces

- `WAN`: `64.53.182.82` on `10Gbase-SR`
- `LAN`: `192.168.1.1` on `1000baseT`
- `OPT1`: `172.16.25.1` on `1000baseT`
- `MGMT`: N/A
- `OPT3`: `10.0.8.1` on `ThornVPN`

## Network and Firewall Notes

- Primary DNS resolver is set to `1.1.1.1`.
- The firewall is actively logging blocked traffic on `WAN`, `LAN`, and `MGMT`.
- Recent blocked traffic includes multicast discovery traffic, broadcast traffic from the management network, and unsolicited WAN traffic.
- State table usage at capture time was `213 / 1632000`, effectively idle.

## Services and VPN

- OpenVPN server shown: `ThornCloud Private Network` on `UDP4:1194`
- Connected clients at capture time: `0`
- Dynamic DNS entries were hidden in the pasted status view.
- No Suricata alerts were shown in the pasted status view.
- No captive portal sessions were shown in the pasted status view.

## Status Snapshot

- Latest version status: up to date
- Version info last updated: `Tuesday, April 28, 2026 14:56:48 CDT`
- Uptime: `13 days, 23 hours, 53 minutes, 45 seconds`
- Snapshot time: `Tuesday, April 28, 2026 15:43:05 CDT`
- Last config change: `Tuesday, April 14, 2026 15:57:08 CDT`
- Memory usage: `13%`
- Swap usage: `0%`
- Root filesystem usage: `4% of 77 GB`
- Temperature: approximately `46-48 C` across all CPU sensors
- Load average: `0.34, 0.14, 0.10`

## Operational Notes

- The router appears lightly loaded based on memory, swap, state table, and disk usage.
- `MGMT` is present as a separate interface, which suggests the box is being used with at least some network separation beyond simple WAN/LAN.
- `OPT1` at `172.16.25.1` and `OPT3` at `10.0.8.1` indicate multiple internal routed segments.
- Because this is the edge firewall, interface assignments, rules, NAT, DHCP, and VPN changes should be documented here as they evolve.

## Follow-Up Documentation To Add

- interface-to-switch-port mapping
- firewall rule intent by interface
- DHCP scopes and static mappings
- NAT and port forward inventory
- OpenVPN client/server details
- backup and restore procedure

## Related

- [[01 Maps/Devices Map|Devices Map]]
- [[01 Maps/Network Map|Network Map]]
- [[Firewall - pfSense|Firewall - pfSense]]
