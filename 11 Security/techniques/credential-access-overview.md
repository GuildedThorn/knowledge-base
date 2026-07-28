---
summary: "Credential access is the theft, dumping, capture, or abuse of authentication material that enables privilege and lateral movement."
status: active
tags: [security, technique, credential-access, attack]
private: false
---

# Credential Access Overview

## Purpose

Credential access is the theft, dumping, capture, or abuse of authentication material that enables privilege and lateral movement.

## Key Ideas

- Credential material includes passwords, hashes, Kerberos tickets, tokens, API keys, cookies, certificates, browser stores, and cloud secrets.
- The tactic is usually a bridge: initial access becomes lateral movement, privilege escalation, cloud access, or persistence.
- Controls must cover storage, runtime access, identity hygiene, and post-theft abuse.

## Defensive Use

- Reduce blast radius with MFA, password uniqueness, tiered administration, secret rotation, short-lived credentials, and least privilege.
- Detect access to LSASS, SAM/NTDS, browser stores, cloud secret APIs, token caches, and unusual authentication from newly seen hosts.

## Sources

- MITRE ATT&CK - Credential Access TA0006 - https://attack.mitre.org/tactics/TA0006/
- Microsoft ASR rules overview - https://learn.microsoft.com/defender-endpoint/attack-surface-reduction
- OWASP Secrets Management Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
