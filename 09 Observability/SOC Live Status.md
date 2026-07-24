---
title: SOC Live Status
type: dashboard
updated: 2026-07-23T20:06Z
---

## Purpose

The in-world anchor for ThornCloud's SOC — a persistent orb you fly to instead of a floating Grafana tab. It holds the **last live snapshot** pulled straight from the real Loki + Prometheus APIs on the `soc` VM (`172.16.25.51`), plus how to refresh it and where to dig deeper. Design lives in [SIEM and SOC - Architecture](kb://09-observability-siem-and-soc-architecture); status of the buildout in [SIEM-SOC Rollout](kb://08-improvements-siem-soc-rollout).

## Live snapshot — 2026-07-23 20:06 UTC

> ● **OPERATIONAL** — all clear, pipeline alive, no real detections.

- **Fleet:** node 3/3 · comin 3/3 · loki 1/1 · pfsense 1/1 — every scrape target up.
- **Down:** none.
- **Detections:**
  - sshd brute-force (10m): **none** (real sshd `Failed password` = 0).
  - suricata (1h): 95 total, **0 high-severity** — all low-sev `GPL ICMP PING *NIX` from `192.168.1.6 → websites`; benign noise, not an attack.
  - canary (30m): `soc` = 4 · `websites` = 6 — detection pipeline provably alive.
- **Heartbeat (real host log lines / 5m, obs-stack excluded):** websites 4.8k · nixos 209 · soc 5.

## Detection scoping — read before trusting counts

An early cut of the cockpit cried wolf: it matched the string `failed password` / `siem-canary-probe` *anywhere* in the journal, which caught **Loki's and Grafana's own query-logs echoing the cockpit's LogQL text** back through the journal — a feedback loop that faked a 150-event "brute-force." Fixed by scoping:

- brute-force → `unit=~"sshd.*"` and exact `Failed password` only.
- suricata → alarm only on `alert_severity <= 2` (ICMP ping is sev 3).
- canary + heartbeat → exclude `loki.service` and `grafana.service`.

If you add detections, scope them to a real source unit or they'll count the observability stack watching itself.

## Refresh it live

The station **SOC console (terminal 900)** is `thorn@nixos` with LAN reach to the whole stack. Re-run the cockpit any time:

```
python3 ~/soc-cockpit.py     # alias: soc
```

Companion pivots on the same console: `~/soc-pivot.py` (top Suricata signatures + src/dest), `~/soc-ssh.py` (top SSH source IPs / usernames). Update this note's snapshot from their output when the picture changes.

## Full dashboards

Grafana at `https://soc.guildedthorn.arpa:3000` — SOC Overview, Fleet Health, Fleet Deploys, Endpoint Activity, Pipeline Health.

## Related

- [SIEM and SOC - Architecture](kb://09-observability-siem-and-soc-architecture)
- [SIEM-SOC Rollout](kb://08-improvements-siem-soc-rollout)
- [NixOS - Host soc](kb://02-systems-nixos-host-soc)
- [Grafana](kb://09-observability-grafana)
- [Observability Map](kb://01-maps-observability-map)
