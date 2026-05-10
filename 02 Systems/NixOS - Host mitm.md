## Purpose

Document the `mitm` host under `nixos/users/thorn/hosts/mitm`.

## Role

Service host for reverse proxying and internal web services.

## Composition

- networking from `hosts/mitm/networking.nix`
- shared service modules for Bluetooth, ClamAV, and SSH
- host-local service definitions for NGINX, Technitium DNS, MongoDB, Grafana, and SearXNG

## Notable Host Behavior

- Hostname is `mitm`.
- NetworkManager is disabled.
- Uses DNS `1.1.1.1`.
- Opens TCP and UDP ports `22`, `53`, `80`, and `443`.
- NGINX proxies traffic for `guildedthorn.com`, `radio.guildedthorn.com`, and internal service domains.
- Grafana is bound locally and fronted by NGINX.
- SearXNG configuration exists, but the service is currently set `enable = false`.

## Secret-Handling Notes

- The SearXNG server secret key is written to read from `config.sops.secrets.searx.path`.
- The active flake does not currently wire in `sops-nix`, so this is a migration target before SearXNG can be enabled cleanly.
- This host is a likely candidate for further secret migration cleanup because it mixes service definitions with secret consumption.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[01 Maps/Network Map|Network Map]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
