---
summary: "Provide a single summary of the host inventory in `ThornixOS` (`~/Documents/ThornixOS`, GitHub `GuildedThorn/ThornixOS`)."
status: active
tags: [systems, host]
---

## Purpose

Provide a single summary of the host inventory in `ThornixOS` (`~/Documents/ThornixOS`, GitHub `GuildedThorn/ThornixOS`).

## Thorn Hosts

- `nixos`: AMD-based main workstation with Hyprland, `glance` dashboard, local DNS, CIFS media mount, Docker (Podman replaced by Docker), gaming/creative/dev tooling, printing, OpenRGB, U2F for sudo/login, and SDR/VR/DisplayLink/fingerprint/tablet services (VMware host support was dropped — the package broke in the current nixpkgs pin).
- `scout`: Intel-based ThinkPad laptop with Hyprland, `glance`, secure boot via `lanzaboote`, ThinkPad fan/thermal tuning, TLP battery charge thresholds, U2F, and a desktop-heavy daily-driver software stack.
- `mac`: Intel CPU / AMD graphics machine, Hyprland desktop, Proxmox VE service enabled — currently has a placeholder LAN IP pending real deployment.
- `websites`: Proxmox VM serving [[GuildedThorn.com - Overview|GuildedThorn.com]] via the `guildedthorn-com` flake input's NixOS module, fronted by a Cloudflare Tunnel (only SSH exposed publicly otherwise), plus Owncast for the live stream, RabbitMQ for the guestbook publisher, and the fleet's host-level Suricata IDS sensor.
- `soc`: headless Proxmox VM running the SIEM — Loki (chunks on TrueNAS S3), Prometheus, and Grafana with Discord alerting; the whole fleet ships logs and metrics here. See [[02 Systems/NixOS - Host soc|Host soc]].
- `firewall`: minimal dedicated firewall box — SSH only, NetworkManager disabled, DNS `1.1.1.1`.
- `mitm`: bare-metal service host whose NGINX now fronts only a still-disabled SearXNG vhost — the `guildedthorn.com`/`radio.guildedthorn.com` reverse-proxy vhosts were pruned, and the `proxmox-mitm` VM variant was removed from the repo entirely.
- `proxmox-guest`: general-purpose Proxmox VM, XFCE+i3 desktop, `glance` dashboard, trusts the internal Proxmox cert from `certs/`.
- `vmware-test` / `vmware-guest`: lighter XFCE+i3 VMware VMs with audio, ClamAV, and SSH; `vmware-guest` additionally has a host-specific Home Manager overlay.

## Shared Patterns

- IPv6 is disabled on every inspected host.
- Host networking is split into separate `hosts/<host>/networking.nix` files.
- Host configs import reusable desktop, graphics, processor, and service modules rather than duplicating large option blocks (see [[02 Systems/NixOS - Shared Modules|Shared Modules]]).
- Deployment is GitOps via `comin`, not manual per-host rebuilds — see [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]].

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[02 Systems/NixOS - Host scout|Host scout]]
- [[02 Systems/NixOS - Host mac|Host mac]]
- [[02 Systems/NixOS - Host websites|Host websites]]
- [[02 Systems/NixOS - Host soc|Host soc]]
- [[02 Systems/NixOS - Host firewall|Host firewall]]
- [[02 Systems/NixOS - Host mitm|Host mitm]]
- [[02 Systems/NixOS - Host proxmox-guest|Host proxmox-guest]]
- [[02 Systems/NixOS - Host vmware-test|Host vmware-test]]
- [[02 Systems/NixOS - Host vmware-guest|Host vmware-guest]]
