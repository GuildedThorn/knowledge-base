## Purpose

Document the `proxmox-mitm` host, composed in `modules/computers/proxmox-mitm.nix` — the Proxmox VM variant of [[02 Systems/NixOS - Host mitm|Host mitm]].

## Role

Proxmox-hosted reverse-proxy/service lab, mirroring the bare-metal `mitm` host's intended role with a Grafana instance added.

## Composition

- `thorn-core` base bundle
- service modules: ClamAV, SSH
- `qemu-guest.nix` profile
- `hosts/proxmox-mitm/hardware-configuration.nix`, `networking.nix`
- inline NGINX + SearXNG + Grafana config (same pattern as `mitm`, defined directly in the host file)

## Notable Host Behavior

- Static networking on `172.16.100.2/24` via `ens18`, DHCP disabled, DNS `8.8.8.8`.
- Firewall opens SSH, DNS (53), DHCP (67/68), and port 5380.
- NGINX config for `guildedthorn.com`, `radio.guildedthorn.com`, `searxng.guildedthorn.arpa`, and `grafana.guildedthorn.arpa` all exist but `services.nginx.enable = false` — this host is currently a template/staging config, not live.
- `services.searx` and `services.grafana` are both fully specified but `enable = false`, same staging status as NGINX.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[01 Maps/Network Map|Network Map]]
- [[02 Systems/NixOS - Host mitm|Host mitm]]
- [[09 Observability/Grafana|Grafana]]
