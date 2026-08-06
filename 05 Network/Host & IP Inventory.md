---
summary: Single source of truth for ThornCloud subnets, pfSense interfaces, host IPs, and service endpoints.
status: active
tags: [network, reference]
---

## Purpose

The **canonical** list of subnets, interfaces, host IPs, and endpoints for ThornCloud. When an address changes, change it *here* — other notes should link to this rather than restate IPs. See [[05 Network/Physical Topology|Physical Topology]] for connections and [[05 Network/VLANs|VLANs]] for why segmentation is subnet-based.

## Subnets

| CIDR | Segment | pfSense interface | Gateway |
|---|---|---|---|
| `192.168.1.0/24` | Main LAN | `LAN` (physical `1000baseT`) | `192.168.1.1` |
| `172.16.25.0/24` | Internal / services | `OPT1` (physical `1000baseT`) | `172.16.25.1` |
| `10.0.8.0/24` | OpenVPN (`ThornVPN`) | `OPT3` | `10.0.8.1` |
| `10.10.10.0/24` | WireGuard road-warrior | (tunnel) | `10.10.10.1` (pfSense) |

## pfSense edge (`pfsense.guildedthorn.arpa`, Netgate XG-2758)

| Interface | Address | Media / notes |
|---|---|---|
| `WAN` | `64.53.182.82` | `10Gbase-SR` |
| `LAN` | `192.168.1.1` | `igb0`; Netgear GS308E; flat, untagged LAN |
| `OPT1` | `172.16.25.1` | `igb1`; Cisco Catalyst 3560G; flat, untagged services network |
| `OPT3` | `10.0.8.1` | OpenVPN `ThornCloud Private Network`, UDP 1194 |
| `MGMT` | (unassigned) | interface exists, no address |
| Management UI | `192.168.1.74` | web UI / SSH |
| WireGuard | `WAN:4501` | road-warrior endpoint; tunnel `10.10.10.0/24`, DNS `10.10.10.1` |

Details: [[03 Devices/pfSense Router|pfSense Router]] · [[05 Network/Firewall - pfSense|Firewall - pfSense]] · [[05 Network/WireGuard - Road Warrior|WireGuard - Road Warrior]].

## Hosts

| Host | `.arpa` | IP | Subnet | Role |
|---|---|---|---|---|
| pfSense | `pfsense` | `192.168.1.1` / `.74` / `172.16.25.1` | edge | Router / firewall / VPN — see above |
| nixos | — | `192.168.1.6` | LAN | Main NixOS workstation. [[02 Systems/NixOS - Host nixos\|Host nixos]] |
| mac / Proxmox | `proxmox` | `172.16.25.3` | OPT1 | Mac Pro 5,1 hypervisor hosting `websites` and `soc`. [[03 Devices/Mac Pro 5,1\|Mac Pro 5,1]] |
| websites | `websites` | `172.16.25.50` | OPT1 | Public web VM (Cloudflare tunnel); Suricata sensor. [[02 Systems/NixOS - Host websites\|Host websites]] |
| soc | `soc` | `172.16.25.51/24` | OPT1 | SIEM/SOC VM — Loki/Prometheus/Grafana. [[02 Systems/NixOS - Host soc\|Host soc]] |
| mitm | `mitm` | `172.16.25.2` | OPT1 | Inline proxy / SearXNG host; referenced as `websites`' upstream gateway + DNS (role slightly ambiguous — confirm). [[02 Systems/NixOS - Host mitm\|Host mitm]] |
| TrueNAS | `truenas` | `172.16.25.4` | OPT1 | NAS — CIFS media, SeaweedFS S3 (Loki/backups), Jellyfin `:8920`. [[03 Devices/TrueNAS\|TrueNAS]] |
| scout | — | `10.10.10.3/32` (WireGuard) | VPN | Roaming laptop. [[02 Systems/NixOS - Host scout\|Host scout]] |

## Physical distribution

| Segment | pfSense interface | Distribution | Confirmed downstream systems |
|---|---|---|---|
| LAN | `igb0` | Netgear GS308E | `nixos` |
| OPT1 | `igb1` | Cisco Catalyst 3560G | Mac/Proxmox, TrueNAS; Proxmox guests `websites` and `soc` |

There are no VLANs. Exact switch port numbers and switch management addresses are not yet documented.

## Service endpoints

- Grafana (SOC): `https://soc.guildedthorn.arpa:3000`
- Loki: `:3100` (soc) · Prometheus: `:9090` (soc) · syslog ingest: `soc:5514` (UDP)
- Jellyfin: `https://truenas.guildedthorn.arpa:8920`
- SeaweedFS S3: `truenas.guildedthorn.arpa:30304` (bucket `loki`, HTTPS / ThornCloud CA)
- SearXNG: `https://mitm.guildedthorn.arpa/searxng/`

## DNS resolvers

- Primary `1.1.1.1`; `8.8.8.8` also referenced; `1.1.1.1` as fallback on several hosts. Internal `.arpa` names are largely pinned via static `extraHosts` overrides rather than a running internal DNS server (see [[05 Network/DNS|DNS]]).

## Related

- [[01 Maps/Network Map|Network Map]]
- [[05 Network/Physical Topology|Physical Topology]]
- [[05 Network/Routing|Routing]]
- [[05 Network/VLANs|VLANs]]
- [[03 Devices/pfSense Router|pfSense Router]]
- [[03 Devices/TrueNAS|TrueNAS]]
