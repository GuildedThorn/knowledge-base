## Purpose

Append-only log of the scheduled SIEM review passes. A systemd user timer on the workstation (`siem-review.timer`, 3x daily at 06:52 / 14:52 / 22:52) runs `~/.local/bin/siem-review.sh`, which pulls the last 9 hours from Loki and Prometheus on `soc` and has Claude review it like a tier-1 analyst. Non-OK verdicts also raise a desktop notification.

This is second-line review — Grafana's provisioned rules (see [SIEM-SOC Rollout](kb://08-improvements-siem-soc-rollout)) remain the real-time alert path. An entry saying "OK" is itself signal: a missing entry means the review pass stopped running.

---

## 2026-07-20 13:23

STATUS: ALERT — Loki unreachable, review pass skipped.

## 2026-07-20 13:24

STATUS: NOTABLE — internal host 192.168.1.6 SSH-scanned websites (07:50) then soc (08:20); identify the source

- **Internal SSH scanning, not internet noise:** 192.168.1.6 (LAN-side, not a Cloudflare/internet source) tripped Suricata on websites ("ET SCAN LibSSH Based Frequent SSH Connections Likely BruteForce", "ET SCAN Potential SSH Scan" → 172.16.25.50:22 at 07:50–07:52) and CrowdSec ssh-bf/ssh-slow-bf on **websites** (07:50–07:52) and then on **soc** (08:20–08:25). Sequential targeting of two hosts — including the SIEM — from an internal address is the unusual pattern worth a look.
- **Likely a scan, not password guessing:** flows are tiny (3–4 packets, ~290 bytes, libssh banner-style connects) and the fleet-wide sshd failure query returned **zero** auth failures, so this looks like connection/banner scanning (nmap/ssh-audit/libssh tool) rather than credential brute force. If 192.168.1.6 is the admin workstation running an authorized scan, downgrade to OK; otherwise investigate that host.
- **Audit CONFIG_CHANGE / sshd-config / modules events are deploy+boot artifacts:** perl activation-script writes with key=sshd-config and auditd rule remove/re-add on nixos (07:29), soc (08:25), plus modprobe storms on nixos (~08:56) and scout (~11:38) match NixOS activations and reboots. Note soc's activation at 08:25 coincides with the CrowdSec hits there — consistent with an admin session doing both.
- **Fleet health clean:** all Prometheus targets up, no failed systemd units, no comin deploy/build/eval failures, no pfSense perimeter priority 1–2 IDS alerts.
- **Volumes plausible:** nixos 645k / websites 386k / soc 131k lines; scout only 3.8k, consistent with the laptop being online briefly late in the window (it booted ~11:38). pfSense absent from the per-host journal volume vector but its Loki streams exist (suricata query processed its lines) and node exporter is up — likely a label difference, worth confirming the volume query covers pfsense.
- One sudo priv-exec on nixos (auid=1000, pts1, 07:28) — single interactive admin escalation, unremarkable.

**Triage (2026-07-20):** resolved — the 192.168.1.6 scan was Thorn (authorized self-scan). Device noted as admin-owned in the review script's prompt so future passes downgrade pure scanning from it.

## 2026-07-20 14:55

STATUS: NOTABLE — admin device (192.168.1.6) SSH sweep tripped crowdsec brute-force scenarios on websites and soc, but no matching sshd auth failures behind them

