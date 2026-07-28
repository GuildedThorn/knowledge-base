---
summary: "Abusing accounts with Kerberos pre-authentication disabled to obtain crackable AS-REP responses without any prior credentials."
status: active
tags: [security, techniques, kerberos, preauth, credential-access]
private: false
---

# AS-REP Roasting

## Purpose

Abusing accounts with Kerberos pre-authentication disabled to obtain crackable AS-REP responses without any prior credentials.

## How It Works

- Normally the AS-REQ carries a pre-auth timestamp encrypted with the user's key, proving password knowledge before the KDC responds.
- Accounts flagged DONT_REQUIRE_PREAUTH (UF_DONT_REQUIRE_PREAUTH) skip this check, so the KDC returns an AS-REP to any requester.
- The AS-REP contains data encrypted with the user's password-derived key, which is extracted and cracked offline.
- Because no valid domain credential is required, the attack can be launched from an unauthenticated position given a username list.

## Security Notes

- Target accounts are enumerable via LDAP by filtering userAccountControl for the pre-auth-disabled bit.
- RC4-encrypted AS-REPs crack quickly, making weak-password accounts high-value targets.
- MITRE ATT&CK tracks this as Steal or Forge Kerberos Tickets sub-technique T1558.004.

## Defensive Use

- Audit for and remove DONT_REQUIRE_PREAUTH on all accounts unless a legacy system truly requires it.
- Enforce strong, long passwords on any account that must keep pre-auth disabled.
- Alert on event 4768 (AS-REQ) with pre-auth type 0 and RC4 encryption.

## Sources

- MITRE ATT&CK T1558.004 - https://attack.mitre.org/techniques/T1558/004/
- harmj0y, Roasting AS-REPs - https://blog.harmj0y.net/activedirectory/roasting-as-reps/

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
