---
summary: Architecture of ThornCloud's SIEM/SOC.
status: active
tags: [observability]
---

## Purpose

Architecture of ThornCloud's SIEM/SOC. The whole capability runs **natively in the `ThornixOS` flake** — no appliances — on a dedicated `soc` VM, deployed via `comin` GitOps and secured with sops-nix like every other host. This note is the design at a glance; [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]] tracks what is live and what remains.

## Placement

- A dedicated headless **`soc` VM** (`hosts/soc/` + `modules/computers/soc.nix`) on the `proxmox` hypervisor ([[03 Devices/Mac Pro 5,1|Mac Pro 5,1]]), defended like the rest of the fleet (key-only SSH, CrowdSec, its own detection canary).
- Evidence lives off-box: Loki chunks/index and Prometheus backups land in SeaweedFS S3 buckets on [[03 Devices/TrueNAS|TrueNAS]], so the VM is rebuildable without log loss.

## Data flow

1. **Host telemetry (every host, via `thorn-core`)** — Grafana **Alloy** ships each host's journal to Loki (buffering when `soc` is unreachable); **node_exporter** exposes metrics on `:9100`; **auditd** watches identity files, `/etc/ssh`, kernel-module syscalls, clock changes, and priv-exec, plus execve behind `thorn.audit.execScope` (`all` on headless hosts). The roaming `scout` laptop remote-writes metrics over WireGuard.
2. **Aggregation on `soc`** — **Loki** (`:3100`, 90-day retention) for logs and **Prometheus** (`:9090`, 90-day + daily restic backup to the NAS) for metrics. **rsyslog** on UDP 5514 fronts pfSense's non-standard FreeBSD syslog and Alloy tails it into Loki as `job="syslog"`.
3. **Detection** — **Suricata** af-packet IDS on `websites` (EVE JSON → Loki) and a second Suricata instance on pfSense at the perimeter; **CrowdSec** detect-only on `nixos`/`websites`/`soc`; **ClamAV** on most hosts; and a **detection canary** on `soc`/`websites` that continuously proves the auditd → journal → Alloy → Loki → query chain is alive.
4. **Presentation & alerting** — **Grafana** (`https://soc.guildedthorn.arpa:3000`, ThornCloud_CA TLS), fully provisioned from the repo: Loki + Prometheus datasources, five SIEM dashboards, and a `siem` alert group (1-minute eval). Alerts fan out to **Discord** via a sops-held webhook, split on a `severity` label (critical pages fast and re-notifies; warnings batch).

## Secrets

The Grafana cert key, the Discord webhook, and any credentials go through **sops-nix**, delivered via `$__file{}` so they never touch the Nix store — the same pattern `nixos` and `websites` already use (see [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]).

## Why native-nix rather than an appliance

Every piece is a `modules/services/*.nix` in the dendritic pattern: reproducible, `comin`-deployed, sops-managed, and diffable — no unmanaged box drifting outside the flake. Heavyweight SIEM stacks (Elastic, Wazuh, TheHive/Cortex, Arkime) were deliberately not adopted: auditd + journal shipping covers host telemetry, Grafana + Loki + Prometheus covers indexing / dashboards / alerting, and Discord covers fan-out — enough for a one-person SOC without the operational weight. Case management is intentionally unhandled.

## Open questions

- Does the `proxmox` hypervisor (Mac Pro 5,1) have spare capacity for growth alongside its current guests, or does it need a resource audit first?
- East-west visibility: `websites`' Suricata only sees its own traffic — a SPAN/mirror port feeding a dedicated sensor (the `mitm` host) would cover inter-subnet traffic. Tracked in [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]].

## Related

- [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]]
- [[99 Archive/SIEM and SOC - Kali Purple Proposal (superseded)|Kali Purple Proposal (superseded)]] — the earlier appliance-based plan that was rejected
- [[01 Maps/Observability Map|Observability Map]]
- [[09 Observability/Grafana|Grafana]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
- [[05 Network/VLANs|VLANs]]
- [[03 Devices/Mac Pro 5,1|Mac Pro 5,1]]
- [[03 Devices/pfSense Router|pfSense Router]]
