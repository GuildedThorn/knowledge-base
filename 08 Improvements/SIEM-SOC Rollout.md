---
summary: "Track the rollout of the SIEM/SOC capability — built natively in the `ThornixOS` flake, deployed via `comin` GitOps like everything else (design in SIEM and SO…"
status: in-progress
tags: [improvements]
---

## Purpose

Track the rollout of the SIEM/SOC capability — built natively in the `ThornixOS` flake, deployed via `comin` GitOps like everything else (design in [[09 Observability/SIEM and SOC - Architecture|SIEM and SOC - Architecture]]). This note tracks what is live and what remains.

## Current State — What Is Built

### The `soc` host

A dedicated headless VM (`hosts/soc/` + `modules/computers/soc.nix`), defended like the rest of the fleet (key-only SSH, CrowdSec, its own detection canary — an attacker who reaches `soc` can rewrite the record of how they got in):

- **Loki** (`:3100`) — every host's journal lands here. Chunks and index live in a SeaweedFS S3 bucket on [[03 Devices/TrueNAS|TrueNAS]] (`truenas.guildedthorn.arpa:30304`, bucket `loki`, HTTPS with the ThornCloud CA), so the VM is rebuildable without log loss. 90-day retention.
- **Prometheus** (`:9090`) — 90-day retention on the VM disk, with a daily restic backup of the TSDB to a `prometheus-backup` bucket on the NAS (keep 7 daily / 4 weekly / 3 monthly). Remote-write receiver enabled for roaming hosts. Scrape jobs: `node` (always-on hosts: `nixos`, `soc`, `websites`), `pfsense` (node_exporter on `172.16.25.1:9100`), `loki` (self-monitoring, so the SIEM going blind is itself alertable), and `comin` (`:4243` — deploy state, so a host silently running a stale config is a query, not an SSH session).
- **Syslog ingest for appliances** — rsyslog on UDP 5514 fronts pfSense's non-standard FreeBSD syslog (no hostname field, which Alloy's strict parser rejects), writes one file per source under `/var/log/remote`, and Alloy tails those into Loki as `job="syslog"`.
- **Grafana** (`https://soc.guildedthorn.arpa:3000`) — TLS via a ThornCloud_CA-signed cert (key in sops), provisioned entirely from the repo: Loki + Prometheus datasources and five dashboards in a SIEM folder (`hosts/soc/dashboards/`): SOC Overview, Fleet Health, Fleet Deploys, Endpoint Activity, Pipeline Health. Repo JSON is the source of truth; UI edits survive only until the next deploy.
- **Alerting to Discord** — webhook in sops, delivered via `$__file{}` so it never touches the Nix store. Notification policy splits on a `severity` label: critical (active hostility, or the SIEM blind) pages at 10s/1m and re-notifies hourly; warnings batch at 30s/5m/4h.

### Alert rules (Grafana `siem` group, 1-minute eval)

- Host down (node exporter unreachable, 5m)
- systemd unit failed (10m)
- SSH brute force — >10 failed logins on one host in 10m (**critical**)
- Suricata IDS alert from EVE JSON (**critical**)
- pfSense perimeter Suricata priority 1–2, matched in the raw syslog stream (**critical**)
- CrowdSec scenario triggered (detect-only today)
- comin deploy failed / build-or-eval failed — a host silently on its previous generation
- Loki unreachable (**critical**, alerts on NoData)
- Detection canary silent per canary host (**critical**, see below)
- Log silence per always-on host (**critical**, alerts on NoData — LogQL returns an empty vector, not zero, for a silent host, so NoData=Alerting is load-bearing)

### Fleet-wide telemetry (in `thorn-core`, so every host)

