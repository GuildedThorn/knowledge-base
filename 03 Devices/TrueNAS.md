## Purpose

Document the TrueNAS box, referenced across `ThornixOS` but not previously captured as its own device note.

## Identity

- Hostname: `truenas.guildedthorn.arpa`
- IP: `172.16.25.4`
- OS: TrueNAS (a `truenas-25.04.2.3` install/upgrade tarball sitting in `~/Downloads` suggests a recent version bump was in progress or being tested)

## Known Services

- **CIFS media share**: mounted by the `nixos` host at `/mnt/media` from `//172.16.25.4/media` (credentials via a credentials file, see [[02 Systems/NixOS - Host nixos|Host nixos]]).
- **Jellyfin**: reachable at `https://truenas.guildedthorn.arpa:8920`, monitored from the [[04 Software/Glance|Glance]] dashboard's Services page. `jellyfin-desktop` (client) is installed on `nixos` and `scout`, presumably to watch what this server hosts.
- **TrueNAS web UI**: `https://truenas.guildedthorn.arpa`, also monitored via Glance.
- Referenced with a static `extraHosts` override on both `nixos` and `websites` — `172.16.25.2` (presumably the internal DNS/gateway) doesn't resolve this `.arpa` name, so it's pinned locally instead. On `websites` this specifically matters because the SeaweedFS S3 endpoint's TLS cert is issued for the hostname, not the raw IP.

## Related

- [[01 Maps/Devices Map|Devices Map]]
- [[04 Software/Glance|Glance]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[02 Systems/NixOS - Host websites|Host websites]]
