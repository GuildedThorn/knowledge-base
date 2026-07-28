---
summary: "Requesting service tickets for SPN-bound accounts and cracking the RC4/AES ticket offline to recover the service account password."
status: active
tags: [security, techniques, kerberos, spn, credential-access]
private: false
---

# Kerberoasting

## Purpose

Requesting service tickets for SPN-bound accounts and cracking the RC4/AES-encrypted ticket offline to recover the service account password.

## How It Works

- Any authenticated domain user can enumerate accounts with a registered ServicePrincipalName (SPN) via LDAP.
- The attacker sends a TGS-REQ for the target SPN; the KDC returns a service ticket encrypted with the service account's password-derived key.
- The ticket portion is extracted and cracked offline, so no traffic reaches the target service and lockout policies do not apply.
- RC4 (etype 23) tickets crack fastest; AES (etype 17/18) tickets are far slower but still offline-attackable.

## Security Notes

- Service accounts with weak, human-set passwords are the core exposure; the technique bypasses account-lockout entirely.
- SPNs on regular user accounts (not machine or managed accounts) are the prime targets due to memorable passwords.
- MITRE ATT&CK classifies this under Steal or Forge Kerberos Tickets, sub-technique T1558.003.

## Defensive Use

- Use Group Managed Service Accounts (gMSA) or long random passwords so offline cracking is infeasible.
- Disable RC4 and enforce AES encryption types on service accounts to slow cracking dramatically.
- Detect abnormal volumes of TGS-REQ / event 4769 with RC4 encryption from a single principal.

## Sources

- MITRE ATT&CK T1558.003 - https://attack.mitre.org/techniques/T1558/003/
- harmj0y, Kerberoasting Without Mimikatz - https://blog.harmj0y.net/powershell/kerberoasting-without-mimikatz/
- Microsoft Kerberos Authentication Overview - https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
