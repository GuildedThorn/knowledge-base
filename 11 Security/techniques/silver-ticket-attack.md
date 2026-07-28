---
summary: "Forging Kerberos service tickets with a stolen service account key to access a single service without contacting the KDC."
status: active
tags: [security, techniques, kerberos, tgs, service-account]
private: false
---

# Silver Ticket Attack

## Purpose

Forging Kerberos service tickets with a stolen service account key to access a single service without contacting the KDC.

## How It Works

- A service ticket (TGS) is encrypted and signed with the key of the target service's account, not the KRBTGT account.
- With that service account's password hash (or machine account hash), an attacker forges a valid TGS offline for a chosen SPN.
- The forged ticket is presented directly to the service; because no TGS-REQ is sent, the KDC never sees the request.
- Access is scoped to services running under the compromised account (e.g. CIFS, HOST, MSSQLSvc) rather than the whole domain.

## Security Notes

- Silver tickets are stealthier than golden tickets since the domain controller logs no ticket-granting activity.
- The forged PAC can assert arbitrary group membership, and services that skip PAC validation accept it unchecked.
- MITRE ATT&CK tracks this as Steal or Forge Kerberos Tickets sub-technique T1558.002.

## Defensive Use

- Enable PAC validation so services verify the ticket's privilege data against the KDC.
- Rotate machine and service account passwords regularly to invalidate stolen keys used for forgery.
- Monitor for service logons (event 4624/4769 mismatch) lacking a corresponding TGS request on the DC.

## Sources

- MITRE ATT&CK T1558.002 - https://attack.mitre.org/techniques/T1558/002/
- ADSecurity, Silver Ticket - https://adsecurity.org/?p=2011

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
