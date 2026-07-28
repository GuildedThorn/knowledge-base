---
summary: "Use this note as the index for generated situational-awareness output — daily briefings and threat dossiers synthesized by vr-brain and the SIEM review loop."
status: active
tags: [maps]
---

Use this note as the index for **generated** situational-awareness output — daily briefings and threat dossiers synthesized by vr-brain and the SIEM/SOC review loop. These are machine-authored (`generated_by: vr-brain`, `status: proposed`) and meant to be reviewed, not trusted as fact until verified against their cited evidence.

## Daily Briefings

Rolling end-of-day summaries of what changed across the vault and the fleet.

- [[Briefings/2026-07-24|2026-07-24 · Daily Briefing]]
- [[Briefings/2026-07-23|2026-07-23 · Daily Briefing]]
- [[Briefings/2026-07-22|2026-07-22 · Daily Briefing]]
- [[Intelligence/Briefings/2026-07-26|2026-07-26 · Briefing]]

> **Reconcile:** briefings currently land in two places — top-level `Briefings/` and `Intelligence/Briefings/`. Pick one home so this index stays single-sourced.

## Threat Dossiers

Per-indicator evidence synthesis (IOC → sources → why-it-connects), emitted by vr-brain from live threat feeds.

- [[Intelligence/Dossiers/20260726-known-botnet-c2-50.16.16.211|Known botnet C2 50.16.16.211]] — Feodo Tracker indicator, Ashburn US

> **Generator note:** dossiers emit their vault backlinks as `kb://` slugs wrapped in `[[…]]` (e.g. `[[01-maps-security-map]]`), which don't resolve as Obsidian wikilinks. Fixed by hand in the note above; the durable fix is in vr-brain's dossier generator (emit `[[Security Map]]`-style basenames or plain `kb://` links).

## Related

- [[01 Maps/Observability Map|Observability Map]] — the SIEM/SOC telemetry these draw from
- [[01 Maps/Security Map|Security Map]]
- [[09 Observability/SIEM Review Log|SIEM Review Log]] — the append-only tier-1 review passes
