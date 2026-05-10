## Purpose

Document how Home Manager is used across the repo and what is shared versus host-specific.

## Shared User Home

The shared `thorn` Home Manager config in `nixos/users/thorn/home.nix` includes:

- Home Manager state version `26.05`
- imports for the AGS and NixVim Home Manager modules
- `zsh`, Oh My Zsh, completion, syntax highlighting, and a `nix-rebuild` alias
- `ghostty`, `atuin`, `intelli-shell`, `zoxide`, `ranger`, `newsboat`, `fastfetch`, `gpg`, and `neomutt`
- `hyprpanel` UI setup for `hyprland`
- `wlogout`, `rofi`, `hyprshot`, `hyprpaper`, `cliphist`, and `swayosd`
- `eww` and `ags` UI tooling
- `obsidian`, `vesktop`, `freetube`, and `nixvim`
- shared user packages such as YubiKey tools, GNOME Calculator, and `anki-bin`
- `firefox` extensions and policy setup
- unified `hyprland` keybinds, layout and plugins

## Shared Home Details

- AGS uses `./programs/ags` and Astal packages for battery, power profiles, IO, network, tray, MPRIS, apps, and WirePlumber integration.
- EWW uses `./programs/eww` with Bash and Zsh integration enabled.
- NixVim imports `./programs/nixvim/main.nix`; details are tracked in [[04 Software/NixVim|NixVim]].
- Vesktop is configured for Discord Canary, tray/minimize behavior, hardware acceleration, arRPC, and several Vencord plugins.
- HyprPanel uses transparent fullscreen auto-hide behavior, 24-hour clock formatting, visible battery/Bluetooth labels, workspace icons, and CaskaydiaCove NF at `16px`.
- Rofi uses `fullscreen-preview.rasi`, and Stylix theming is disabled for Rofi.
- The shared Hyprland config uses the upstream flake package, the Hyprexpo plugin, `SUPER` as mod, Dwindle layout, VRR enabled, workspace rules for browser/terminal/mail/editor, screenshot bindings through Hyprshot, and SwayOSD bindings for audio, brightness, lock keys, and media keys.
- Firefox defaults to DuckDuckGo, adds Nix package/options/wiki search aliases, starts at `http://localhost:8080`, and force-installs uBlock Origin, Vimium, Dark Reader, and Spirited Away.
- GPG is enabled with scdaemon configured for PC/SC sharing and CCID disabled.
- Mako is configured but disabled; SwayOSD and Cliphist are enabled instead.
- The pointer cursor is Bibata Modern Ice at size `24`.

## Host-Specific Home Overlays

- `users/thorn/hosts/scout/home.nix`: single-monitor Hyprland and wallpaper/panel layout for the ThinkPad.
- `users/thorn/hosts/nixos/home.nix`: multi-monitor Hyprland and panel layout for the main workstation.
- `users/thorn/hosts/vmware-guest/home.nix`: currently only sets `home.stateVersion = "26.05"`.

## Practical Takeaway

- system-level software and services live in host or shared NixOS modules
- user workflow, prompt, editor, launcher, and desktop polish live in Home Manager
- monitor layout and desktop UI are split per host rather than forced into the shared home config

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Host Layout|Host Layout]]
