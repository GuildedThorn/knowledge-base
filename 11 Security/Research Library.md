---
summary: Hub for the ingested security research library — technical writeups, threat reports, and papers digested into per-topic notes across offense, defense, and analysis.
status: active
tags: [security, research-library, index]
private: false
---

# Research Library

A curated corpus of real security technical writeups, vendor threat reports, conference papers, and researcher blogs — each digested into a dense, source-cited vault note. Every note carries a `## Sources` section with the URLs it was built from. Scope is **authorized research and education**.

This hub sits above ten topic collections; each collection has its own index.

## Collections

- [Research Source Corpus](kb://11-security-research-source-corpus) — source bibliography for the library: papers, standards, docs, books, vendor research, and writeups.
- [Threat Intel — Index](kb://11-security-threat-intel-threat-intel-index) — malware families & APT groups (Emotet, TrickBot/Qakbot, LockBit, Mirai, Stuxnet, Lazarus, APT29, FIN7, SolarWinds)
- [Techniques — Index](kb://11-security-techniques-techniques-index) — ATT&CK technique deep-dives (injection, DLL sideloading, AMSI/ETW bypass, LSASS dumping, persistence, LOLBins)
- [Exploit Dev — Index](kb://11-security-exploit-dev-exploit-dev-index) — memory-corruption bug classes and mitigation bypasses (stack/heap, UAF, ROP, CFG/DEP/ASLR)
- [Reversing — Index](kb://11-security-reversing-reversing-index) — static/dynamic RE, packers, anti-analysis, obfuscation, YARA, shellcode
- [Web-Advanced — Index](kb://11-security-web-advanced-web-advanced-index) — SSRF, deserialization, request smuggling, prototype pollution, JWT, OAuth/SAML, SSTI, GraphQL
- [C2 & Post-Ex — Index](kb://11-security-c2-postex-c2-postex-index) — C2 framework internals, malleable profiles, lateral movement, Kerberos, BloodHound
- [DFIR & Detection — Index](kb://11-security-dfir-detection-dfir-detection-index) — detection engineering, Sigma, memory forensics, threat hunting, IR lifecycle
- [Crypto & Ransomware — Index](kb://11-security-crypto-ransomware-crypto-ransomware-index) — ransomware crypto, supply-chain, code-signing abuse, hashing/cracking
- [Cloud & Container — Index](kb://11-security-cloud-container-cloud-container-index) — AWS/Azure/GCP attacks, Kubernetes, container escapes, IMDS SSRF, CI/CD
- [Mobile & Hardware — Index](kb://11-security-mobile-hardware-mobile-hardware-index) — Android/iOS RE, firmware, IoT, fault injection, baseband, UEFI bootkits

## Conventions

- One topic per note; every claim grounded in a fetched source (see each note's `## Sources`).
- Techniques mapped to **MITRE ATT&CK** IDs where documented.
- Offensive material is defensively framed — mechanics plus detection/mitigation.

## Related

- [Security Map](kb://01-maps-security-map)
- [Malware Analysis Workflow](kb://11-security-malware-analysis-malware-analysis-workflow)
- [Blue Team - Detection Engineering](kb://11-security-blue-team-detection-engineering)
- [11-security](kb://hub-11-security)
