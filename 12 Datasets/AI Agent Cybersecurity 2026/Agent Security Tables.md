---
summary: "Data dictionary for the five agent-security attack tables (adversarial ML, AI supply chain, LLM jailbreaks, MCP incidents, multi-agent attacks) in the AI Agent Cybersecurity 2026 dataset."
status: active
tags: [datasets]
---

# Agent Security Tables — AI Agent Cybersecurity 2026

The `data/agent_security/` group: five curated attack catalogs covering the agent-specific attack surface — adversarial ML, the AI/ML supply chain, LLM jailbreaks, Model Context Protocol incidents, and multi-agent (agent-to-agent) attacks. Reference tables of 10–15 rows each. Part of [[12 Datasets/AI Agent Cybersecurity 2026/Dataset Index|AI Agent Cybersecurity Dataset 2026]].

## adversarial_ml_attacks.csv — 15 rows

`data/agent_security/adversarial_ml_attacks.csv` · one row = an adversarial-ML attack method (e.g. FGSM) with formulation and measured success.

| Column | Description |
|---|---|
| attack_id | Stable ID (e.g. ADV-001) |
| attack_name | Method name (e.g. Fast Gradient Sign Method) |
| attack_family | Family (e.g. Gradient-Based) |
| attack_type | White-/black-/grey-box |
| target_model_type | Model class targeted |
| description | Prose explanation |
| math_formulation | Formal/notation of the perturbation |
| perturbation_type | Norm/kind of perturbation |
| epsilon_typical | Typical perturbation budget |
| attack_success_rate_imagenet | ASR on ImageNet (0–1) |
| attack_success_rate_llm | ASR against LLMs (0–1) |
| requires_model_access | Access needed (weights/gradients) |
| compute_cost | Relative cost |
| transferability | Cross-model transfer |
| real_world_applicability | Practicality |
| paper_ref | Source paper (e.g. arXiv:1412.6572) |
| year | Year |
| mitigation | Defense |
| ai_agent_relevance | Why it matters to agents |

## ai_supply_chain_attacks.csv — 10 rows

`data/agent_security/ai_supply_chain_attacks.csv` · one row = an AI/ML supply-chain attack (model repo, dependency, or data poisoning).

| Column | Description |
|---|---|
| attack_id | Stable ID (e.g. SC-001) |
| attack_name | Name |
| attack_type | e.g. Model Repository Poisoning |
| platform | Where it occurs (e.g. Hugging Face Hub) |
| target | What is compromised |
| technique | How it is carried out |
| impact | Consequence |
| severity_score | 0–10 severity |
| risk_level | Critical/High/… |
| cve_reference | Related CVE(s) |
| affected_frameworks | Frameworks impacted |
| real_world_ref | Documented case |
| year | Year |
| mitigation | Defense |
| source | Citation |

## llm_jailbreak_dataset.csv — 15 rows

`data/agent_security/llm_jailbreak_dataset.csv` · one row = a documented jailbreak technique with per-model success rates and patch status.

| Column | Description |
|---|---|
| jailbreak_id | Stable ID (e.g. JB-001) |
| jailbreak_name | Name (e.g. DAN) |
| jailbreak_family | Family (e.g. Persona Injection) |
| variant | Specific variant |
| target_models | Models affected |
| description | Explanation |
| example_prompt_summary | Sanitised summary of the prompt |
| attack_mechanism | How it works |
| bypass_technique | Guardrail bypassed |
| attack_success_rate_gpt4 | ASR vs GPT-4 (0–1) |
| attack_success_rate_claude | ASR vs Claude (0–1) |
| attack_success_rate_llama | ASR vs Llama (0–1) |
| detection_difficulty | How hard to detect |
| harmful_content_categories | Content classes elicited |
| first_documented | First seen |
| year | Year |
| mitigation | Defense |
| source | Citation |
| status | Patch status (e.g. Partially Patched) |

## mcp_security_incidents.csv — 15 rows

`data/agent_security/mcp_security_incidents.csv` · one row = a Model Context Protocol security incident against a named MCP server. **Directly relevant to this vault — vr-brain and the SOC cockpit are MCP-driven.**

| Column | Description |
|---|---|
| incident_id | Stable ID (e.g. MCP-001) |
| mcp_server | Server involved (e.g. filesystem-server) |
| attack_type | e.g. Tool Poisoning |
| technique | Method |
| impact | Consequence |
| severity_score | 0–10 severity |
| risk_level | Critical/High/… |
| cve_reference | Related CVE(s) |
| affected_clients | Clients hit (e.g. Claude Desktop, Cursor) |
| year | Year |
| real_world_ref | Documented case |
| mitre_atlas_id | ATLAS technique ID |
| mitigation | Defense |
| source | Citation |

## multi_agent_attacks.csv — 10 rows

`data/agent_security/multi_agent_attacks.csv` · one row = an attack between agents in a multi-agent system (names source and target agent).

| Column | Description |
|---|---|
| attack_id | Stable ID (e.g. MAA-001) |
| attack_name | Name |
| attack_type | Class |
| description | Explanation |
| source_agent | Attacking agent role |
| target_agent | Victim agent role |
| agent_framework | Framework (e.g. CrewAI) |
| ai_model | Model involved |
| attack_vector | Channel exploited |
| impact | Consequence |
| severity_score | 0–10 severity |
| risk_level | Critical/High/… |
| attack_success_rate | ASR (0–1) |
| mitre_atlas_id | ATLAS technique ID |
| real_world_ref | Documented case |
| mitigation | Defense |
| year | Year |

## Related

- [[12 Datasets/AI Agent Cybersecurity 2026/Dataset Index|Dataset Index]]
- [[12 Datasets/AI Agent Cybersecurity 2026/Defenses Tables|Defenses Tables]]
- [[11 Security/payloads/payloads-index|Payload Cheat Sheets — Index]]
