---
summary: "Document the `nixos` host, composed in `modules/computers/nixos.nix`."
status: active
tags: [systems, host]
---

## Purpose

Document the `nixos` host, composed in `modules/computers/nixos.nix`.

## Role

Main AMD workstation with a broad desktop, gaming, virtualization, creative, XR, and local-network tooling stack.

## Composition

- `thorn-core` base bundle
- Hyprland desktop module, AMD processor and AMD graphics modules
- service modules: audio, Bluetooth, ClamAV, DisplayLink, fingerprint, Keybase, OBS, RetroArch, Spicetify, SDR, SSH, Steam, tablets, VR (VMware host support was dropped — package broken in the current nixpkgs pin)
- `thorn-glance` dashboard module
- `hosts/nixos/hardware-configuration.nix`, `disko.nix`, `networking.nix`, `secrets.nix` (see [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]])
- host-specific Home Manager overlay (`hosts/nixos/home.nix`) for the multi-monitor Hyprland layout, plus the spanning wallpaper (`thorn.desktop.wallpaper`) and the CRT SOC display (`thorn.desktop.crt`)

## Notable Host Behavior

- Uses external DNS `1.1.1.1` with NetworkManager enabled (kept for Wi-Fi/VPN use); local `extraHosts` entries resolve `pfsense.guildedthorn.arpa`, `proxmox.guildedthorn.arpa`, and `truenas.guildedthorn.arpa`. There is no local DNS resolver service on this host — the previous note's claim of Technitium DNS at `127.0.0.1` no longer matches the repo.
- Enables Docker (via `virtualisation.docker`), printing (CUPS + Canon UFR2), OpenRGB, CoreCtrl, Thunar, AppImage binfmt, direnv, starship, gnupg agent, flatpak (incl. Sober/Vinegar Roblox compatibility layers, QRookie, MongoDB Compass).
- U2F (`security.pam.u2f`) required for `sddm` and `sudo`; YubiKey smartcard support enabled.
- `zramSwap` at 25%, `ananicy`, `earlyoom`, `systemd.oomd`. (`system.autoUpgrade` was dropped — `comin` owns deploys.)
- `services.ollama.package = pkgs.ollama-vulkan`.

## User-Facing Software Themes

- gaming: `steam`, `lutris`, `heroic`, `osu-lazer`, `clonehero`
- virtualization: `virt-viewer` (`vmware-workstation` removed along with VMware host support)
- creative tools: `blender`, `krita`, `kdenlive`, `mixxx`, `musescore`, `hydrogen`
- fabrication and electronics: `orca-slicer`, `fritzing`, `plasticity`, `chirp`, `arduino`
- development: `codex`, `opencode`, `postman`, `mongodb-compass`, `distrobox`
- XR: `openxr-loader`, `xrizer`, `wayvr`

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
