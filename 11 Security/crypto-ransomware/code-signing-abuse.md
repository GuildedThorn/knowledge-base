---
summary: "Code-signing abuse turns trust infrastructure into an evasion and supply-chain risk when certificates, build systems, or signed binaries are misused."
status: active
tags: [security, code-signing, supply-chain, evasion]
private: false
---

# Code-Signing Abuse

## Purpose

Code-signing abuse turns trust infrastructure into an evasion and supply-chain risk when certificates, build systems, or signed binaries are misused.

## Key Ideas

- Abuse paths include stolen certificates, weak signing keys, compromised build pipelines, signed malware, vulnerable signed drivers, and signed-binary proxy execution.
- A valid signature proves signing-key control and file integrity since signing; it does not prove the software is safe.
- Revocation and trust-store propagation are operationally slow compared with attacker use.

## Defensive Use

- Protect signing keys with hardware-backed controls, strong approval workflows, audit logs, and separation between build and signing roles.
- Monitor new signed executables, rare publishers, vulnerable drivers, and trusted binaries used outside expected command/parent contexts.

## Sources

- Microsoft - Driver code signing - https://learn.microsoft.com/en-us/windows-hardware/drivers/install/code-signing
- MITRE ATT&CK - System Binary Proxy Execution T1218 - https://attack.mitre.org/techniques/T1218/
- CISA - Securing Software Supply Chain series - https://www.cisa.gov/news-events/alerts/2022/11/17/cisa-nsa-and-odni-release-guidance-customers-securing-software-supply-chain

## Related

- [Crypto & Ransomware - Index](kb://11-security-crypto-ransomware-crypto-ransomware-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
