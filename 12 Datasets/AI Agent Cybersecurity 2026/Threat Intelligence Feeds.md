---
summary: "Data dictionary for the threat-intelligence feeds (HuggingFace prompt injections, AlienVault OTX pulses/indicators) in the AI Agent Cybersecurity 2026 dataset — the largest tables, ~21k rows."
status: active
tags: [datasets]
---

# Threat Intelligence Feeds — AI Agent Cybersecurit[[TrueNAS Storage Capture 2026-08-01]]y 2026

The `data/threat_intelligence/` group: the real telemetry in this dataset — a labeled prompt-injection corpus from HuggingFace and live AlienVault OTX pulses/indicators. These four files hold ~21,300 of the dataset's rows. Part of [[12 Datasets/AI Agent Cybersecurity 2026/Dataset Index|AI Agent Cybersecurity Dataset 2026]].

## hf_prompt_injections.csv — 11,616 rows

`data/threat_intelligence/hf_prompt_injections.csv` · one row = a labeled text sample. A ready-to-use training/eval corpus for a prompt-injection classifier (largest file in the dataset).

| Column | Description |
|---|---|
| text | The prompt/text sample |
| label | `0` = benign, `1` = injection |
| source_dataset | Upstream HF dataset (e.g. deepset/prompt-injections) |

## otx_threat_pulses.csv — 1,201 rows

`data/threat_intelligence/otx_threat_pulses.csv` · one row = a general AlienVault OTX threat "pulse" (a curated threat report).

| Column | Description |
|---|---|
| pulse_id | OTX pulse ID |
| name | Pulse title |
| description | Summary |
| author | Contributor |
| created | Creation timestamp |
| modified | Last-modified timestamp |
| tlp | Traffic Light Protocol level |
| targeted_countries | Countries targeted |
| tags | Free-text tags |
| malware_families | Named malware families |
| attack_ids | MITRE ATT&CK technique IDs |
| industries | Sectors targeted |
| indicator_count | Number of IOCs in the pulse |
| subscriber_count | OTX subscribers |
| references | External reference URLs |

## otx_ai_agent_threats.csv — 2,768 rows

`data/threat_intelligence/otx_ai_agent_threats.csv` · one row = an OTX pulse filtered for AI-agent relevance, **plus two scoring columns** on top of the `otx_threat_pulses` schema.

| Column | Description |
|---|---|
| *(all columns from otx_threat_pulses.csv)* | see above |
| severity_score | Derived 0–10 severity |
| risk_level | Derived band (e.g. Medium) |

> Same base schema as `otx_threat_pulses.csv`; this is the AI-filtered, severity-scored subset.

## otx_indicators.csv — 5,743 rows

`data/threat_intelligence/otx_indicators.csv` · one row = a single indicator of compromise (IOC) tied to a pulse — the pulses "exploded" one IOC per row. **This is the actionable feed for detection/blocklists.**

| Column | Description |
|---|---|
| pulse_id | Parent OTX pulse ID |
| pulse_name | Parent pulse title |
| type | IOC type (IPv4, domain, hostname, hash, URL…) |
| indicator | The IOC value (e.g. `196.251.107.130`) |
| created | When added |
| is_active | `1` = active, `0` = retired |

> These IOCs could feed the ThornCloud [[09 Observability/SIEM and SOC - Architecture|SIEM/SOC]] as a watchlist — see the Dataset Index for the "possible integrations" note.

## Related

- [[12 Datasets/AI Agent Cybersecurity 2026/Dataset Index|Dataset Index]]
- [[12 Datasets/AI Agent Cybersecurity 2026/Vulnerability Feeds|Vulnerability Feeds]]
- [[01 Maps/Observability Map|Observability Map]]
