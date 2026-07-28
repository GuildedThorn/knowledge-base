---
summary: Modular Windows loader that began as a 2014 banking trojan, evolved into a malware-as-a-service delivery platform spread by thread-hijacking malspam, dropping TrickBot/Qakbot/Cobalt Strike and ransomware.
status: active
tags: [security, threat-intel, emotet, malware]
private: false
---

# Emotet

Emotet (a.k.a. Geodo, MITRE S0367) is one of the most prolific malware families of the past decade — a polymorphic, modular Windows loader operated as malware-as-a-service and associated with the Wizard Spider (G0102) ecosystem.

## Overview

First identified in June 2014 as a banking trojan that intercepted network traffic to steal credentials from German, Austrian, and later Swiss banks. By ~2018 it pivoted from direct theft to a downloader/loader delivery platform run as a paid service, distributing other actors' payloads. Before disruption it ran three parallel botnets — Epoch 1, Epoch 2, Epoch 3 — and infected 1.6M+ machines. A coordinated Europol/Eurojust operation seized its infrastructure in January 2021, with a BKA-authored uninstall module purging hosts by 25 April 2021. It returned in November 2021 when TrickBot C2 servers instructed infected machines to download a fresh Emotet build, rapidly rebuilding the botnet.

## Delivery / Initial Access

Primarily malspam using email thread hijacking — hijacked legitimate threads, forwards, and "RE:" reply spoofing with minimal body text to appear as document shares. Attachments: macro-enabled Word (DOCM), Excel with OLE2 macros (XLSM), and password-protected ZIP archives (password included in the email body to defeat scanning). Later variants used malicious LNK files with embedded Base64 PowerShell, and malicious links.

## Capabilities

Modular downloader/loader that fetches additional modules and second-stage payloads. Documented functions: browser/stored-password theft, Outlook email and contact scraping, LSASS credential dumping (Mimikatz), SMB spreading via EternalBlue (MS17-010) and admin-share brute forcing, and Wi-Fi enumeration. Anti-analysis: detects VM/sandbox and lays dormant. Known follow-on drops: TrickBot, Qakbot, IcedID, Cobalt Strike, and ransomware (Ryuk; Quantum in a 2022 DFIR case).

## Infrastructure / C2

Tiered architecture split across Epoch 1/2/3 clusters. HTTP-based C2 frequently over non-standard ports (observed 20, 22, 443, 7080, 50000), traffic encrypted (RSA/symmetric) and Base64-encoded. Compromised legitimate websites/hosts serve as C2 and payload-staging servers.

## MITRE ATT&CK

- Initial Access: T1566.001 Spearphishing Attachment, T1566.002 Spearphishing Link
- Execution: T1059.001 PowerShell, T1059.003 Windows Command Shell, T1059.005 Visual Basic, T1047 WMI, T1204.001/.002 User Execution
- Persistence: T1547.001 Registry Run Keys, T1543.003 Windows Service, T1053.005 Scheduled Task
- Defense Evasion: T1027.002 Software Packing, T1055.001 DLL Injection, T1055.012 Process Hollowing, T1218.010 Regsvr32, T1140 Deobfuscate/Decode Files, T1620 Reflective Code Loading
- Credential Access: T1110.001 Password Guessing, T1555.003 Credentials from Web Browsers, T1003.001 LSASS Memory, T1552.001 Credentials In Files
- Discovery: T1087.003 Email Account Discovery, T1135 Network Share Discovery, T1016.002 Wi-Fi Discovery
- Lateral Movement: T1021.002 SMB/Admin Shares, T1210 Exploitation of Remote Services, T1570 Lateral Tool Transfer
- Collection: T1114.001 Local Email Collection, T1040 Network Sniffing
- C2/Exfil: T1071.001 Web Protocols, T1571 Non-Standard Port, T1573.001 Symmetric Cryptography, T1105 Ingress Tool Transfer

## Detection & IOCs

- Persistence: Registry Run key launching the Emotet DLL (often via regsvr32.exe); auto-start Windows Service re-executing after reboot; scheduled tasks.
- Execution: DLL copied to a randomly named folder under %TEMP%, run via regsvr32.exe/rundll32.exe; Office macros spawning PowerShell child processes.
- Post-infection recon: `systeminfo`, `ipconfig /all`, `nltest /dclist:`.
- Detection patterns: Office process spawning PowerShell; LSASS access with 0x1010 mask (Mimikatz); SMB executable transfers; follow-on Cobalt Strike beacons and rclone exfil to Mega.nz. Network IOCs rotate rapidly — treat as time-bound.

## Sources

- MITRE ATT&CK — Emotet, Software S0367 — https://attack.mitre.org/software/S0367/
- Malwarebytes — Emotet — https://www.malwarebytes.com/emotet
- The DFIR Report — Emotet Strikes Again: LNK File Leads to Domain Wide Ransomware (2022) — https://thedfirreport.com/2022/11/28/emotet-strikes-again-lnk-file-leads-to-domain-wide-ransomware/
- Cisco Talos — Back from the dead: Emotet re-emerges (2021) — https://blog.talosintelligence.com/2021/11/emotet-back-from-the-dead.html

## Related
- [Threat Intel — Index](kb://11-security-threat-intel-threat-intel-index)
- [Malware Analysis Workflow](kb://11-security-malware-analysis-malware-analysis-workflow)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