- **192.168.1.6 SSH activity stayed at scan level, but check the crowdsec side-effects.** Suricata on websites fired "LibSSH Frequent SSH Connections" / "Potential SSH Scan" at 07:50–07:52, and crowdsec logged `ssh-bf`/`ssh-slow-bf` for that IP on websites (07:50–07:52) and again on soc (08:20–08:24). Flow sizes (3–4 packets, ~300 bytes, drop right after banner) and a fleet-wide **empty sshd-failure query** say these were preauth connect/disconnects — banner scanning, not credential attempts — so this fits the confirmed self-testing and stays capped at NOTABLE. Worth confirming crowdsec didn't ban the admin IP, and that the 08:24 pass at the SIEM was part of the same test.
- **Audit "sshd-config"/"identity"/"priv-exec" events on nixos and soc are NixOS activation, not tampering.** The writes come from the perl activation script in /nix/store running as root (rename/symlink of sshd config, /run/wrappers regeneration), immediately followed by auditd rule remove/re-add — the normal signature of a rebuild/deploy. Prometheus shows zero comin deploy/build/eval failures, corroborating clean activations. nixos also rebooted mid-window (udev/modprobe module-load burst with fresh low PIDs).
- **scout logged only 3,780 lines vs 130k–650k for its peers, and isn't in Prometheus at all** — consistent with the roaming laptop being powered on only briefly (its boot-time audit rule load appears late in the window). Expected for that host, but noted since it means scout has near-zero monitoring coverage this window.
- All Prometheus targets up (node, loki, pfsense, comin ×3), no failed systemd units anywhere, and pfSense perimeter Suricata priority 1–2 was completely quiet — no external attack traffic worth mentioning this window.
- Only privileged execs in the audit trail are two `sudo` invocations on nixos by uid 1000 on pts/1 (interactive admin session) — nothing first-seen or unattended.

## 2026-07-20 22:53

STATUS: OK

- All monitored targets up in Prometheus (nixos, soc, websites, pfsense, Loki, and comin on all three NixOS hosts); zero failed systemd units and zero comin deploy/build/eval failures.
- No Suricata alerts from either sensor (websites EVE and pfSense priority 1–2), no CrowdSec scenario hits, and no sshd auth failures anywhere in the window — quieter than even normal background scanner noise, consistent with websites being reachable only via the Cloudflare tunnel.
- Audit keyed events (identity/privilege/priv-exec/sshd-config/modules/time-change) returned nothing across ~1.34M lines scanned — no first-seen or unusual privilege activity.
- scout is absent from both journal volume and Prometheus targets. That's internally consistent (silent in both systems, not a discrepancy), so it reads as the laptop simply being off or away — but it means the fleet has had no telemetry from it this window; worth confirming next time it should be online.
- Journal volumes look proportionate: nixos ~548k and websites ~531k lines with soc ~100k, in line with soc's lighter role; no host wildly diverging from peers.
- No activity of any kind from 192.168.1.6 in this window — nothing to attribute to admin self-testing.

## 2026-07-21 06:55

STATUS: OK

- All monitored targets are up in Prometheus (nixos, soc, websites, pfsense node/comin exporters, Loki), with zero failed systemd units and zero comin deploy/build/eval failures across the window.
- Security signal is quiet across the board: no Suricata EVE alerts on the websites sensor, no priority 1–2 perimeter Suricata hits on pfsense, no CrowdSec scenario triggers, and zero matches on the audit keys (identity/privilege changes, priv-exec, sshd config, kernel modules, time changes) despite ~1.47M lines scanned.
- Notably, zero sshd failures fleet-wide this window — consistent with websites sitting behind the Cloudflare tunnel rather than exposing SSH, and no internal brute-force noise either.
- scout (roaming laptop) is absent from both Prometheus and Loki, which is internally consistent — it's simply off-network, not a half-dead host. Worth confirming next time it checks in, but expected for a laptop.
- Journal volume distribution (nixos ~688k, websites ~528k, soc ~98k lines over 9h) shows no host wildly out of line with its role; soc being the quietest and the workstation the loudest is the normal shape.
- No activity of any kind observed from 192.168.1.6 in this window — nothing to assess against the authorized-scanning carve-out.

## 2026-07-21 14:55

STATUS: OK

