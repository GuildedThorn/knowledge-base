---
summary: "Forging arbitrary Kerberos TGTs using the KRBTGT account hash to impersonate any principal across a domain."
status: active
tags: [security, techniques, kerberos, tgt, krbtgt]
private: false
---

# Golden Ticket Attack

## Purpose

Forging arbitrary Kerberos TGTs using the KRBTGT account hash to impersonate any principal across a domain.

## How It Works

- Every Ticket-Granting Ticket (TGT) is encrypted and signed with the key of the domain's KRBTGT account.
- With the KRBTGT hash (obtained via DCSync, NTDS.dit theft, or domain compromise), an attacker forges TGTs offline for any user and group membership.
- Forged tickets can claim arbitrary SIDs, including Domain Admins, and set validity far beyond normal lifetimes.
- The KDC accepts the ticket because it only validates the KRBTGT signature, granting service tickets for any resource.

## Security Notes

- A golden ticket is a full domain-persistence primitive; it survives password resets of individual users.
- The forged TGT bypasses normal authentication, so the initial account never needs a valid password.
- MITRE ATT&CK records this as Steal or Forge Kerberos Tickets sub-technique T1558.001.

## Defensive Use

- Reset the KRBTGT password twice (double rotation), since two prior keys are honored, to fully invalidate forged tickets.
- Treat KRBTGT hash exposure as full domain compromise requiring rebuild-grade response.
- Detect anomalous TGT lifetimes, mismatched account/RID data, and tickets with no corresponding AS-REQ (event 4768).

## Sources

- MITRE ATT&CK T1558.001 - https://attack.mitre.org/techniques/T1558/001/
- ADSecurity, Golden Ticket - https://adsecurity.org/?p=1640
- mimikatz wiki - https://github.com/gentilkiwi/mimikatz/wiki

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
