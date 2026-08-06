---
summary: "Document the `mac` host, composed in `modules/computers/mac.nix`."
status: active
tags: [systems, host]
---

## Purpose

Document the `mac` host, composed in `modules/computers/mac.nix`.

## Role

Intel CPU / AMD graphics machine running NixOS, a Hyprland desktop, and Proxmox VE. It is the deployed hypervisor for the `websites` and `soc` VMs.

## Composition

- `thorn-core` base bundle
- Hyprland desktop module, Intel processor module, AMD graphics module
- service modules: ClamAV, Proxmox, SSH
- `hosts/mac/disko.nix`, `networking.nix`
- host-specific Home Manager overlay (`hosts/mac/home.nix`): Hyprland + desktop-rice, Firefox, Ghostty — no Obsidian or Vesktop here, unlike `nixos`/`scout`

## Notable Host Behavior

- systemd-boot bootloader.
- The host is deployed on OPT1; its canonical address and DNS identity are in [[05 Network/Host & IP Inventory|Host & IP Inventory]].
- `enp9s0` is attached to `vmbr0`, which carries the host management address and Proxmox guest traffic to the Cisco Catalyst 3560G.
- `enp10s0` is unused; `vmbr1` and `vmbr2` are empty.
- NetworkManager is disabled. pfSense is the primary DNS resolver and gateway, with `1.1.1.1` as a fallback resolver.
- The firewall opens SSH and the Proxmox web UI port (`8006`).

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
- [[03 Devices/Mac Pro 5,1|Mac Pro 5,1]]
- [[05 Network/Host & IP Inventory|Host & IP Inventory]]
- [[05 Network/Physical Topology|Physical Topology]]
