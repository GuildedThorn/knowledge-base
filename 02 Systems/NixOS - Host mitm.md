## Purpose

Document the `mitm` host, composed in `modules/computers/mitm.nix`. A Proxmox VM variant of the same role exists as `proxmox-mitm` — see [[02 Systems/NixOS - Host proxmox-mitm|Host proxmox-mitm]].

## Role

Bare-metal service host for reverse proxying and internal web services.

## Composition

- `thorn-core` base bundle
- service modules: Bluetooth, ClamAV, SSH
- `hosts/mitm/hardware-configuration.nix`, `networking.nix`
- inline NGINX + SearXNG config (no separate service module — defined directly in `modules/computers/mitm.nix`)

## Notable Host Behavior

- NetworkManager disabled; DNS `1.1.1.1`.
- NGINX reverse-proxies `guildedthorn.com` and `radio.guildedthorn.com` (ACME-issued certs, `forceSSL`) to `proxmox.guildedthorn.arpa` on ports 5000/5001, plus `searxng.guildedthorn.arpa` over a UWSGI socket.
- `services.searx` is fully configured (DuckDuckGo-forward engine set, vim hotkeys, rate limiting) but currently `enable = false`.
- A `services.mongodb` block exists but is commented out.

## Secret-Handling Notes

- The SearXNG secret key reads from `config.sops.secrets.searx.path`, but `mitm` has no `hosts/mitm/secrets.nix` yet — this is a migration target before SearXNG can be enabled cleanly (see [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]).

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[01 Maps/Network Map|Network Map]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
- [[02 Systems/NixOS - Host proxmox-mitm|Host proxmox-mitm]]
