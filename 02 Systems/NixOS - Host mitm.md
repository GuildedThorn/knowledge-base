## Purpose

Document the `mitm` host, composed in `modules/computers/mitm.nix`. The Proxmox VM variant of this role (`proxmox-mitm`) was removed from the repo entirely.

## Role

Bare-metal service host for reverse proxying and internal web services.

## Composition

- `thorn-core` base bundle
- service modules: Bluetooth, ClamAV, SSH
- `hosts/mitm/hardware-configuration.nix`, `networking.nix`
- inline NGINX + SearXNG config (no separate service module — defined directly in `modules/computers/mitm.nix`)

## Notable Host Behavior

- NetworkManager disabled; DNS `1.1.1.1`.
- The `guildedthorn.com`/`radio.guildedthorn.com` reverse-proxy vhosts were pruned — NGINX (still enabled) now fronts only `searxng.guildedthorn.arpa` over a UWSGI socket. A `security.acme` block for `guildedthorn.com` lingers in the host file.
- `services.searx` is fully configured (DuckDuckGo-forward engine set, vim hotkeys, rate limiting) but currently `enable = false`.
- A `services.mongodb` block exists but is commented out.

## Secret-Handling Notes

- The SearXNG secret key reads from `config.sops.secrets.searx.path`, but `mitm` has no `hosts/mitm/secrets.nix` yet — this is a migration target before SearXNG can be enabled cleanly (see [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]).

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[01 Maps/Network Map|Network Map]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
