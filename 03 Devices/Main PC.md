## Purpose

Primary workstation for software development, VMware-based development VMs, finance, gaming, and general desktop use.

## Identity

- Hostname: `nixos`
- OS: `NixOS 26.06`
- Config path: `~/nix-config/nixos/users/thorn/hosts/nixos`

## Hardware Specs

- CPU: `Ryzen 9 5900X`
- GPU: `RX 6700XT 2x Mech OC`
- Memory: `32 GB DDR4 @ 3200 MHz`
- Storage: `2 TB Samsung 980 Evo`

## NixOS-Specific Notes

- Uses the `nixos` host under the `thorn` user tree.
- Runs Hyprland with a host-specific multi-monitor layout.
- Uses AMD processor and graphics modules.
- Uses local DNS at `127.0.0.1`.
- Has NetworkManager disabled.
- Mounts the media share at `/mnt/media` from `//172.16.25.4/media`.
- Enables Podman with Docker compatibility and `waydroid`.
- Includes desktop services for DisplayLink, OBS, Steam, VMware, VR, SDR, Ollama, and Technitium DNS.

## Workload Notes

- Development: `codex`, `claude-code`, `jetbrains.rider`, `postman`, `mongodb-compass`, `android-studio`, `neovim`
- Virtualization: `vmware-workstation`, `virt-viewer`, `realvnc-vnc-viewer`, `waydroid`, `podman`
- Gaming: `steam`, `lutris`, `heroic`, `osu-lazer`, `clonehero`, `retroarch`
- Creative and media: `blender`, `krita`, `inkscape`, `kdenlive`, `mixxx`, `musescore`, `hydrogen`

## Related

- [[01 Maps/Devices Map|Devices Map]]
- [[02 Systems/NixOS - Host nixos|NixOS - Host nixos]]
- [[90 Templates/Setup Note Template|Setup Note Template]]