- All monitored targets are up in Prometheus (nixos, soc, websites, pfsense node exporters, Loki, and all three comin instances); zero failed systemd units and zero comin deploy/build/eval failures in the window.
- No hits on any detection layer: pfSense Suricata priority 1–2 alerts, CrowdSec scenario triggers, and the keyed auditd queries (identity/privilege changes, priv-exec, sshd config, module loads, time changes) all returned empty over ~1.4M lines scanned.
- The only Suricata event on the websites sensor is a single severity-3 informational alert for `update.argotunnel.com` in TLS SNI from 172.16.25.50 — that's the host's own cloudflared client phoning Cloudflare, which is expected infrastructure for a tunnel-fronted VM.
- Journal volumes (nixos ~625k, websites ~533k, soc ~97k lines) look proportionate to each host's role; no host is wildly off from its peers. pfsense doesn't appear in the journal-volume vector, but its Suricata stream is clearly ingesting (2.7k lines processed), so log flow from the perimeter is intact.
- scout (roaming laptop) is absent from both Prometheus and Loki — consistent silence across both systems, i.e. simply offline, not a monitoring inconsistency.
- Minor observation, not actionable: the sshd-failure query processed zero lines on a window where scanner background noise is normally expected on websites. Most likely the Cloudflare tunnel is doing its job (no exposed SSH) or the query's stream selector matched nothing; if the next few reviews also show a flat zero, it's worth a one-time check that the query still matches the sshd log labels.

## 2026-07-21 22:56

STATUS: OK

- Single Suricata sev-1 hit on **websites**: a WordPress Gravity SMTP probe (CVE-2026-4020, `/wp-json/gravitysmtp/...`) from 195.178.110.211 via the Cloudflare tunnel at 20:46 CDT. One request, server returned 404, no follow-up traffic — consistent with routine internet-wide CVE scanning, not a targeted or successful exploit.
- **scout** rebooted around 15:41 CDT (audit rules re-added, boot-time modprobe burst) and shows three interactive `sudo` priv-exec events on pts0/pts2 for uid 1000 — matches normal admin use of the laptop, nothing running as an unexpected user or tty.
- pfSense perimeter Suricata (prio 1–2), sshd failures, and CrowdSec scenarios were all empty for the window; no brute-force or perimeter IDS activity beyond the one web probe above.
- All Prometheus targets are up, no failed systemd units, no comin deploy/build/eval failures. Note scout has no Prometheus scrape target but is shipping logs to Loki — expected for the roaming laptop, so no up/Loki inconsistency.
- Journal volumes (nixos 600k, websites 538k, soc 100k, scout 70k lines) are in normal proportion for a workstation and a public web VM versus the quieter hosts; nothing an order of magnitude off its peers' pattern.
- No first-seen processes, identity/privilege audit anomalies, sshd-config or time-change events, and no activity at all from 192.168.1.6 this window.

## 2026-07-22 06:56

You've hit your session limit · resets 7:50am (America/Chicago)

## 2026-07-22 14:56

STATUS: OK

- Quiet window overall: no pfSense Suricata priority 1–2 alerts, no CrowdSec scenario hits, no sshd auth failures fleet-wide, and zero audit-keyed events (identity/privilege/module/time-change) across all hosts.
- All Prometheus targets are up (node exporters, pfSense, Loki, comin on all three NixOS hosts), no failed systemd units, and no comin deploy/build/eval failures — the fleet is healthy and deploys are clean.
- The only Suricata activity on the websites sensor is a single long-lived ICMP echo flow from 192.168.1.6 (admin device) to 172.16.25.50, pinging every ~30 seconds since 13:44 local — consistent with an uptime/monitoring ping or authorized self-testing, informational severity only, no auth or payload activity from that source.
- scout logged only ~3.7k journal lines versus 350k–684k on its peers; as a roaming laptop with no Prometheus scrape target this most likely means it was asleep or off-network most of the window, but worth a glance if it was expected to be online today.
- Journal volumes on nixos (684k), websites (556k), and soc (352k) are mutually consistent for a 9-hour window; no host is simultaneously up in Prometheus but silent in Loki (pfSense ships Suricata logs, not journald, as expected).

## 2026-07-22 22:55

STATUS: OK

