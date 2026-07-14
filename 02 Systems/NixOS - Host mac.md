## Purpose

Document the `mac` host, composed in `modules/computers/mac.nix`.

## Role

Intel CPU / AMD graphics machine running a Hyprland desktop, with Proxmox VE service support enabled.

## Composition

- `thorn-core` base bundle
- Hyprland desktop module, Intel processor module, AMD graphics module
- service modules: ClamAV, Proxmox, SSH
- `hosts/mac/disko.nix`, `networking.nix`
- host-specific Home Manager overlay (`hosts/mac/home.nix`)

## Notable Host Behavior

- systemd-boot bootloader.
- `services.proxmox-ve.ipAddress` is still a placeholder (`192.168.1.2`) marked `TODO: set this to mac's real LAN IP before deploying` — this host is not yet fully deployed.
- NetworkManager disabled; DNS `1.1.1.1`; firewall opens SSH and the Proxmox web UI port (8006).

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
