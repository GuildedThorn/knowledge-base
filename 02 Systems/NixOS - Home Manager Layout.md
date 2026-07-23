---
summary: Document how Home Manager is used across `ThornixOS` and what is shared versus host-specific.
status: active
tags: [systems]
---

## Purpose

Document how Home Manager is used across `ThornixOS` and what is shared versus host-specific.

## Shared Home Manager Modules

`modules/home-manager/` holds one file per concern rather than a single monolithic home config:

- `base.nix`: core shell/CLI setup — `zsh` (Oh My Zsh, completion, syntax highlighting, a `nix-rebuild` shell alias), [[04 Software/Shell Environment|Shell Environment]] tools (`atuin`, `intelli-shell`, `zoxide`, `fastfetch`), [[04 Software/Yazi|Yazi]], `feh`, `playerctld`, GPG with scdaemon settings, and shared user packages (`arc-theme`, YubiKey tools). Corrects an earlier pass of this note, which claimed `ranger`/`newsboat`/`anki-bin`/GNOME Calculator were declared here — none of those actually appear in `base.nix`; GNOME Calculator is real but lives in `hyprland.nix`/`xfce-i3.nix` as a keybind target instead, and a `~/.newsboat` directory exists on disk with no feeds configured, suggesting vestigial/imperative setup rather than something Home Manager manages.
- `hyprland/`: shared Hyprland config, split per-concern into `core.nix`, `keybinds.nix`, `animations.nix`, and `window-rules.nix` (was a single `hyprland.nix`).
- `desktop-rice.nix`: shared desktop polish/theming layer (panel, cursor, etc. conventions shared across Hyprland hosts).
- `wallpaper.nix`: spanning wallpaper across all monitors via the `awww` daemon (`thorn.desktop.wallpaper`).
- `crt.nix`: the CRT SOC display on the workstation (`thorn.desktop.crt`) — a live log feed from the SIEM, see [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]].
- `ghostty.nix`: terminal config — see [[04 Software/GhostTTY|GhostTTY]].
- `nixvim/`: editor config, split per-concern into `core.nix`, `lsp.nix`, `completion.nix`, `keymaps.nix`, and `debug.nix` (was a single `nixvim.nix`) — see [[04 Software/NixVim|NixVim]].
- `claude-code.nix`: Claude Code CLI setup, enabled on `nixos` and `scout` — see [[04 Software/AI Coding Tools|AI Coding Tools]].
- `obsidian.nix`: this vault's Obsidian setup — see [[04 Software/Obsidian|Obsidian]].
- `firefox.nix`: extensions and policy — see [[04 Software/Firefox|Firefox]].
- `vesktop.nix`: Discord Canary via Vesktop — tray/minimize behavior, hardware acceleration, arRPC, Vencord plugins. Briefly dropped in favor of a new `dorion.nix` (Dorion Discord client), then brought back — `dorion.nix` still exists but nothing enables it. See [[04 Software/Vesktop|Vesktop]].
- `matcha.nix`: the Matcha terminal email client — see [[04 Software/Matcha|Matcha]]. (Corrects an earlier pass of this note, which mis-described this as a theming module without having read it.)
- `neomutt.nix`: a second, parallel mbsync/msmtp/notmuch/neomutt email stack against the same accounts as Matcha.
- `weechat.nix`: WeeChat IRC client, CertFP-authenticated against OFTC — see [[04 Software/WeeChat|WeeChat]].
- `xfce-i3.nix`: Home Manager pieces for the XFCE+i3 desktop hosts.

## Host-Specific Home Overlays

- `hosts/scout/home.nix`: two-monitor Hyprland and panel layout for the ThinkPad (`eDP-1` internal + `HDMI-A-2` external dock/monitor) — corrects an earlier "single-monitor" claim.
- `hosts/nixos/home.nix`: multi-monitor Hyprland and panel layout for the main workstation.
- `hosts/mac/home.nix`: home overlay for the `mac` host.
- `hosts/proxmox-guest/home.nix`: home overlay for the general-purpose Proxmox VM.
- `hosts/vmware-guest/home.nix`: minimal overlay, historically just `home.stateVersion`.

Hosts with no `home.nix` (`websites`, `soc`, `firewall`, `mitm`, `vmware-test`) run without a Home Manager user layer — they're service/test boxes, not desktops. (`proxmox-mitm` was removed from the repo.)

## Standalone Program Trees

The `programs/ags/` and `programs/eww/` widget trees were deleted (along with the `astal`/`ags` flake inputs); only `programs/clonehero/` remains — see [[02 Systems/NixOS - Shared Modules|Shared Modules]].

## Practical Takeaway

- system-level software and services live in host or shared NixOS modules
- user workflow, prompt, editor, launcher, and desktop polish live in Home Manager
- monitor layout and desktop UI are split per host rather than forced into the shared home config

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Host Layout|Host Layout]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
