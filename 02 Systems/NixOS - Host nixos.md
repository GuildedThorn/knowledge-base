## Purpose

Document the `nixos` host, composed in `modules/computers/nixos.nix`.

## Role

Main AMD workstation with a broad desktop, gaming, virtualization, creative, XR, and local-network tooling stack.

## Composition

- `thorn-core` base bundle
- Hyprland desktop module, AMD processor and AMD graphics modules
- service modules: audio, Bluetooth, ClamAV, DisplayLink, fingerprint, Keybase, OBS, RetroArch, Spicetify, SDR, SSH, Steam, tablets, VMware host support, VR
- `thorn-glance` dashboard module
- `hosts/nixos/hardware-configuration.nix`, `disko.nix`, `networking.nix`, `secrets.nix` (one of only two hosts with sops secrets — see [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]])
- host-specific Home Manager overlay (`hosts/nixos/home.nix`) for multi-monitor Hyprland layout

## Notable Host Behavior

- Uses external DNS `1.1.1.1` with NetworkManager enabled (kept for Wi-Fi/VPN use); local `extraHosts` entries resolve `pfsense.guildedthorn.arpa`, `proxmox.guildedthorn.arpa`, and `truenas.guildedthorn.arpa`. There is no local DNS resolver service on this host — the previous note's claim of Technitium DNS at `127.0.0.1` no longer matches the repo.
- Enables Docker (via `virtualisation.docker`), printing (CUPS + Canon UFR2), OpenRGB, CoreCtrl, Thunar, AppImage binfmt, direnv, starship, gnupg agent, flatpak (incl. Sober/Vinegar Roblox compatibility layers, QRookie, MongoDB Compass).
- U2F (`security.pam.u2f`) required for `sddm` and `sudo`; YubiKey smartcard support enabled.
- `zramSwap` at 25%, unattended `system.autoUpgrade` (no auto-reboot), `ananicy`, `earlyoom`, `systemd.oomd`.
- `services.ollama.package = pkgs.ollama-vulkan`.

## User-Facing Software Themes

- gaming: `steam`, `lutris`, `heroic`, `osu-lazer`, `clonehero`
- virtualization: `virt-viewer`, `vmware-workstation`
- creative tools: `blender`, `krita`, `kdenlive`, `mixxx`, `musescore`, `hydrogen`
- fabrication and electronics: `orca-slicer`, `fritzing`, `plasticity`, `chirp`, `arduino`
- development: `codex`, `opencode`, `jetbrains.rider` (implied via prior notes), `postman`, `mongodb-compass`, `distrobox`
- XR: `openxr-loader`, `xrizer`, `wayvr`

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