- `services-observability` — Grafana Alloy ships the journal to Loki (buffers and retries when `soc` is unreachable); node_exporter on `:9100`; comin metrics port opened for scraping.
- `services-audit` — auditd baseline: watches on identity files (`/etc/passwd`, `group`, `shadow`, `sudoers`), `/etc/ssh`, kernel module syscalls, clock changes, and `priv-exec` on the su/sudo wrappers, plus **execve auditing** behind a `thorn.audit.execScope` option: `"sessions"` (auid-carrying processes only) on desktops, `"all"` on headless hosts (`soc`, `websites`) where nobody logs in and a web-shell would otherwise run unwatched. Audit events reach Loki through the normal journal path — no extra plumbing.
- `scout` (roaming laptop) adds `services-observability-roaming`: Alloy remote-writes node and comin metrics over WireGuard with labels matching the pull-based jobs, so it appears in the same dashboards.

### Detection layers per host

- **Suricata** on `websites` (`services-suricata`) — af-packet alert-only IDS on `lo` + `eth0`, because public ingress is a Cloudflare tunnel and the decrypted HTTP lives on loopback. ET Open + abuse.ch SSLBL + traffic-id rulesets, BPF-scoped to `ip or ip6 or arp`, EVE JSON (alert/anomaly/ssh) shipped to Loki, NIC offloads disabled for wire-faithful capture, and a SIGUSR2 live reload so daily rule updates actually reach the running engine (they didn't, for weeks, before that fix).
- **CrowdSec** detect-only on `nixos`, `websites`, `soc` — self-contained local LAPI (`127.0.0.1:8083`), linux + sshd collections, fed from the journal via a `_TRANSPORT=syslog` acquisition. No bouncer installed yet, so nothing is blocked.
- **ClamAV** on most hosts (`services-clamav`).
- **Detection canary** on `soc` + `websites` (`services-canary`) — a `siem-canary-probe` no-op runs every 10 minutes; the only trace it leaves is its execve audit record, and a Grafana rule alerts if that record stops arriving in Loki (30m window tolerates two misses). This tests the entire auditd → journal → Alloy → Loki → query chain, and exists because that chain *did* silently break once: a wrong LogQL filter left every audit panel empty for weeks, indistinguishable from a quiet fleet. Requires `execScope = "all"` (asserted in the module) — timer-spawned processes have no auid.
- pfSense additionally runs its **own Suricata package** at the perimeter, feeding the syslog path — resolving what the original plan left as an open question.

There is also a CRT SOC display on the workstation (`thorn.desktop.crt`) showing the live log feed — decoration, but it keeps the pipeline visibly alive.

### Deliberately not adopted

Heavyweight SIEM appliances (Elastic, Wazuh, TheHive/Cortex, Arkime) were not adopted. auditd + journal shipping fills the host-telemetry role; Discord fills the alert fan-out role (via webhook, not [[07 Projects/ThornBot/ThornBot - Overview|ThornBot]]); case management is unhandled and probably unnecessary for a one-person SOC.

## Tasks

### Quick wins (an evening each)

- [ ] **Fire-drill the alert path.** The canary alert has never actually fired end-to-end. Stop `siem-canary.timer` on `soc` for 40 minutes, watch for the Discord ping, restart. Do the same for one Prometheus rule (stop node-exporter somewhere). Untested detection is a hypothesis, not a control.
- [ ] **DNS visibility.** pfSense's Unbound is the LAN's DNS — turn on query logging and ship it to Loki over the existing syslog path (UDP 5514). Highest-value missing log source: C2 domains, DGA patterns, exfil, "which device suddenly started resolving weird TLDs." Add an RPZ blocklist while in there and blocking comes almost free.
- [ ] **Widen Suricata's EVE types on `websites`.** Only `alert`, `anomaly`, `ssh` ship today. Adding `dns`, `tls`, `flow` turns the sensor into a proper NSM telemetry source (JA3/JA4, SNI, flow records) instead of an alarm bell. Volume is modest on a web VM.
- [ ] **pfSense filterlog.** If block logs aren't in the `job="syslog"` stream yet, ship them — "top blocked sources hitting the WAN" and "LAN device suddenly blocked outbound" are dashboards that write themselves.
- [ ] **Interim hypervisor/NAS telemetry.** The layer under the SIEM is currently blind: the Proxmox hypervisor (the box `soc` runs on) and TrueNAS (the box its evidence lives on) ship no logs or metrics. The proper fix is blocked (see Blockers), but the interim isn't: stock PVE is Debian — point rsyslog/journald at `soc:5514` and `apt install prometheus-node-exporter`; TrueNAS has a remote-syslog setting in the UI. Reversible, doesn't touch guest storage, and gets discarded naturally when the migration happens.

### The real XDR move (a weekend)

- [ ] **Graduate CrowdSec from detect to respond.** Run the LAPI centrally on `soc`, register the existing machines, put the firewall bouncer on pfSense — then a scenario tripping on `websites` drops the attacker's IP at the perimeter for every host. That detect→decide→respond loop is what makes this XDR rather than a very nice logging pipeline. Start with conservative ban times.
- [ ] **A whole-LAN sensor.** `websites`' Suricata only sees its own traffic. A SPAN/mirror port on the switch feeding a dedicated sensor (the `mitm` host's name is begging for the job) gives east-west visibility — the IoT-to-everything traffic nobody currently watches. Blocked on network isolation (no VLANs — see [[05 Network/VLANs|VLANs]]).

