---
summary: "Primary workstation for software development, VMware-based development VMs, finance, gaming, and general desktop use."
status: active
tags: [devices]
---

## Purpose

Primary workstation for software development, VMware-based development VMs, finance, gaming, and general desktop use.

## Identity

- Hostname: `nixos`
- OS: `NixOS 26.06`
- Config path: `~/Documents/ThornixOS` (`modules/computers/nixos.nix` + `hosts/nixos/`)

## Hardware Specs

- CPU: `Ryzen 9 5900X`
- GPU: `RX 6700XT 2x Mech OC`
- Memory: `32 GB DDR4 @ 3200 MHz`
- Storage: `2 TB Samsung 980 Evo`

## NixOS-Specific Notes

- Uses the `nixos` host under the `thorn` user tree.
- Runs Hyprland with a host-specific multi-monitor layout.
- Uses AMD processor and graphics modules.
- Uses external DNS `1.1.1.1`, with local `extraHosts` entries for `pfsense`/`proxmox`/`truenas` `.guildedthorn.arpa`. NetworkManager is enabled (kept for Wi-Fi/VPN use) — there is no local Technitium/DNS-server role on this host anymore.
- Mounts the media share at `/mnt/media` from `//172.16.25.4/media`.
- Enables Docker (`virtualisation.docker`) — Podman/Waydroid are no longer part of the config.
- Includes desktop services for DisplayLink, OBS, Steam, VMware, VR, SDR, and a `glance` dashboard.

## Workload Notes

- Development: `codex`, `opencode`, `postman`, `mongodb-compass`, `distrobox`
- Virtualization: `vmware-workstation`, `virt-viewer`
- Gaming: `steam`, `lutris`, `heroic`, `osu-lazer`, `clonehero`, `retroarch`
- Creative and media: `blender`, `krita`, `kdenlive`, `plasticity`, `mixxx`, `musescore`, `hydrogen`

## Related

- [[01 Maps/Devices Map|Devices Map]]
- [[02 Systems/NixOS - Host nixos|NixOS - Host nixos]]
- [[90 Templates/Setup Note Template|Setup Note Template]]
