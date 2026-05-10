## Purpose

Summarize the reusable modules under `nixos/desktop`, `nixos/graphics`, `nixos/processor`, `nixos/services`, `nixos/secrets`, and `nixos/users/thorn/services`.

## Desktop Modules

- `desktop/hyprland.nix`: enables upstream Hyprland, UWSM, XWayland, `greetd` + `regreet`, `hyprlock`, `hypridle`, and Wayland helper packages.
- `desktop/gnome-x11.nix`: enables GNOME on X11 with GDM and desktop portal packages.
- `desktop/xfce+i3.nix`: combines XFCE services with i3 as the window manager.

## Graphics Modules

- `graphics/amd.nix`: enables 32-bit graphics support, ROCm/OpenCL packages, `amdgpu`, `lact`, and overdrive support.
- `graphics/intel.nix`: enables 32-bit graphics support and Intel VAAPI/media packages.
- `graphics/nvidia.nix`: forces the stable proprietary NVIDIA driver, disables `nouveau`, and enables `nvidia-settings`.

## Processor Modules

- `processor/amd.nix`: enables AMD microcode updates and tags OpenRGB with `motherboard = "amd"`.
- `processor/intel.nix`: currently empty placeholder Intel processor module.

## Service Modules

- `audio.nix`: standard PipeWire setup with PulseAudio disabled.
- `bluetooth.nix`: BlueZ, Blueman, gamepad-oriented Bluetooth settings, and PlayStation-related kernel modules.
- `clamav.nix`: installs ClamAV and enables both daemon and updater.
- `displaylink.nix`: enables EVDI and a manual `DisplayLinkManager` service.
- `fingerprint.nix`: enables `fprintd` with PAM integration for login and sudo.
- `keybase.nix`: enables KBFS and user services for Keybase GUI.
- `obs.nix`: enables OBS Studio with PipeWire and background-removal plugins plus `v4l2loopback`.
- `ollama.nix`: enables Ollama, preloads `llama3.2:3b` and `deepseek-r1:1.5b`, and exposes Open WebUI on port `8081`.
- `proxmox.nix`: enables `services.proxmox-ve` and the matching overlay.
- `retroarch.nix`: installs RetroArch plus a curated libretro core set under `/etc/retroarch`.
- `sdr.nix`: enables RTL-SDR and HackRF tooling.
- `spicetify.nix`: enables Spicetify with adblock, shuffle, and custom app/snippet configuration.
- `ssh.nix`: starts the SSH agent.
- `steam.nix`: enables Steam, Gamescope, Steam hardware support, and GameMode.
- `tablets.nix`: enables `uinput` and OpenTabletDriver.
- `vmware-guest.nix`: enables VMware guest support.
- `vmware.nix`: enables VMware Workstation host support, including macOS guest support.
- `vr.nix`: enables WiVRn and custom Steam/OpenXR handling, and applies an AMD GPU kernel patch.

## Secrets Module

- `secrets/default.nix` installs `age`, `sops`, and `ssh-to-age`.
- It configures `sops-nix` to reuse `/etc/ssh/ssh_host_ed25519_key` for decryption.
- The file currently contains example secret declarations rather than active ones.
- The active flake does not currently import `sops-nix` or `secrets/default.nix`, so this is a plan/staging area rather than working secret plumbing.

## Thorn Service Modules

- `users/thorn/services/glance.nix`: exposes Glance on `0.0.0.0:8080` with Home, Videos, and Services pages.
- `users/thorn/services/pihole.nix`: defines a Pi-hole/FTL service profile and DNS/DHCP settings, but is not imported by any current host.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
- [[02 Systems/NixOS - Hosts Overview|Hosts Overview]]
