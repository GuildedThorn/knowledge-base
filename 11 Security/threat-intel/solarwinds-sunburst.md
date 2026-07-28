---
summary: "SUNBURST was a trojanized SolarWinds Orion update path used for stealthy downstream access and cloud identity compromise."
status: active
tags: [security, threat-intel, supply-chain, sunburst]
private: false
---

# SolarWinds SUNBURST

## Purpose

SUNBURST was a trojanized SolarWinds Orion update path used for stealthy downstream access and cloud identity compromise.

## Key Ideas

- The intrusion used a trusted software update mechanism, then selected victims for follow-on access rather than exploiting every installation equally.
- SUNBURST blended C2 into normal-looking Orion traffic and delayed activity to reduce obvious correlation with installation.
- The broader campaign extended into Microsoft 365/Azure identity abuse, forged tokens, and privileged application access.

## Defensive Use

- Track build/release integrity, code-signing paths, vendor update trust, DNS anomalies, federation changes, and service-principal activity.
- Plan for trusted-tool compromise: vendor allowlists need behavior monitoring and revocation playbooks.

## Sources

- MITRE ATT&CK - SUNBURST S0559 - https://attack.mitre.org/software/S0559/
- CISA AA21-008A - Microsoft cloud post-compromise activity - https://content.govdelivery.com/accounts/USDHSCISA/bulletins/2b4e726
- SolarWinds - Secure by Design update - https://www.solarwinds.com/blog/secure-by-design-a-solarwinds-update-for-national-defenders

## Related

- [Threat Intel - Index](kb://11-security-threat-intel-threat-intel-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
