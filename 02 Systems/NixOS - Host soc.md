---
summary: "Document the `soc` host, composed in `modules/computers/soc.nix` — the SIEM/observability hub the entire fleet reports to."
status: active
tags: [systems, host]
---

## Purpose

Document the `soc` host, composed in `modules/computers/soc.nix` — the SIEM/observability hub the entire fleet reports to. See [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]] for the capability-level picture; this note covers the host itself.

## Role

Headless Proxmox VM running Loki, Prometheus, and Grafana. Every host ships its journal here via Alloy, Prometheus scrapes (or receives pushes from) the fleet, and Grafana evaluates the `siem` alert rules and pages Discord. It is deliberately defended like a target, not just infrastructure — an attacker who reaches `soc` can rewrite the record of how they got in — so it runs CrowdSec, the detection canary, and key-only SSH itself.

## Composition

- `thorn-core` base bundle (which includes `services-observability` and `services-audit` fleet-wide)
- service modules: CrowdSec (detect-only), detection canary, SSH
- `qemu-guest.nix` profile (Proxmox VM)
- `hosts/soc/hardware-configuration.nix`, `disko.nix`, `networking.nix`, `secrets.nix`
- provisioned Grafana dashboards live in-repo at `hosts/soc/dashboards/` (SOC Overview, Fleet Health, Fleet Deploys, Endpoint Activity, Pipeline Health)

## Notable Host Behavior

- **Loki** (`:3100`) keeps only its WAL and caches on the VM disk; chunks and index live in a SeaweedFS S3 bucket (`loki`) on [[03 Devices/TrueNAS|TrueNAS]] at `truenas.guildedthorn.arpa:30304`, over HTTPS verified against the ThornCloud CA. 90-day retention. The VM is rebuildable without log loss.
- **Prometheus** (`:9090`) keeps 90 days on the VM disk, with a daily restic backup of the TSDB to a `prometheus-backup` bucket on the same NAS (keep 7 daily / 4 weekly / 3 monthly). The snapshot API route was deliberately rejected: enabling the admin API would hand every LAN host a delete-series endpoint. The remote-write receiver is enabled so roaming hosts (`scout` over WireGuard) can push metrics they can't be scraped for.
- Scrape jobs cover only the always-on hosts (`nixos`, `soc`, `websites`) plus pfSense's node_exporter by IP, Loki's own metrics (so the SIEM going blind is alertable), and every host's `comin` deploy metrics.
- **rsyslog on UDP 5514** fronts appliance syslog: pfSense's FreeBSD syslogd emits RFC3164 with no hostname field, which Alloy's strict parser rejects, so rsyslog accepts it, files it per-source under `/var/log/remote`, and Alloy tails those into Loki as `job="syslog"`.
- **Grafana** (`https://soc.guildedthorn.arpa:3000`) with a ThornCloud_CA-signed cert (cert in-repo, key in sops). Datasources, dashboards, Discord contact point, severity-split notification policy, and the whole `siem` alert-rule group are Nix-provisioned — see [[09 Observability/Grafana|Grafana]].
- Headless, so `thorn.audit.execScope = "all"` — under the default "sessions" scope nothing would ever be recorded here, and the canary requires it.
- sops secrets (age key derived from the host SSH key): Loki/restic S3 credentials, restic repo password (not recoverable — also keep it in a password manager), Grafana admin password, secret key, Discord webhook, and TLS private key.
- Static `172.16.25.51/24` on `eth0` (predictable NIC names disabled), gateway/DNS via pfSense; firewall opens only 22, 3000, 3100, 9090. IPv6 disabled like the rest of the fleet.
- BIOS boot via GRUB forced to a single device (same disko duplicate-entry workaround as `websites`), ext4 root plus 8G swap on `/dev/sda`.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[01 Maps/Observability Map|Observability Map]]
- [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]]
- [[09 Observability/Grafana|Grafana]]
- [[03 Devices/TrueNAS|TrueNAS]]
- [[02 Systems/NixOS - Host websites|Host websites]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
