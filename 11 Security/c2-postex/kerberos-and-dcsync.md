---
summary: "Kerberos and DCSync abuse turns identity-control weaknesses into credential replication, ticket forgery, and domain persistence."
status: active
tags: [security, active-directory, kerberos, credential-access]
private: false
---

# Kerberos and DCSync Abuse

## Purpose

Kerberos and DCSync abuse turns identity-control weaknesses into credential replication, ticket forgery, and domain persistence.

## Key Ideas

- DCSync abuses directory replication rights to request password material as if the caller were a domain controller.
- Kerberos abuse patterns include ticket theft, Kerberoasting, AS-REP roasting, unconstrained/constrained delegation risk, and golden/silver ticket concepts.
- These techniques are identity-plane problems; host cleaning alone does not repair delegated rights or exposed secrets.

## Defensive Use

- Audit replication rights, Tier Zero membership, delegation settings, SPN exposure, KRBTGT rotation plans, and privileged logon hygiene.
- Collect directory service events and authentication telemetry; alert on non-DC principals performing replication-like actions.

## Sources

- MITRE ATT&CK - OS Credential Dumping: DCSync T1003.006 - https://attack.mitre.org/techniques/T1003/006/
- SpecterOps BloodHound documentation - https://bloodhound.specterops.io/home
- Microsoft - Securing privileged access - https://learn.microsoft.com/en-us/security/privileged-access-workstations/privileged-access-access-model

## Related

- [C2 & Post-Ex - Index](kb://11-security-c2-postex-c2-postex-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
