## Purpose

Document the `scout` host as defined in `nixos/users/thorn/hosts/scout`.

## Role

Daily-driver laptop for remote network management, development, media, light creative work, and general mobile use.

## Composition

- networking from `hosts/scout/networking.nix`
- Intel graphics module
- Hyprland desktop module
- shared service modules for audio, Bluetooth, ClamAV, fingerprint, Keybase, OBS, Spicetify, SDR, and SSH
- host-specific Home Manager overlay for ThinkPad monitor and Hyprpanel layout

## Notable Host Behavior

- Hostname is `scout`.
- Uses NetworkManager with Wi-Fi power saving enabled.
- Uses external DNS `1.1.1.1`.
- Opens TCP and UDP port `53`.
- Enables ThinkPad fan control through `thinkpad_acpi` and `thinkfan`.
- Enables `howdy`, IR emitter support, `tlp`, `thermald`, `upower`, `fwupd`, `flatpak`, `earlyoom`, and other laptop-oriented services.

## User-Facing Software Themes

- networking and diagnostics: `networkmanager`, `ethtool`
- hardware control: `corectrl`, `openrgb`, `brightnessctl`, `piper`
- communications: `element-desktop`, `telegram-desktop`, `teamspeak6-client`
- creative tools: `blender`, `krita`, `kdenlive`, `mixxx`, `musescore`, `hydrogen`
- engineering and electronics: `fritzing`, `chirp`, `orca-slicer`
- development: `codex`, `postman`, `mongodb-compass`, `android-studio`

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[03 Devices/ThinkPad T15|ThinkPad T15]]