- **No threshold-adjacent security events fired.** sshd failures, CrowdSec scenario hits, pfSense perimeter Suricata prio 1–2, and audit keyed events (identity/privilege/priv-exec/sshd-config/modules/time-change) all returned zero across the 9h window.
- **All hosts healthy.** Prometheus `up` = 1 for every node/comin/loki target (soc, nixos, websites, pfsense); no failed systemd units and no comin deploy/build/eval failures.
- **Only Suricata activity is admin-box ICMP.** Every alert on the websites sensor is "GPL ICMP PING *NIX" (informational, sev 3) from 192.168.1.6 → 172.16.25.50 — the admin's own device doing echo probes to the web VM's internal IP. Pure scanning from that host, well within the confirmed self-testing baseline; no auth attempts or payloads accompany it, so it does not escalate.
- **Journal volumes track host roles.** nixos 782k (workstation) > websites 542k (public web VM) > soc 381k (SIEM) > scout 59k (roaming laptop, expected low). No host is silent-while-up or wildly off its peers.
- **Minor note, not a gap:** pfSense is absent from the per-host journald volume vector but is `up` in Prometheus and does ship logs (its Suricata query scanned 2337 lines) — consistent with FreeBSD not using journald, not a Loki/Prometheus inconsistency.

## 2026-07-23 06:56

STATUS: NOTABLE — nixos audit cluster rewrote /etc/shadow, sshd config, and removed sudo/su audit rules (activation-style, confirm it was an intended rebuild)

- **nixos privileged audit burst (~01:11 window):** an unset-auid (auid=4294967295) nix-store `perl` running as root fired `identity` (rename/chown on passwd/shadow-class files), `sshd-config`, `privilege`, and `modules` keys, plus `CONFIG_CHANGE op=remove_rule` deleting the `priv-exec` audit rules on `/run/wrappers/bin/sudo` and `/su`. Signature is a textbook NixOS activation/rebuild footprint (system context, nix-store perl, clustered timestamps) — almost certainly a legit deploy, but it's exactly the "privileged config tampering" shape, so confirm a rebuild ran on nixos. Only `remove_rule` events are visible here; a human should verify the rules were re-added.
- **Interactive sudo on nixos looks normal:** two `priv-exec` events with auid=1000/uid=1000, tty=pts4, ses=4 — the admin using sudo directly. Consistent with a hands-on session (matching the rebuild above).
- **Perimeter/edge clean:** pfSense Suricata prio 1–2 empty, sshd failures empty, CrowdSec scenario hits empty, no failed systemd units, no comin deploy/build/eval failures. No threshold-rule territory triggered.
- **Admin box (192.168.1.6) only pinging:** all websites-sensor Suricata alerts are informational `GPL ICMP PING *NIX` from 192.168.1.6 → 172.16.25.50, a single long-lived flow. ICMP only, no scan/auth/payload — below the NOTABLE cap for authorized self-testing; noted for completeness.
- **Log volume sane vs peers:** nixos 1.21M (workstation, expected high), websites 527k, soc 487k. scout at 940 lines is low but it's the roaming laptop and has no Prometheus node target, so it's away/mostly-off — not an up-but-silent inconsistency.
- **No Prometheus/Loki inconsistencies:** every host reporting `up=1` (nixos, soc, websites, pfsense, loki, comin×3) is also producing logs; nothing up-in-Prometheus-but-dark-in-Loki.

## 2026-07-23 14:53

STATUS: NOTABLE — nixos journal volume ~20–28× below the two servers; sustained admin ICMP to websites

- **nixos log volume far below peers**: nixos 23,244 vs soc 644,069 and websites 530,463 lines this window. Likely just workstation-vs-server role difference and nixos shows `up=1`, but a 20–28× gap is worth a glance to confirm journald/promtail isn't silently dropping on the workstation.
- **Admin box (192.168.1.6) sustained ICMP ping to websites** (172.16.25.50): a single flow started 01:58 and kept re-firing GPL ICMP PING *NIX every ~30s for 1,400+ packets across the window. Informational sev-3, pure ping from the admin device → consistent with authorized self-testing; capped at NOTABLE. No auth attempts, payloads, or lateral movement from that IP.
- **scout (roaming laptop) is dark**: absent from both Loki journal volume and Prometheus `up`. Expected for an off-network roaming host, but confirm it's intentionally offline and not a dropped agent.
- **Perimeter and threshold surfaces are clean**: pfSense suricata prio 1–2 empty, sshd failures none, CrowdSec scenario hits none, no audit identity/privilege/module/time-change events.
- **Fleet health green**: all node/comin/loki/pfsense targets `up=1`, zero failed systemd units, zero comin deploy/build/eval failures. pfSense up in Prometheus with no journald stream is expected (ships suricata only, which was empty).
- **Internal consistency holds**: every Prometheus-up host that should ship to Loki did (nixos/soc/websites present); no "up but silent" mismatches beyond the expected pfSense/scout cases.

