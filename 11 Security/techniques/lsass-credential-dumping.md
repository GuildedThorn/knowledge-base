---
summary: "Extracting plaintext passwords, hashes, and Kerberos tickets from the memory of the LSASS process."
status: active
tags: [security, techniques, lsass, memory, credential-access]
private: false
---

# LSASS Credential Dumping

## Purpose

Extracting plaintext passwords, hashes, and Kerberos tickets from the memory of the LSASS process.

## How It Works

- The Local Security Authority Subsystem (LSASS) caches interactive-logon secrets to support single sign-on.
- Attackers open a handle to lsass.exe and either dump its memory or parse credential structures in place.
- `MiniDumpWriteDump` (via tools like ProcDump, Task Manager, or comsvcs.dll) writes a memory image for offline parsing.
- Direct readers such as Mimikatz `sekurlsa::logonpasswords` recover NT hashes, tickets, and legacy WDigest plaintext.

## Recoverable Material

- NTLM hashes for every cached interactive session on the host.
- Kerberos TGTs and service tickets usable for pass-the-ticket.
- WDigest cleartext passwords when that legacy provider is enabled.

## Defensive Use

- Enable RunAsPPL (LSA Protection) so LSASS runs as a protected process, blocking normal handle access.
- Deploy Credential Guard to isolate secrets in a VBS-backed enclave outside LSASS reach.
- Disable WDigest cleartext caching (default off since Windows 8.1/2012 R2).
- Alert on non-standard processes opening LSASS handles with PROCESS_VM_READ (Sysmon Event ID 10).

## Sources

- MITRE ATT&CK T1003.001 - https://attack.mitre.org/techniques/T1003/001/
- Microsoft LSA Protection - https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
