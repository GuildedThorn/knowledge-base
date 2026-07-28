---
summary: "Modern ransomware combines file encryption, data theft, leak-site extortion, and operational pressure against recovery workflows."
status: active
tags: [security, ransomware, crypto, extortion]
private: false
---

# Ransomware Encryption and Extortion

## Purpose

Modern ransomware combines file encryption, data theft, leak-site extortion, and operational pressure against recovery workflows.

## Key Ideas

- Encryption is only one pressure mechanism; many groups steal data first and threaten publication, regulators, partners, or customers.
- Encryption implementation often uses hybrid crypto: per-file/session symmetric keys protected by asymmetric keys controlled by the operator.
- Fast encryption campaigns typically pre-stage discovery, privilege escalation, backup tampering, and exfiltration before detonation.

## Defensive Use

- Detect backup deletion, mass file rename/write, shadow-copy tampering, suspicious archive/exfil staging, and EDR disablement.
- Keep immutable/offline backups, pre-tested restore procedures, and legal/communications decisions in the ransomware playbook.

## Sources

- CISA StopRansomware Guide - https://www.cisa.gov/stopransomware/ransomware-guide
- CISA LockBit advisory - https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
- NIST IR 8374 Ransomware Risk Management - https://csrc.nist.gov/pubs/ir/8374/r1/final

## Related

- [Crypto & Ransomware - Index](kb://11-security-crypto-ransomware-crypto-ransomware-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
