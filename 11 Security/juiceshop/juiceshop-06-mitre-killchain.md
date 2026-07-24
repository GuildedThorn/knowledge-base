---
title: "Juice Shop · 06 · MITRE kill-chain (Crossview)"
tags: [juiceshop, mitre, attack, capec, crossview]
verdict: mapped
---

# 06 · MITRE kill-chain — 🟢 mapped via Crossview silo

## Command

```bash
cd ~/Documents/crossview
nix develop -c python -m crossview show CWE-89     # + CWE-1321, CWE-22
```

## Result — CWE-89 silo cross-refs (verbatim)

- **parents:** CWE-74 (Injection), CWE-943 (Improper Neutralization in a Data Query)
- **targets / used-by CAPEC:** CAPEC-66 (SQL Injection), CAPEC-7 (Blind SQLi), CAPEC-108/109/110, CAPEC-470

## Kill-chain tree (UKC → ATT&CK → CAPEC/CWE)

```
UKC phase          ATT&CK                      CAPEC / CWE (Crossview)
──────────────────────────────────────────────────────────────────────
Reconnaissance  →  T1595 Active Scanning       CWE-548 dir listing (/ftp, /api-docs)   [step 01]
Delivery/Access →  T1190 Exploit Public App    CAPEC-52 Embedding NULL Bytes → CWE-158/CWE-22   [step 02]
Exploitation    →  T1190                        CAPEC-66/7 → CWE-89 SQLi                 [step 04]
Priv-Esc/Creds  →  T1550.001 App Access Token   forged admin JWT (role=admin)           [step 04]
Discovery/Coll. →  T1213 Data from Repos        CAPEC-1 → CWE-639 BOLA                   [step 05]
Supply-chain    →  T1195.001 Compromise Deps    CWE-1321 / CWE-347 latent               [step 03]
```

## Notes

- Anchored on real silo output for CWE-89; other legs use canonical MITRE mappings the silo corroborates.
- Full narrative + remediation in the consolidated report: [[Juice Shop Assessment 2026-07-23]].
- Crossview run gotchas captured in memory (`nix run .` broken → use `nix develop -c python -m crossview`).
