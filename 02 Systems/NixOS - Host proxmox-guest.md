## Purpose

Document the `proxmox-guest` host, composed in `modules/computers/proxmox-guest.nix`.

## Role

General-purpose Proxmox VM running an XFCE+i3 desktop.

## Composition

- `thorn-core` base bundle
- `desktop-xfce-i3` module
- service modules: audio, ClamAV
- `thorn-glance` dashboard module
- `qemu-guest.nix` profile
- `hosts/proxmox-guest/networking.nix`, `hardware-configuration.nix`
- host-specific Home Manager overlay (`hosts/proxmox-guest/home.nix`)

## Notable Host Behavior

- Trusts the internal Proxmox certificate (`certs/proxmox.guildedthorn.arpa.crt`) via `security.pki.certificates`.
- GRUB bootloader (`nodev` device, for VM boot), `services.qemuGuest.enable`, partition auto-growth on first boot.
- NetworkManager enabled (kept available for Wi-Fi/VPN use even though this is a VM); DNS `1.1.1.1`; firewall opens only SSH.
- SSH service module is present in the file but commented out — SSH is reachable here via base tooling/firewall rule rather than the shared `services-ssh` module being active.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
