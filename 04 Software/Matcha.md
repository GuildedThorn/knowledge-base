## Purpose

Track the Matcha terminal email client setup, managed by the `thorn.programs.matcha` Home Manager module (`modules/home-manager/matcha.nix` in `ThornixOS`).

## Current State

- Enabled on the `nixos` host only (`hosts/nixos/home.nix`) — not configured on `scout`, `mac`, or `proxmox-guest`.
- Three Gmail accounts are declared, all using the `gmail` service-provider preset (IMAP/SMTP servers filled in automatically):
  - `guildedthorn` → `guildedthorn@gmail.com`
  - `opticalpvpx` → `opticalpvpx@gmail.com`
  - `jamieduddleston2` → `jamieduddleston2@gmail.com`
- Real name on outgoing mail defaults to `Jamie Duddleston` for every account.

## How the Module Works

- The module renders `~/.config/matcha/config.json` from the declared `accounts` attrset — each account becomes one entry with `name`, `email`, `service_provider`, and a `pass_cmd`.
- Passwords never touch the Nix store or the rendered config file directly: each account's `secretPath` points at a sops-nix secret (e.g. `osConfig.sops.secrets.gmail_guildedthorn_app_password.path`), and `pass_cmd` is just `cat <that path>` — Matcha shells this out at startup to get the password.
- `serviceProvider` supports `gmail`, `outlook`, `icloud`, or `custom` (the last requires explicit `imapServer`/`imapPort`/`smtpServer`/`smtpPort`).

## Relationship to Neomutt

`nixos` also runs a second, parallel email stack against the exact same three Gmail accounts: Home Manager's built-in `accounts.email` module plus `programs.neomutt`/`mbsync`/`msmtp`/`notmuch` (wired up via the separate `thorn.programs.neomutt` module, which additionally runs a `mail-notify` script via `services.mbsync.postExec` for desktop new-mail notifications). Matcha and Neomutt are both enabled and both point at the same accounts/secrets — Neomutt does not yet have its own vault note.

## Secret-Handling Notes

- All three account passwords are Gmail app passwords, stored as sops-nix secrets (`gmail_guildedthorn_app_password`, `gmail_opticalpvpx_app_password`, `gmail_jamieduddleston2_app_password`) on the `nixos` host — see [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]].

## Confirmed Live

`~/Maildir/` on `nixos` has real per-account subfolders for all three accounts (`guildedthorn`, `jamieduddleston2`, `opticalpvpx`) — this is actively syncing mail via `mbsync`, not just declared config.

## Related

- [[01 Maps/Software Map|Software Map]]
- [[02 Systems/NixOS - Home Manager Layout|Home Manager Layout]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
