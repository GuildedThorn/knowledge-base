## Purpose

Document the `scout` host, composed in `modules/computers/scout.nix`.

## Role

Daily-driver ThinkPad laptop for remote network management, development, media, light creative work, and general mobile use.

## Composition

- `thorn-core` base bundle
- Intel processor module, Intel graphics module, Hyprland desktop module
- service modules: audio, Bluetooth, ClamAV, fingerprint, Keybase, OBS, observability-roaming (WireGuard remote-write metrics to the SIEM), Spicetify, SDR, SSH
- `thorn-glance` dashboard module
- `hosts/scout/hardware-configuration.nix`, `networking.nix`, `secrets.nix` (WireGuard keys — see [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]), `wireguard.nix`
- host-specific Home Manager overlay (`hosts/scout/home.nix`) for a two-monitor Hyprland/panel layout (`eDP-1` laptop panel + `HDMI-A-2` external, both `highres`), plus Firefox/Ghostty/Obsidian/Vesktop — corrects an earlier "single-monitor" claim in this note

## Notable Host Behavior

- NetworkManager-managed Wi-Fi with power saving; external DNS `1.1.1.1`.
- Secure boot via `boot.lanzaboote` (`pkiBundle = /var/lib/sbctl`); `systemd-boot` disabled in favor of lanzaboote's own loader path.
- ThinkPad fan control via `thinkfan` with a custom aggressive fan curve, plus `thermald`, `tlp` (performance on AC, powersave + capped max perf on battery, charge thresholds 75–80%).
- `howdy`/IR emitter support, `upower`, `fwupd`, `flatpak` (MongoDB Compass), `earlyoom`, `ananicy`.
- U2F required for `sddm` and `sudo`; `gphoto2` enabled.
- `zramSwap` at 25%. (`system.autoUpgrade` was dropped — `comin` owns deploys, see [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]].)
- On-demand WireGuard road-warrior tunnel back to pfSense (`vpn-full`/`vpn-split`/`vpn-off` aliases) — see [[05 Network/WireGuard - Road Warrior|WireGuard - Road Warrior]].

## User-Facing Software Themes

- networking and diagnostics: `networkmanager`, `ethtool`
- hardware control: `corectrl`, `openrgb`, `brightnessctl`, `piper`
- communications: `element-desktop`, `telegram-desktop`, `teamspeak6-client`
- creative tools: `blender`, `krita`, `kdenlive`, `mixxx`, `musescore`, `hydrogen`
- engineering and electronics: `fritzing`, `plasticity`, `orca-slicer`
- development: `codex`, `claude-code`, `postman`, `android-studio`

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[03 Devices/ThinkPad T15|ThinkPad T15]]
