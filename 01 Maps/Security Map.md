Use this note as the index for security work — both offensive methodology (reusable pentest methodology, per-tool and per-payload references, live HTB/CTF campaign logs, malware analysis) and defensive/blue-team detection engineering. Offensive scope is **authorized** engagements only — targets you own or are explicitly permitted to test.

## Reference layer

- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index) — recon → foothold → privesc → AD → pivoting methodology
- [Offensive Tools — Index](kb://11-security-tools-tools-index) — per-tool flags and invocations (nmap, ffuf, Burp, Metasploit, hashcat, impacket, BloodHound…)
- [Payload Cheat Sheets — Index](kb://11-security-payloads-payloads-index) — copy-paste libraries: SQLi, XSS, LFI, command injection, upload bypass, GTFOBins/LOLBAS

## Campaigns

- [HTB: Bedsides — Campaign Index](kb://11-security-htb-bedsides-htb-bedsides-index) — recon → CVE-2025-64512 (pdfminer.six pickle RCE) foothold → root
- [HTB: Cobblestone — Campaign Index](kb://11-security-htb-cobblestone-htb-cobblestone-index)

## Defense / analysis

- [Blue Team - Detection Engineering](kb://11-security-blue-team-detection-engineering) — Sigma rules, threat hunting, MITRE D3FEND, log source prioritization, alert tuning, purple teaming
- [Malware Analysis Workflow](kb://11-security-malware-analysis-malware-analysis-workflow) — safe lab, static triage, dynamic/behavioral analysis
- [Atomic Red Team](kb://11-security-tools-atomic-red-team) — purple-team: run ATT&CK atomics, confirm the [SIEM/SOC](kb://08-improvements-siem-soc-rollout) detections fire

## Datasets

- [AI Agent Cybersecurity Dataset 2026](kb://12-datasets-ai-agent-cybersecurity-2026-dataset-index) — AI-agent / LLM / MCP / autonomous-system attack, defense, and threat-intel corpus (data dictionaries + provenance)

## Related

- [Observability Map](kb://01-maps-observability-map)
- [Network Map](kb://01-maps-network-map)
- [Reference Map](kb://01-maps-reference-map)
