---
summary: "Service host for NGINX reverse proxying, internal web services, DNS, and supporting network infrastructure workloads."
status: active
tags: [devices]
---

## Purpose

Service host for NGINX reverse proxying, internal web services, DNS, and supporting network infrastructure workloads.

## Identity

- Hostname: `mitm`
- OS: `NixOS 26.06`
- Config path: `~/Documents/ThornixOS` (`modules/computers/mitm.nix` + `hosts/mitm/`)

## Hardware Specs

- CPU: `Intel Core i3-8100`
- GPU: `Intel UHD Graphics`
- Memory: `16 GB DDR4 @ 2133 MHz`
- Storage: `256 GB Samsung 870 Evo`

## NixOS-Specific Notes

- Uses the `mitm` host under the `thorn` user tree.
- Has NetworkManager disabled.
- Uses DNS `1.1.1.1`.
- Opens TCP and UDP ports `22`, `53`, `80`, and `443`.
- Imports shared NixOS service modules for Bluetooth, ClamAV, and SSH.

## Hosted Services

Currently Installed:
- `NGINX` reverse proxy
- `SearXNG` configuration exists, but the service is currently disabled
- a commented-out `MongoDB` block exists but is not active

Note: Technitium DNS and a locally-proxied Grafana instance were part of an earlier config pass and no longer appear in the current `mitm` module. (The `proxmox-mitm` VM variant that briefly carried a disabled Grafana was removed from the repo; the live Grafana is now on `soc` — see [[09 Observability/Grafana|Grafana]].)

## Reverse Proxy Notes

- `guildedthorn.com` proxies to `https://proxmox.guildedthorn.arpa:5000`
- `radio.guildedthorn.com` proxies to `https://proxmox.guildedthorn.arpa:5001`
- `searxng.guildedthorn.arpa` is wired for local UWSGI socket proxying (SearXNG itself disabled)

## Role Notes

- This machine currently acts as one of the core internal service hosts in ThornCloud.
- It is a better fit for centralized service hosting than end-user workstation tasks.
- The note in your original draft about Home Assistant BLE and possibly offloading OpenVPN still belongs as future/planned scope rather than current state, since that is not present in the inspected `mitm` host config.

## Related

- [[01 Maps/Devices Map|Devices Map]]
- [[02 Systems/NixOS - Host mitm|NixOS - Host mitm]]
- [[DNS|DNS]]
- [[Firewall - pfSense|Firewall - pfSense]]
- [[Grafana]]
- [[90 Templates/Setup Note Template|Setup Note Template]]
