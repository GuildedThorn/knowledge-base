---
title: Breach Intel — Week of 2026-07-16 → 07-23
type: security-briefing
window: 2026-07-16 to 2026-07-23
sources: [Miniflux RSS, live web roundups, MITRE silo (crossview)]
---

# Breach Intel — Week of 2026-07-16 → 07-23

Computed from RSS security items + live weekly-roundup research, grounded against the MITRE knowledge silo (crossview). See [[Security Map]].

## Headline: potential people affected

| Tier | Basis | Total |
|---|---|---|
| **Company-confirmed** | Orgs stated victim counts | **≈ 27.9 M** |
| **+ Actor-claimed exfil** | Unverified group claims (records/rows) | **≈ 104 M** running |
| **+ Conduent cumulative** | Healthcare notification tally that landed this period | **≈ 166 M** |

**Bottom line:** ~**104 million** records/individuals across incidents newly surfacing this week; ~**166 million** if you fold in Conduent's cumulative 62.2 M notification total.

> ⚠️ *Records ≠ unique people.* Counts overlap across the ShinyHunters CRM cluster, mix "rows/files/installs" with "individuals," and actor claims are unverified. Treat as an **upper-bound estimate**, not a census.

## Incident ledger

**Company-confirmed disclosures**
- **KDDI** (Japan telecom) — 14.22 M customers (emails + passwords) — unattributed
- **AssuranceAmerica** — ~7 M records — compromised employee account
- **Aflac** (Japan subsidiary) — 4.38 M customers (PII + bank details)
- **Moody Bible Institute** — 2.3 M donors/students/alumni — *ShinyHunters*
- **Transport for London** — 27,000 employees; 148 systems disabled — *Scattered Spider* (Thalha Jubair, Owen Flowers named)

**Actor-claimed exfiltration (unverified)**
- **Abbott Laboratories** — 30 M PII rows incl. 1 M+ SSNs — *ShinyHunters / ShadowByt3$*
- **Coca-Cola Europacific Partners** — ~23 M records (63 GB) — *Gehenna*
- **Fluke Corp** — 21 M+ Salesforce records (100 GB+) — *ShinyHunters*
- **Kudankulam NPP / Reliance** — 858 K files — *World Leaks*
- **Ingram Content Group** — 80,190 rows — *ShinyHunters*
- **ModHeader extension** — 1.6 M installs (supply-chain) — unattributed
- **Bosch** — engineering data — *D1R*; **Accenture** — 35 GB claimed

**Cumulative update**
- **Conduent** — healthcare notification tally reached **62.2 M** individuals this period (older intrusion)

## Most common vulnerabilities & exploit chains

1. **SaaS/CRM identity abuse — the dominant cluster** (Abbott, Coca-Cola EP, Fluke, Ingram). No CVE — pure identity attack:
   `CAPEC-98 Phishing/vishing → ATT&CK T1078 Valid Accounts (OAuth connected-app abuse) → T1567 Exfiltration over Web Service (bulk Salesforce API export)` *(chain confirmed live in MITRE silo)*
2. **Third-party / helpdesk / supply-chain** — EY (15 days inside a vendor helpdesk platform), Pinnacle via Mercadien accounting firm, ModHeader.
3. **Edge webmail exploitation** — Roundcube `CVE-2024-42009`, `CVE-2025-49113`; **Zimbra** (CISA/NSA/FBI advisory, **Russia state-supported** — from RSS).
4. **SharePoint "ToolShell" chain** — `CVE-2026-56164` + `CVE-2026-56155` → IIS machine-key theft → RCE.
5. **WordPress core pre-auth RCE** — `CVE-2026-63030` + `CVE-2026-60137` (~500 M sites exposed).
6. **Adobe ColdFusion** `CVE-2026-48282` — critical, active exploitation.
7. **AI-agent-driven attacks** — JadePuffer ransomware auto-driven via **Langflow**; Claude Code / DeepSeek-v4 abused by China-linked ops (echoes SANS ISC "autonomous attacker is your own AI model," RSS).
8. **Ransomware impact** — `ATT&CK T1486 Data Encrypted for Impact` — Coca-Cola/fairlife, Bosch.

## Actor attribution breakdown

- **ShinyHunters** — most prolific this week; Salesforce/CRM extortion (Abbott, Fluke, Ingram, Moody Bible)
- **Gehenna** — Coca-Cola Europacific
- **Scattered Spider** — Transport for London
- **World Leaks** — Kudankulam / Reliance
- **D1R** — Bosch · **ShadowByt3$** — Abbott (2nd breach) · **BlackField** — 2 TB corp theft
- **China-linked / UNK_MassTraction** — Roundcube + gov/university mail (AI-assisted)
- **Russia (state-supported)** — Zimbra Collaboration Suite (CISA/NSA/FBI)
- **Unattributed** — most healthcare/insurance disclosures (KDDI, Aflac, EY, Markel, Lake Region)

## Takeaway

The week's real story is **identity, not CVEs**: the largest confirmed and claimed losses came from social-engineered access to SaaS/CRM platforms (Salesforce) — a phishing → valid-accounts → web-service-exfil chain that patching can't fix. State-nexus activity (Russia/Zimbra, China/Roundcube) and AI-orchestrated intrusion are the emerging secondary themes.