## 2026-07-23 18:25

STATUS: NOTABLE — authorized RED-team exercise (out-of-band, not a scheduled pass): full unauth→admin chain proven against OWASP Juice Shop v20.1.1 on localhost:3000

- **This is an operator-run exercise, not the timer pass.** Target is a deliberately-vulnerable lab app (`localhost:3000`), so the findings are expected — logged here so the chain and its IOCs are on record and don't read as an unexplained intrusion if they surface in fleet telemetry. Full write-up: [[Juice Shop Assessment 2026-07-23]].
- **Chain proven end-to-end, non-persistent (no writes, no data mutation):** `/ftp` directory-listing → Poison-Null-Byte (`%2500.md`) bypass of the `.bak` extension filter (403→200) exfiltrated a 750 KB lockfile → SQLi login `' OR 1=1--` returned an RS256 admin JWT (id=1, `admin@juice-sh.op`, role=admin) with no password → stolen token dumped all 22 users via `/api/Users` (200). Password field is stripped in v20; emails/roles/lastLoginIp/deluxeToken are not.
- **SCA (Crossview + osv-scanner) on the leaked lockfile:** 144 vulnerable packages, 324 advisories, **184 unique CVEs** — heaviest in tar/handlebars/lodash/jsonwebtoken/js-yaml (proto-pollution, template-RCE, JWT-verification gadgets).
- **Detection notes for the real SOC (what to alert on if this pattern ever hits production assets):** `%2500` / null-byte in request URIs, especially a 403→200 flip on the same path; `' OR 1=1--` (and SQL metacharacters) in login request bodies; a single freshly-issued token immediately performing a full-table `/api/Users` read. None of these are Juice-Shop-specific.
- **No impact to the monitored fleet.** This exercise ran against the isolated lab target only; nixos/soc/websites/pfsense unaffected. Cross-refs: [[SOC Live Status]], [[Security Map]].

## 2026-07-23 22:52

STATUS: OK

- **Clean window across all threshold-adjacent channels:** zero sshd auth failures, zero CrowdSec scenario hits, zero pfSense perimeter Suricata prio 1-2 events, zero audit keyed events (identity/privilege/priv-exec/sshd-config/modules/time-change), no failed systemd units, and no comin deploy/build/eval failures on any host.
- **Only IDS activity is benign admin self-test:** every websites-sensor Suricata alert is `GPL ICMP PING *NIX` (sev-3 informational) from 192.168.1.6 → 172.16.25.50, a single sustained flow (~113 pings, one every ~30s, 21:54→22:51). This is the admin box doing pure ICMP against the web VM's internal IP — no scanning-beyond, no auth, no payloads — so it stays within the authorized-self-test exemption; likely a connectivity/uptime probe.
- **All monitored hosts up:** Prometheus `up=1` for every node/comin/loki/pfsense target; pfSense reporting via its exporter as expected (its absence from journal volume is normal — non-systemd host).
- **scout inconsistency (minor, expected for a roaming laptop):** shipping Loki journal (988 lines) but has no Prometheus node/comin scrape target — logging alive, just unmonitored. No action, noting for baseline.
- **Journal volumes consistent with roles:** websites highest (531k) as the public web VM, soc 147k (SIEM), nixos 24k, scout 988 (mostly offline laptop) — no host far off its expected profile; nothing resembling a log-flood or a silent-but-up host.
- **No first-seen process/auth/audit anomalies surfaced** in the 9h window; nothing warranting escalation beyond what threshold rules already cover.