### Structural (ongoing)

- [ ] **Vulnerability inventory, the Nix way.** The store holds a complete, exact software inventory per host. Run vulnix (or nixpkgs advisory scanning) against each host's toplevel in CI, export counts to Prometheus, alert on new criticals. Asset + vuln management nearly free — a genuinely unfair advantage of the platform.
- [ ] **Deception beyond the pipeline canary.** Extend the canary idea to intrusion detection: an SSH honeypot on an unused IP (endlessh or opencanary), a fake credential file on `websites` with an audit `-w` watch, canary DNS names that should never be resolved. Near-zero false-positive rate — a hit *means* something, which on a one-person SOC beats any volume of maybe-alerts.
- [ ] **Tune the auth detections already collected.** `activation`'s perl legitimately touches `/etc/passwd` on every deploy, so a naive identity alert would false-positive constantly. Alert on identity/priv-exec events where `auid` is a real user, or outside a comin deploy window — turning dashboard-only audit keys into alertable signals.
- [ ] **Purple-team loop.** Carve out an isolated segment, stand up a disposable target, run an attack scenario end-to-end, and confirm the expected detections fire. Blocked on network isolation (no VLANs — see [[05 Network/VLANs|VLANs]]).

## Blockers

- **Network isolation** — the whole-LAN SPAN sensor and the purple-team segment both need traffic isolation. There are no VLANs (see [[05 Network/VLANs|VLANs]]), so this means a switch SPAN/mirror port for the sensor and a dedicated physical interface/subnet on pfSense (or introducing VLANs specifically for this) for the isolated red-team segment.
- **Hypervisor migration** — properly managed (GitOps/Nix) monitoring of the Proxmox box means moving the hypervisor itself to NixOS-Proxmox, which would destroy the existing guests (`websites`, `soc`, `proxmox-guest`). Deliberately deferred until there's a migration path for the VMs; only the *managed* version is blocked, not visibility (see the interim-telemetry task above).

## Done Looks Like

- Every alert rule has fired at least once, on purpose, and reached Discord.
- Something blocks automatically (CrowdSec bouncer on pfSense) instead of only detecting.
- East-west traffic has a sensor on it, not just `websites`.

## Related

- [[09 Observability/SIEM and SOC - Architecture|SIEM and SOC - Architecture]]
- [[09 Observability/Grafana|Grafana]]
- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[08 Improvements/Network Improvements|Network Improvements]]
- [[05 Network/VLANs|VLANs]]
- [[03 Devices/TrueNAS|TrueNAS]]
- [[03 Devices/pfSense Router|pfSense Router]]
