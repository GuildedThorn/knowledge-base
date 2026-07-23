---
summary: "Track the WeeChat IRC client setup, managed by the `thorn.programs.weechat` Home Manager module (`modules/home-manager/weechat.nix` in `ThornixOS`)."
status: active
tags: [software]
---

## Purpose

Track the WeeChat IRC client setup, managed by the `thorn.programs.weechat` Home Manager module (`modules/home-manager/weechat.nix` in `ThornixOS`).

## Current State

- Enabled on the `nixos` host only (`hosts/nixos/home.nix`) — not configured on `scout`, `mac`, or `proxmox-guest`.
- Nick/username/realname default to `GuildedThorn` for every configured server.
- One server is currently declared: `oftc` (`irc.oftc.net/6697`), autoconnecting with 7 autojoin channels — `#kali-linux`, `#oftc`, `#kali-nethunter`, `#linux`, `#home-manager`, `#wayland`, `#freedesktop`. OFTC hosts the Kali, Wayland/freedesktop.org, and Home Manager support channels, which is why they're all on this one network.

## Authentication

- Uses CertFP (client-certificate) authentication rather than a password: `sslCert` points at a sops-nix secret (`oftc_client_cert`), a PEM file with cert+key concatenated, presented during the TLS handshake.
- The certificate's fingerprint must be registered once with NickServ (`/msg NickServ CERT ADD`) before it actually identifies the user — the module only wires up the client-side cert, registration is a manual one-time step.
- `sasl` (IRCv3 SASL EXTERNAL on top of the cert) defaults to `true` in the module but is explicitly set `false` for the `oftc` server, because OFTC's ircd doesn't advertise the `sasl` capability — it auto-identifies from the cert at registration instead, and requesting an unsupported capability just loops connect/disconnect.
- `commandDelay` (default 3s) waits after connecting before autojoin fires, so CertFP/SASL registration has time to land first — without it, the first autojoin can race ahead of authentication and silently fail to join until done manually.

## How the Module Works

Renders `~/.config/weechat/irc.conf` from the declared `servers` attrset — each server becomes an `irc.server.<name>.*` block (`addresses`, `ssl`/`ssl_verify`, `autoconnect`, `nicks`/`username`/`realname`, `ssl_cert` when set, `sasl_mechanism = external` when both `sslCert` and `sasl` are set, `autojoin`, and `command_delay`).

## Secret-Handling Notes

- The OFTC client certificate is stored as the sops-nix secret `oftc_client_cert` on the `nixos` host — see [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]].

## Related

- [[01 Maps/Software Map|Software Map]]
- [[02 Systems/NixOS - Home Manager Layout|Home Manager Layout]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
