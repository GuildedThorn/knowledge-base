---
summary: "Overview and index of the Kaggle AI Agent Cybersecurity Dataset 2026 — 22 CSVs across 6 categories covering AI-agent, LLM, MCP, and autonomous-system security. Provenance, structure, caveats, and how to load."
status: active
tags: [datasets, index]
---

# AI Agent Cybersecurity Dataset 2026

Kaggle dataset **`chuneeb/ai-agent-cybersecurity-dataset-2026`** — a security corpus for AI agents, LLMs, the Model Context Protocol (MCP), and autonomous systems. **22 CSV files**, ~21,900 rows total: a small hand-curated reference core (attack taxonomies, framework/threat/defense catalogs) plus large real-world feeds (HuggingFace prompt injections, AlienVault OTX, NVD, CISA KEV).

## Provenance

- **Source:** [Kaggle — AI Agent Cybersecurity Dataset 2026](https://www.kaggle.com/datasets/chuneeb/ai-agent-cybersecurity-dataset-2026) (author `chuneeb`)
- **Ingested:** 2026-07-23 (via in-world browser download → `~/Downloads/archive.zip`)
- **Raw files on disk:** `~/Downloads/ai-agent-cyber-2026/data/` — kept outside the vault by design; these notes are the knowledge layer / data dictionary over the CSVs.
- **Upstream sources embedded in the data:** OWASP LLM Top 10 (2025), MITRE ATLAS & ATT&CK, CISA KEV, NVD, AlienVault OTX, HuggingFace (`deepset/prompt-injections`), and academic papers.
- **Coverage window:** through mid-2026 (newest KEV entries dated 2026-06).
- **License:** not restated here — check the Kaggle page before redistributing.

## Structure

| Category | Note | Files | Rows |
|---|---|---|---|
| Core reference | [[12 Datasets/AI Agent Cybersecurity 2026/Core Tables\|Core Tables]] | 4 | ~97 |
| Agent security | [[12 Datasets/AI Agent Cybersecurity 2026/Agent Security Tables\|Agent Security Tables]] | 5 | ~65 |
| Autonomous systems | [[12 Datasets/AI Agent Cybersecurity 2026/Autonomous Systems Tables\|Autonomous Systems Tables]] | 2 | ~22 |
| Defenses | [[12 Datasets/AI Agent Cybersecurity 2026/Defenses Tables\|Defenses Tables]] | 3 | ~87 |
| Threat intelligence | [[12 Datasets/AI Agent Cybersecurity 2026/Threat Intelligence Feeds\|Threat Intelligence Feeds]] | 4 | ~21,300 |
| Vulnerabilities | [[12 Datasets/AI Agent Cybersecurity 2026/Vulnerability Feeds\|Vulnerability Feeds]] | 3 | ~3,170 |
| **Master (consolidated)** | *this note, below* | 1 | 147 |

## Master consolidated table

`data/master_ai_agent_cybersecurity.csv` — 147 rows. A normalized roll-up that flattens the curated catalogs into one common schema. Its `record_id`s (e.g. `AIA-001`) overlap with `core/ai_agent_core_threats.csv`, so treat this as a unified *view*, not an independent source.

| Column | Description |
|---|---|
| record_id | Stable ID, joins back to the source tables |
| category | High-level bucket (e.g. AI Agent Core Threat) |
| subcategory | Finer class (e.g. Prompt Injection) |
| attack_name | Attack name |
| description | Prose explanation |
| severity | 0–10 severity |
| source | Origin table/citation |
| year | Year |

## Caveats & data quality

- **NVD keyword noise:** `nvd_ai_cves*.csv` use substring keyword matching, so `LLMNR`/unrelated CVEs match `LLM`. Filter before analysis.
- **Multi-line cells:** `incident_response_playbooks.csv` has quoted values spanning lines — use a real CSV parser (`pandas.read_csv`), not line splitting.
- **Duplicated schemas:** `otx_ai_agent_threats.csv` = `otx_threat_pulses.csv` + `severity_score`/`risk_level`; `nvd_ai_cves_enriched.csv` = `nvd_ai_cves.csv` + 6 agent-context columns.
- **Curated vs. real:** the core/agent_security/defenses/autonomous tables are hand-authored reference (8–60 rows); only the threat-intel and vulnerability feeds are bulk real-world data. Some enrichment fields (`attack_success_rate`) appear heuristic.

## How to load

```python
import pandas as pd, pathlib
root = pathlib.Path("~/Downloads/ai-agent-cyber-2026/data").expanduser()
tables = {p.relative_to(root).as_posix(): pd.read_csv(p) for p in root.rglob("*.csv")}
tables["master_ai_agent_cybersecurity.csv"].head()
```

## Possible ThornCloud integrations

- Feed `otx_indicators.csv` IOCs into the [[09 Observability/SIEM and SOC - Architecture|SIEM/SOC]] as a watchlist/blocklist.
- Use `hf_prompt_injections.csv` to evaluate prompt-injection detection on the vault's own MCP-driven agents.
- Cross-reference `mcp_security_incidents.csv` against how vr-brain / the SOC cockpit expose MCP tools.

## Related

- [[01 Maps/Datasets Map|Datasets Map]]
- [[01 Maps/Security Map|Security Map]]
- [[11 Security/playbook/pentest-playbook-index|Pentest Playbook — Index]]
- [[01 Maps/Observability Map|Observability Map]]
