## Purpose

Summarize the reusable named modules under `modules/` that hosts compose from (see [[02 Systems/NixOS - Repository Layout|Repository Layout]] for how auto-loading works).

## Core

`modules/core/` provides base plumbing rather than opt-in features: `base.nix`, `files.nix`, `home-manager-modules.nix`, `nixos-modules.nix`, and `thorn-core.nix` (the bundle every host imports first as `config.nixos.modules.thorn-core`).

## Desktop Modules

- `desktop/hyprland.nix`: upstream Hyprland, UWSM, XWayland, `greetd` + `regreet`, `hyprlock`, `hypridle`, Wayland helper packages.
- `desktop/gnome-x11.nix`: GNOME on X11 with GDM and desktop portal packages.
- `desktop/xfce-i3.nix`: XFCE services combined with i3 as the window manager.
- `desktop/kde-wle.nix`: KDE Plasma (Wayland) — new since the last vault pass, not yet used by any current host module.

## Graphics Modules

- `graphics/amd.nix`: 32-bit graphics support, ROCm/OpenCL, `amdgpu`, `lact`, overdrive support.
- `graphics/intel.nix`: 32-bit graphics support, Intel VAAPI/media packages.
- `graphics/nvidia.nix`: stable proprietary NVIDIA driver, `nouveau` disabled, `nvidia-settings` enabled.

## Processor Modules

- `processor/amd.nix`: AMD microcode updates, tags OpenRGB with `motherboard = "amd"`.
- `processor/intel.nix`: Intel processor module.

## Service Modules (`modules/services/`)

`audio.nix` (PipeWire, PulseAudio disabled), `bluetooth.nix` (BlueZ/Blueman, PlayStation controller kernel modules), `clamav.nix`, `displaylink.nix`, `fingerprint.nix` (`fprintd` + PAM), `keybase.nix`, `obs.nix` (PipeWire capture + background-removal + `v4l2loopback`), `ollama.nix`, `proxmox.nix` (`services.proxmox-ve`), `retroarch.nix`, `sdr.nix` (RTL-SDR/HackRF), `spicetify.nix`, `ssh.nix`, `steam.nix` (Gamescope, GameMode), `tablets.nix` (`uinput` + OpenTabletDriver), `vmware.nix` (host support incl. macOS guests — no longer used by any host since it broke in the current nixpkgs pin), `vmware-guest.nix`.

SIEM/observability service modules added by the [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]]: `observability.nix` (Alloy journal shipping + node_exporter, in `thorn-core` fleet-wide), `observability-roaming.nix` (WireGuard remote-write variant for `scout`), `audit.nix` (auditd baseline + `thorn.audit.execScope`), `suricata.nix` (the `websites` sensor), `crowdsec.nix` (detect-only), `canary.nix` (the detection canary on `soc`/`websites`).

## Apps and Users

- `modules/apps/mcpelauncher.nix`: Minecraft Bedrock launcher packaging.
- `modules/users/thorn.nix`: the shared `thorn` user account.
- `modules/users/thorn-glance.nix`: the `glance` dashboard service module (separated out from the user module so only some hosts opt in — `nixos` and `scout` currently do).

## Home Manager Modules

See [[02 Systems/NixOS - Home Manager Layout|Home Manager Layout]] for `modules/home-manager/` in detail.

## Standalone Program Trees (`programs/`)

Not Home Manager modules — actual application source/config that a Home Manager module imports: only `programs/clonehero/clonehero.nix` (Clone Hero packaging) remains. The `programs/ags/` and `programs/eww/` widget trees were deleted along with the unused `astal`/`ags` flake inputs.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
- [[02 Systems/NixOS - Hosts Overview|Hosts Overview]]
- [[02 Systems/NixOS - Home Manager Layout|Home Manager Layout]]
