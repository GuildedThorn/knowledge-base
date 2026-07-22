## Purpose

Capture the current secret-management approach in ThornixOS without copying sensitive values into the knowledge base.

## Current State

sops-nix is fully live, not just planned — this reverses the old note's premise. Secrets are encrypted with [sops](https://github.com/getsops/sops)/[sops-nix](https://github.com/Mic92/sops-nix) and committed to the repo as ciphertext, per-host, in `hosts/<host>/secrets.yaml` with a matching `hosts/<host>/secrets.nix` declaring `sops.secrets.<name>`.

Four hosts are onboarded: `nixos`, `websites`, `soc`, and `scout` (each has `hosts/<host>/secrets.nix` + `secrets.yaml`; other hosts have neither).

## Recipients (`.sops.yaml`)

Two recipient classes, per file:

- The admin's YubiKey-backed GPG key — always a co-recipient on every secrets file, so a host key loss never locks the admin out. Decrypting/re-encrypting from the workstation prompts for the YubiKey PIN.
- Each onboarded host's own age key, derived from that host's SSH host key (`/etc/ssh/ssh_host_ed25519_key`) via `ssh-to-age`. This lets `sops-nix` decrypt unattended during activation with no YubiKey involved.

`sops` and `ssh-to-age` are installed on every host via `modules/core/base.nix`.

## Lifecycle

- **Edit an existing file**: `sops hosts/<host>/secrets.yaml` — opens `$EDITOR` on the decrypted contents, re-encrypts to all configured recipients on save.
- **Add a secret to an onboarded host**: add the key via `sops`, declare `sops.secrets.my_new_secret = { };` in `hosts/<host>/secrets.nix`, rebuild. It lands at `/run/secrets/my_new_secret` (root:root, 0400 by default) and is referenced elsewhere via `config.sops.secrets.<name>.path`.
- **Onboard a new host**: get its SSH host public key, convert with `ssh-to-age`, add the resulting `age1...` key to `.sops.yaml` plus a `creation_rules:` entry for `hosts/<host>/secrets\.ya?ml$`, create the encrypted file with `sops --encrypt --in-place`, then add `hosts/<host>/secrets.nix` to that host's `modules/computers/<host>.nix` module list.
- **Rotate recipients**: after changing `.sops.yaml`, run `sops updatekeys hosts/<host>/secrets.yaml` to re-encrypt for the new recipient set.
- **Recover after host reinstall / host-key loss**: a wipe regenerates the SSH host key, invalidating that host's old age key. Get the new age key via `ssh-to-age`, swap it into `.sops.yaml`, run `sops updatekeys`, rebuild. The admin's GPG key being a permanent co-recipient means this is never a lockout — just an `updatekeys` round-trip. Host private keys are intentionally never backed up.

## Non-Secret Certs

`certs/` holds two checked-in (non-secret) certificate files: `ThornCloud_CA.crt` (an internal CA) and `proxmox.guildedthorn.arpa.crt`. These are trusted into specific hosts (e.g. `proxmox-guest` reads the Proxmox cert into `security.pki.certificates`) — they are public certificates, not key material, so they live in the repo in plaintext.

## Known Secrets in Use

- `nixos`: `wakatime_api_key` (templated into `~/.wakatime.cfg` for [[04 Software/AI Coding Tools|Wakapi]]), three Gmail app passwords (`gmail_guildedthorn_app_password`, `gmail_opticalpvpx_app_password`, `gmail_jamieduddleston2_app_password` — consumed by both [[04 Software/Matcha|Matcha]] and the parallel Neomutt/mbsync/msmtp stack), and `oftc_client_cert` (the [[04 Software/WeeChat|WeeChat]] CertFP client certificate).
- `websites`: `guildedthorn_env` (the entire [[GuildedThorn.com - Overview|GuildedThorn.com]] dotenv — JWT/MongoDB/RabbitMQ/Spotify secrets bundled as one opaque blob rather than declared individually) and `cloudflared_tunnel_token` (templated into a `cloudflared.env` sops template for the Cloudflare Tunnel).
- `soc`: Loki S3 credentials for the TrueNAS bucket (`loki_s3_access_key_id`/`loki_s3_secret_access_key`, currently reused for the restic Prometheus backup too), `restic_password` (not recoverable from the host — also kept in a password manager), `grafana_admin_password`, `grafana_secret_key`, `grafana_discord_webhook`, and the Grafana TLS private key — see [[02 Systems/NixOS - Host soc|Host soc]].
- `scout`: `wg_private_key` and `wg_preshared_key` for the [[05 Network/WireGuard - Road Warrior|WireGuard road-warrior]] tunnel.
- `mitm`: a SearXNG secret key is wired to read from `config.sops.secrets.searx.path`, but SearXNG itself is currently `enable = false` and the host has no `secrets.nix` yet, so this isn't live. (The `proxmox-mitm` variant was removed from the repo.)

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Repository Layout|Repository Layout]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
- [[02 Systems/NixOS - Host websites|Host websites]]
