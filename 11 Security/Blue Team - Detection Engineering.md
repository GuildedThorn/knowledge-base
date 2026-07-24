---
summary: Detection engineering methodology and blue-team framework — Sigma rules, threat hunting, MITRE D3FEND, log source prioritization, alert tuning, purple teaming.
status: active
tags: [security, blueteam, detection-engineering]
private: false
---

## Purpose

Defensive counterpart to the offensive [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index) — the methodology layer for building and validating detections, complementing ThornCloud's live [SIEM/SOC](kb://09-observability-siem-and-soc-architecture) (Loki + Prometheus + Grafana, auditd, Suricata, CrowdSec). Compiled 2026-07-24.

## Detection Engineering Lifecycle (Detection-as-Code)

**hypothesis → data source mapping → author → test → deploy → monitor → tune → retire.** Hypotheses come from threat intel, ATT&CK coverage-gap analysis, or purple-team findings.

- **Author**: rules in structured, version-controlled formats (Sigma YAML, or a platform DSL) committed to Git — not clicked together in a SIEM UI.
- **Test**: CI/CD validates rule syntax/schema and replays known-good and known-malicious log samples before merge (the detection analog of [Atomic Red Team](kb://11-security-tools-atomic-red-team)).
- **Deploy**: phased/shadow rollout before full enforcement, to catch false-positive storms early.
- **Tune**: track hit rate, alert fidelity, and suppression rate as first-class metrics feeding back into revision.
- **Retire**: rules carry a lifecycle status and get formally deprecated — stale rules are maintenance debt, not free coverage.

## Sigma Rules

SIEM-agnostic YAML detection format — write once, compile to many backend query languages.

```yaml
title: Okta User Account Locked Out
id: 14701da0-4b0f-4ee6-9c95-2ffb4e73bb9a
status: test          # stable | test | experimental | deprecated
logsource:
  product: okta
  service: okta
detection:
  selection:
    displaymessage: Max sign in attempts exceeded
  condition: selection
level: medium          # informational | low | medium | high | critical
tags: [attack.impact]  # ATT&CK tactic/technique mapping
```

Field modifiers use pipe syntax: `ScriptBlockText|contains: "..."`, `|startswith`, `|endswith`, `|re`. `logsource` + `detection` (named selections) + `condition` (boolean combination) is what actually fires.

**Backend conversion**: `pySigma` is the core library; backend plugins (`pySigma-backend-loki`, `-splunk`, `-microsoft365defender`, etc.) translate. `grafana/pySigma-backend-loki` is directly relevant to a Loki-based stack — it emits raw LogQL or Loki ruler YAML. `sigma-cli` drives it: `sigma convert -t loki sigma/rules/windows/sysmon/ -p sysmon -p loki_promtail_sysmon` (the `-p` processing pipeline maps Sigma's generic field names onto the target schema).

**Ruleset**: [github.com/SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) — Generic Detection Rules (technique-based), Threat Hunting Rules (broader/exploratory), Emerging Threat Rules (APT/CVE-specific). Treat as an upstream feed to vendor and filter, not something to trust blind.

## Threat Hunting Frameworks

**Pyramid of Pain** (David Bianco) — indicator types ranked by attacker cost to evade detection, bottom to top: hash values → IP addresses → domain names → network/host artifacts → tools → **TTPs**. Hashes/IPs are trivial to rotate; detecting TTPs forces the attacker to redesign tradecraft. Prioritize detection-engineering effort at the top of the pyramid — behavioral/TTP-based rules over static IOC blocklists.

**Hypothesis-driven hunting**: map existing detections against the ATT&CK matrix, find techniques with weak/zero coverage, form a hunt hypothesis, hunt manually against telemetry, and any validated finding becomes a permanent automated detection — the loop that turns one-off hunts into lasting capability.

## MITRE D3FEND

The defensive counterpart to ATT&CK — countermeasures mapped to techniques via an intermediate "digital artifacts" ontology explaining *why* a defense counters a technique. Tactical categories: **Model, Harden, Detect, Isolate, Deceive, Evict, Restore**. Example: T1003 credential dumping maps to Harden→credential-hardening + Detect→process-analysis countermeasures. For each ATT&CK gap a hunt surfaces, look up the D3FEND technique to find the concrete control, not just "write a detection."

## Log Source Prioritization

Ranked by detection value per ingest cost: **authentication logs** (highest value) → **process creation/execve** (Windows 4688 with command-line logging, or Linux auditd/execve — ThornCloud already runs this fleet-wide via [SIEM-SOC Rollout](kb://08-improvements-siem-soc-rollout)'s `services-audit`) → **DNS query logs** (cheap, reveals C2 beaconing/tunneling/known-bad domains) → cloud/app audit logs → firewall/proxy/EDR. NetFlow gives pattern/volume visibility (beaconing intervals, volume spikes) as a corroborating signal, not a primary source. Common blind spots: missing AD/cloud audit logs, command-line auditing disabled, DNS logs excluded for volume.

## Alert Tuning / False-Positive Reduction

**Baseline** normal behavior per host/user/automation account before writing thresholds. **Allowlist** known-good automation explicitly rather than loosening the rule itself. **Suppress/tag** known-benign recurring hits without disabling the rule. Audit rules periodically and kill high-noise/low-value ones outright. Static rules give deterministic, explainable, low-maintenance coverage for known TTPs; statistical/UBA baselining catches novel behavior but is only as good as the baseline — the two are complementary, not substitutes. Track hit rate *and* suppression rate as ongoing metrics, not just alert count.

## Purple Teaming Loop

**Attack → Observe → Fix → Validate.** Red team executes a specific ATT&CK technique, blue team checks in real time whether the detection fired, gaps get patched (new Sigma rule or D3FEND-mapped control), same technique re-run to confirm closure. [Atomic Red Team](kb://11-security-tools-atomic-red-team) is the standard tool — each atomic scoped to one technique, self-contained, scoreable 0–5 for detection effectiveness. This is the integration test that proves hypothesis-driven detections actually fire against real behavior before being trusted in production — directly the loop ThornCloud's own SIEM-SOC rollout tracker calls out as not yet fire-drilled end-to-end.

## Detection Maturity Model

Elastic's **Detection Engineering Behavior Maturity Model (DEBMM, 2025)**: five non-linear tiers (Foundation → Expert) scoring telemetry integration, rule management/versioning, documentation, threat modeling. Simpler threat-hunting progression: **Level 0 reactive** (alerts-only) → **Level 1/2 procedural** (threat-intel-driven hypotheses on a cadence) → **Level 3 program-level** (systematic ATT&CK coverage mapping, automated routine hunts feeding the detection-engineering loop, often paired with SOAR). 2025 Elastic guidance: treat detections as testable/versioned software, favor behavior-driven over IOC rules, run continuous purple-team-style coverage metrics.

## Current Developments (2025-2026)

- **AI-assisted triage tied to detection-as-code**: triage outcomes fed back into detection logic automatically so alert volume shrinks over time. Caveat: a 2025 survey of 282 security leaders found 40% of alerts still go uninvestigated, mainly from missing ownership/impact context — AI triage doesn't fix broken telemetry context by itself.
- **Sigma CI/CD pipelines**: lint → convert (pySigma) → replay against samples → deploy, now a documented GitOps pattern.
- **YARA-L / Google SecOps (Chronicle)**: multi-event correlation across time windows, entity-based matching. 2026 additions: **retrohunting** (apply a new rule against up to 12 months of historical data with no live-detection perf hit) and **Composite Detections** (chaining rules so one's output feeds another as input).

## Related

- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index)
- [Atomic Red Team](kb://11-security-tools-atomic-red-team)
- [SIEM and SOC - Architecture](kb://09-observability-siem-and-soc-architecture)
- [SIEM-SOC Rollout](kb://08-improvements-siem-soc-rollout)
- [SIEM Review Log](kb://09-observability-siem-review-log)
- [Security Map](kb://01-maps-security-map)
