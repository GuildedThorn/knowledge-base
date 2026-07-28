---
summary: "Injecting stolen or forged Kerberos tickets into a logon session to authenticate as the ticket owner."
status: active
tags: [security, techniques, kerberos, ticket, lateral-movement]
private: false
---

# Pass-the-Ticket

## Purpose

Injecting stolen or forged Kerberos tickets into a logon session to authenticate as the ticket owner.

## How It Works

- Kerberos issues a TGT that a client presents to the KDC to obtain service tickets (TGS) for specific resources.
- An attacker who obtains a valid TGT or TGS can import it into their own session and access resources as the victim.
- Tickets live in LSASS memory; extracting them yields reusable credentials that require no password.
- Injected tickets are honored until they expire, giving a bounded but often multi-hour window of access.

## Tooling and Variants

- Mimikatz `sekurlsa::tickets /export` dumps cached tickets to `.kirbi` files; `kerberos::ptt` injects them.
- Overpass-the-hash (pass-the-key) uses an NT/AES key to request a fresh TGT, converting a hash into a ticket.
- Golden and silver tickets are forged variants: KRBTGT-signed TGTs or service-key-signed TGS built offline.
- Rubeus provides equivalent extraction, injection, and request operations on Windows.

## Defensive Use

- Watch for tickets used from unexpected hosts or accounts with abnormal encryption types (RC4 vs AES).
- Rotate the KRBTGT account password twice to invalidate outstanding forged golden tickets.
- Protect LSASS with RunAsPPL and Credential Guard to limit ticket theft.
- Correlate Event IDs 4768/4769 for anomalous ticket-request patterns.

## Sources

- MITRE ATT&CK T1550.003 - https://attack.mitre.org/techniques/T1550/003/
- mimikatz wiki - https://github.com/gentilkiwi/mimikatz/wiki

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
