---
summary: "Data dictionary for the four curated core reference tables (attack taxonomy, framework inventory, core threat catalog, MITRE crosswalk) in the AI Agent Cybersecurity 2026 dataset."
status: active
tags: [datasets]
---

# Core Tables — AI Agent Cybersecurity 2026

The `data/core/` group: four small, hand-curated reference tables that define the dataset's vocabulary — the attack taxonomy, the framework inventory, the primary threat catalog, and the MITRE crosswalk. These are reference tables (8–60 rows), not telemetry. Part of [[12 Datasets/AI Agent Cybersecurity 2026/Dataset Index|AI Agent Cybersecurity Dataset 2026]].

## agent_attack_taxonomy.csv — 12 rows

`data/core/agent_attack_taxonomy.csv` · one row = a class of AI-agent attack technique with taxonomy and standards references.

| Column | Description |
|---|---|
| attack_type | Name of the technique (e.g. Prompt Injection) |
| category | Top-level bucket (e.g. Input Manipulation) |
| subcategory | Finer class (e.g. Direct Injection) |
| description | Prose explanation |
| target_component | Agent component attacked (e.g. LLM System Prompt) |
| impact | Consequence if successful |
| owasp_ref | OWASP LLM Top 10 ID (e.g. LLM01:2025) |
| mitre_atlas_ref | MITRE ATLAS technique ID (e.g. AML.T0051) |
| severity_range | Typical severity band |
| example_frameworks | Frameworks where it applies |
| real_world_incidents | Known real incidents |

## agent_frameworks.csv — 8 rows

`data/core/agent_frameworks.csv` · one row = an AI-agent framework profiled for security posture.

| Column | Description |
|---|---|
| framework | Framework name (e.g. LangChain) |
| category | e.g. Agent Framework |
| subcategory | Finer classification |
| language | Implementation language(s) |
| first_release | Year/date first released |
| github_stars_approx | Approximate popularity |
| key_features | Notable capabilities |
| known_cves | Published CVEs against it |
| attack_surface | Where it can be attacked |
| security_docs_url | Link to security docs |
| status | Maturity/lifecycle (e.g. Active — Production) |

## ai_agent_core_threats.csv — 60 rows

`data/core/ai_agent_core_threats.csv` · one row = a catalogued agent threat (`AIA-###`) with severity, success rate, and mitigation. **This is the primary threat catalog; its `attack_id`s reappear in the master table.**

| Column | Description |
|---|---|
| attack_id | Stable ID (e.g. AIA-001) |
| attack_name | Human-readable name |
| attack_type | Technique class |
| agent_framework | Framework involved (e.g. LangChain) |
| ai_model | Model targeted (e.g. GPT-4o) |
| description | Prose explanation |
| cve_reference | Related CVE(s) if any |
| mitre_atlas_id | MITRE ATLAS technique ID |
| real_world_example | Documented occurrence |
| severity_score | CVSS-style 0–10 severity |
| attack_success_rate | Empirical/estimated success rate (0–1) |
| mitigation | Recommended defense |
| target_component | Component attacked |
| year | Year documented |
| source | Citation/source |

## mitre_attack_mapping.csv — 17 rows

`data/core/mitre_attack_mapping.csv` · one row = a MITRE ATT&CK technique mapped into an AI-agent context (a crosswalk from classic ATT&CK to agent threats).

| Column | Description |
|---|---|
| source_framework | Origin framework (e.g. MITRE ATT&CK) |
| technique_id | Technique ID (e.g. T1059) |
| technique_name | Technique name |
| ai_agent_context | How it manifests against agents |
| ai_attack_type | Equivalent agent attack (e.g. Tool Poisoning) |
| relevant_agent_component | Component involved |
| tactic | ATT&CK tactic (e.g. Execution) |
| mitre_url | Reference URL |

## Related

- [[12 Datasets/AI Agent Cybersecurity 2026/Dataset Index|Dataset Index]]
- [[12 Datasets/AI Agent Cybersecurity 2026/Agent Security Tables|Agent Security Tables]]
- [[11 Security/playbook/pentest-playbook-index|Pentest Playbook — Index]]
