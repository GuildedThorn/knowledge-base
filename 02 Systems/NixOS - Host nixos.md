## Purpose

Document the `nixos` host under `nixos/users/thorn/hosts/nixos`.

## Role

Main AMD workstation with a broad desktop, gaming, virtualization, creative, XR, and local-network tooling stack.

## Composition

- networking from `hosts/nixos/networking.nix`
- Hyprland desktop module
- AMD processor and AMD graphics modules
- shared service modules for audio, Bluetooth, ClamAV, DisplayLink, fingerprint, Keybase, OBS, RetroArch, Spicetify, SDR, SSH, Steam, tablets, VMware host support, and VR
- host-specific Home Manager overlay for multi-monitor Hyprland layout

## Notable Host Behavior

- Hostname is `nixos`.
- Uses local DNS at `127.0.0.1`.
- NetworkManager is disabled.
- Opens TCP and UDP ports `53`, `4455`, `8500`, `5201`, and `8000`.
- Mounts `//172.16.25.4/media` at `/mnt/media` using a credentials file under `/etc/nixos/secrets/credentials.env`.
- Enables Podman with Docker compatibility and Waydroid.
- Enables printing with common CUPS filters and Canon UFR2 drivers.
- Enables OpenRGB, CoreCtrl, Thunar, AppImage binfmt support, Thunderbird, smartcards, and Ananicy.

## User-Facing Software Themes

- gaming: `steam`, `lutris`, `heroic`, `osu-lazer`, `clonehero`
- virtualization: `virt-viewer`, `vmware-workstation`, `realvnc-vnc-viewer`
- creative tools: `blender`, `krita`, `kdenlive`, `mixxx`, `musescore`, `hydrogen`
- fabrication and electronics: `orca-slicer`, `fritzing`, `chirp`, `arduino`
- development: `codex`, `claude-code`, `jetbrains.rider`, `postman`, `mongodb-compass`
- XR: `openxr-loader`, `xrizer`, `wayvr`, WiVRn/Monado via the VR module

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
