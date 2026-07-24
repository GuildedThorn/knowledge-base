---
summary: "Data dictionary for the defensive tables (defense mechanisms, security benchmarks, incident-response playbooks) in the AI Agent Cybersecurity 2026 dataset."
status: active
tags: [datasets]
---

# Defenses Tables — AI Agent Cybersecurity 2026

The `data/defenses/` group: the blue-team half of the dataset — a catalog of defensive controls, a table of benchmark results pairing attacks against defenses, and a set of incident-response playbooks. Part of [[12 Datasets/AI Agent Cybersecurity 2026/Dataset Index|AI Agent Cybersecurity Dataset 2026]].

## agent_defense_mechanisms.csv — 15 rows

`data/defenses/agent_defense_mechanisms.csv` · one row = a defense/mitigation with effectiveness and overhead metrics.

| Column | Description |
|---|---|
| defense_id | Stable ID (e.g. DEF-001) |
| defense_name | Name (e.g. Prompt Shield / Azure AI) |
| defense_category | e.g. Input Filtering |
| attack_prevented | Attack it counters |
| description | Explanation |
| effectiveness_score | Effectiveness (0–1) |
| false_positive_rate | FPR (0–1) |
| applicable_frameworks | Frameworks it fits |
| applicable_models | Models it fits |
| implementation_complexity | Effort to deploy |
| performance_overhead | Runtime cost |
| year_introduced | Year |
| source | Citation |
| link | Reference URL |

## ai_agent_benchmarks.csv — 12 rows

`data/defenses/ai_agent_benchmarks.csv` · one row = a benchmark result pairing an attack and a defense with measured success rates.

| Column | Description |
|---|---|
| benchmark_id | Stable ID (e.g. BM-001) |
| benchmark_name | Benchmark (e.g. PromptBench) |
| framework | Framework under test |
| attack | Attack evaluated |
| ai_model | Model evaluated (e.g. GPT-4o) |
| attack_success_rate | ASR without defense (0–1) |
| defense | Defense applied |
| defense_success_rate | Defense block rate (0–1) |
| metric | Metric reported (e.g. ASR) |
| dataset_size | Sample size |
| year | Year |
| paper_ref | Source paper |
| notes | Free-text notes |

## incident_response_playbooks.csv — 60 rows

`data/defenses/incident_response_playbooks.csv` · one row = an IR playbook for one attack type. **Quirk: `immediate_steps` and other step fields contain multi-line quoted values — parse with a real CSV reader (e.g. `pandas.read_csv`), not line splitting.**

| Column | Description |
|---|---|
| playbook_id | Stable ID (e.g. IRP-001) |
| attack_type | Attack the playbook responds to |
| trigger_indicators | Signals that fire the playbook |
| immediate_steps | First actions (multi-line) |
| short_term_mitigation | Near-term containment |
| long_term_remediation | Durable fix |
| affected_components | Systems in scope |
| escalation_criteria | When to escalate |
| recovery_time_estimate | Expected recovery time |
| severity | Severity band |
| source | Citation |

> These IR playbooks pair naturally with the vault's own [[11 Security/playbook/pentest-playbook-index|Pentest Playbook]] (offensive) and the [[09 Observability/SIEM and SOC - Architecture|SIEM/SOC]] detection layer.

## Related

- [[12 Datasets/AI Agent Cybersecurity 2026/Dataset Index|Dataset Index]]
- [[12 Datasets/AI Agent Cybersecurity 2026/Agent Security Tables|Agent Security Tables]]
- [[01 Maps/Observability Map|Observability Map]]
