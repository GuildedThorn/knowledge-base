---
summary: "Impersonating a domain controller via the MS-DRSR replication protocol to remotely extract password hashes including KRBTGT."
status: active
tags: [security, techniques, replication, credential-access, active-directory]
private: false
---

# DCSync

## Purpose

Impersonating a domain controller via the MS-DRSR replication protocol to remotely extract password hashes including KRBTGT.

## How It Works

- Domain controllers synchronize directory data using the MS-DRSR replication protocol and the `DsGetNCChanges` call.
- An attacker with sufficient rights issues that replication request from any host, and the DC returns account secrets.
- No code runs on the DC and no LSASS access is needed, so the technique leaves a light on-host footprint.
- Extracted material includes NT hashes, Kerberos keys, and the KRBTGT hash that enables golden tickets.

## Required Rights

- The caller needs the Replicating Directory Changes and Replicating Directory Changes All extended rights on the domain object.
- These are normally held by Domain Admins, Enterprise Admins, and the DCs themselves.
- Delegated or misconfigured ACLs granting these rights to lesser accounts are a common privilege-escalation path.

## Defensive Use

- Audit the domain naming-context ACL for the DS-Replication-Get-Changes rights and remove unexpected principals.
- Alert on replication requests originating from IPs that are not known domain controllers.
- Monitor directory service access events (Event ID 4662) for the replication GUIDs.
- Tier and tightly control accounts holding replication privileges.

## Sources

- MITRE ATT&CK T1003.006 - https://attack.mitre.org/techniques/T1003/006/
- ADSecurity Mimikatz DCSync - https://adsecurity.org/?p=1729

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
