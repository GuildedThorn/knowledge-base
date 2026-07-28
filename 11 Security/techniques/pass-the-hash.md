---
summary: "Authenticating over NTLM using a captured NT hash instead of the plaintext password to move laterally without cracking it."
status: active
tags: [security, techniques, ntlm, lateral-movement, credential-reuse]
private: false
---

# Pass-the-Hash

## Purpose

Authenticating over NTLM using a captured NT hash instead of the plaintext password to move laterally without cracking it.

## How It Works

- NTLM authentication never sends the password; the NT hash is the effective credential used to compute the challenge-response.
- An attacker who holds the NT hash can replay it against any service accepting NTLM, so the plaintext is never needed.
- The hash is typically harvested from LSASS memory, the local SAM, or NTDS.dit on a domain controller.
- Because the hash is a static, non-salted secret, it stays valid until the account password is changed.

## Tooling

- Mimikatz `sekurlsa::pth` spawns a process with an injected NTLM hash for the target identity.
- Impacket modules (`psexec.py`, `wmiexec.py`, `smbexec.py`) accept `-hashes LM:NT` to authenticate directly.
- CrackMapExec/NetExec sweep hosts with a hash to find where an account has local admin rights.

## Defensive Use

- Enforce Microsoft tiered administration so high-privilege hashes never land on low-trust hosts.
- Deploy LAPS to randomize local admin passwords and break hash reuse across machines.
- Restrict lateral SMB/RPC with host firewalls and monitor for anomalous NTLM logons (Event ID 4624 type 3).
- Enable Credential Guard and disable WDigest to reduce recoverable secrets in memory.

## Sources

- MITRE ATT&CK T1550.002 - https://attack.mitre.org/techniques/T1550/002/
- Impacket - https://github.com/fortra/impacket
- Microsoft NTLM Overview - https://learn.microsoft.com/en-us/windows-server/security/kerberos/ntlm-overview

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
