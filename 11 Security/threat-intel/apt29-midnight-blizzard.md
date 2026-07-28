---
summary: "APT29 is a Russian SVR-attributed cluster associated with stealthy espionage, cloud identity abuse, and supply-chain compromise."
status: active
tags: [security, threat-intel, apt, cloud]
private: false
---

# APT29 / Midnight Blizzard

## Purpose

APT29 is a Russian SVR-attributed cluster associated with stealthy espionage, cloud identity abuse, and supply-chain compromise.

## Key Ideas

- Known aliases include Cozy Bear, NOBELIUM, UNC2452, Midnight Blizzard, and related vendor names.
- Public reporting emphasizes stealth, long dwell time, cloud identity abuse, token theft/forgery, and supply-chain access.
- The SolarWinds/SUNBURST campaign is the canonical supply-chain case tied to this cluster in public reporting.

## Defensive Use

- Prioritize cloud identity telemetry: service principals, OAuth apps, federation changes, token anomalies, and mailbox/API access patterns.
- Correlate endpoint, DNS, cloud audit, and identity-provider logs; endpoint-only visibility is insufficient for this actor model.

## Sources

- MITRE ATT&CK - APT29 G0016 - https://attack.mitre.org/groups/G0016/
- MITRE ATT&CK Evaluations - APT29 - https://evals.mitre.org/enterprise/apt29/
- CISA AA21-008A - Detecting Post-Compromise Threat Activity in Microsoft Cloud Environments - https://content.govdelivery.com/accounts/USDHSCISA/bulletins/2b4e726

## Related

- [Threat Intel - Index](kb://11-security-threat-intel-threat-intel-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
