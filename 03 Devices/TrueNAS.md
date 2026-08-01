---
summary: "Document the TrueNAS box, referenced across `ThornixOS` but not previously captured as its own device note."
status: active
tags: [devices]
---

## Purpose

Document the TrueNAS box, referenced across `ThornixOS` but not previously captured as its own device note.

## Identity

- Hostname: `truenas.guildedthorn.arpa`
- IP: `172.16.25.4`
- OS: TrueNAS SCALE **25.10.4** (`/etc/version`, captured 2026-08-01). The previous `25.04.2.3` boot environment is retained on the boot pool; its `@pristine` snapshots date the upgrade to ~2026-07-13.

## Known Services

- **CIFS media share**: mounted by the `nixos` host at `/mnt/media` from `//172.16.25.4/media` (credentials via a credentials file, see [[02 Systems/NixOS - Host nixos|Host nixos]]).
- **Jellyfin**: reachable at `https://truenas.guildedthorn.arpa:8920`, monitored from the [[04 Software/Glance|Glance]] dashboard's Services page. `jellyfin-desktop` (client) is installed on `nixos` and `scout`, presumably to watch what this server hosts.
- **TrueNAS web UI**: `https://truenas.guildedthorn.arpa`, also monitored via Glance.
- **Apps** (confirmed by `platter/ix-apps/app_mounts/*` datasets, 2026-08-01): **Gitea** (with its own Postgres), **Jellyfin**, **MongoDB** (~1.24G of data — likely candidate for GuildedThorn.com's undocumented Mongo, see [[08 Improvements/Backup and DR Strategy|Backup and DR Strategy]]; also relevant to the 2026-07-28 "internal MongoDB probing" SIEM alert), and **SeaweedFS** (the S3 endpoint `websites` uses).
- Referenced with a static `extraHosts` override on both `nixos` and `websites` — `172.16.25.2` (presumably the internal DNS/gateway) doesn't resolve this `.arpa` name, so it's pinned locally instead. On `websites` this specifically matters because the SeaweedFS S3 endpoint's TLS cert is issued for the hostname, not the raw IP.

## Storage

Captured 2026-08-01 over SSH (read-only) — raw output in [[12 Datasets/TrueNAS Storage Capture 2026-08-01|TrueNAS Storage Capture 2026-08-01]].

### Pools

| Pool | Size | Used | Free | Health |
|---|---|---|---|---|
| `boot-pool` | 111G | 12.2G | 98.8G | ONLINE |
| `platter` | 7.25T | 540G | 6.72T | ONLINE |

`platter` is the single data pool — everything below lives on it.

### Datasets (platter)

- `platter/media` — **447G**, the CIFS share mounted by `nixos` at `/mnt/media`. The bulk of the pool.
- `platter/malware` — **53.6G** of sample storage.
- `platter/files`, `platter/certs` — present but effectively empty (96K each).
- `platter/ix-apps` — **16.8G**, TrueNAS app infrastructure: app mounts for Gitea, Jellyfin, MongoDB, SeaweedFS, plus 13G of Docker layers.
- `platter/.system` — 2.16G of TrueNAS service state.

### Snapshots — none that matter

- **No periodic snapshot tasks are configured** (`pool.snapshottask.query` returns empty, `com.sun:auto-snapshot` unset everywhere).
- The only snapshots on the system are app-upgrade rollback points (`gitea@1.6.19/@1.6.21`, `seaweedfs@1.2.29`) and boot-environment `@pristine` markers from the 25.10.4 upgrade.
- `media`, `malware`, `files`, and `certs` have **zero snapshots** — no point-in-time protection on any user data.

### Scrubs

- One scheduled scrub task: `platter`, Sundays 00:00, **35-day threshold**, enabled — so it actually runs roughly every 5 weeks. Last run Sun 2026-07-12, 0B repaired, 0 errors, 18m22s.
- `boot-pool` scrubs via the separate boot-pool scrub interval (not a pool scrub task); last run Sun 2026-07-26, clean.

### Replication — none

`replication.query` returns empty. Combined with no snapshots, the NAS holds the **only copy** of media and app data — see the SPOF discussion in [[08 Improvements/Backup and DR Strategy|Backup and DR Strategy]].

## Related

- [[01 Maps/Devices Map|Devices Map]]
- [[04 Software/Glance|Glance]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[02 Systems/NixOS - Host websites|Host websites]]
- [[08 Improvements/Backup and DR Strategy|Backup and DR Strategy]]
- [[12 Datasets/TrueNAS Storage Capture 2026-08-01|TrueNAS Storage Capture 2026-08-01]]
