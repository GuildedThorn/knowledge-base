---
summary: "Catalog of the Ignitetechnologies/Mindmap collection — 100+ pentest/blue-team/compliance visual mind maps, grouped by domain and mapped to existing vault notes."
status: active
tags: [security, reference, mindmaps, index]
private: false
---

# Mindmap Library

## Purpose

Discovery index for the **Hacking Articles / Ignitetechnologies "Mindmap"** collection — 104 visual mind maps across 78 topics plus 9 standalone diagrams, covering offensive methodology, tooling, blue-team/DFIR, and compliance frameworks. This note catalogs what the collection holds and links each domain to the vault note that already covers it, so the maps are a discoverable reference rather than an opaque image dump.

> Scope: methodology reference for **authorized** engagements only (owned or explicitly permitted targets), consistent with the [Pentest Playbook](kb://11-security-playbook-pentest-playbook-index).

## Source

- Repo: `https://github.com/Ignitetechnologies/Mindmap` (commit `8acfe75`, 2026-07-21)
- Publisher: Hacking Articles — `https://www.hackingarticles.in/`
- Format: each topic ships as a PDF plus Normal/HD/UHD PNG renders; a few folders link a companion article (Nmap → `Nmap-For-Pentester`, Mimikatz and Impacket → hackingarticles.in guides).
- **Not vendored:** the ~30 MB of binary PDF/PNG assets are intentionally left in the upstream repo, not copied into this text-first vault. To view a map, clone the repo or open it on GitHub; if a local copy is ever wanted, prefer the single PDF per topic under `91 Images/`, not the full multi-resolution set.

## Catalog

### Recon, OSINT & search
OSINT Framework · Shodan Filters · Censys · Google Hacking Dorks · Google Search Operators · Github Dorks · Red Team Dorks · Search Engine for Pentester · Subdomain Enumeration Tools · Enumeration · SMB Enumeration.
→ vault: [Recon & Enumeration](kb://11-security-playbook-recon-enumeration).

### Scanning, fuzzing & content discovery
nmap · Vulnerability Scanners · Web Directory Scanners · Feroxbuster · FFUF · gobuster · wfuzz · httpx · wpscan.
→ vault: [nmap](kb://11-security-tools-nmap) · [ffuf / gobuster](kb://11-security-tools-ffuf-gobuster).

### Web application testing
OWASP Web · OWASP Testing Checklist · OWASP Mobile Top 10 · Burp Suite · Burp Extensions · Sqlmap · XSS Testing Tools · SSRF Tools · HTTP Status Codes · Firefox Pentest Add-ons · Web App Pentest Lab (Docker).
→ vault: [Web Application Testing](kb://11-security-playbook-web-app-testing) · [Burp Suite](kb://11-security-tools-burp-suite) · [sqlmap](kb://11-security-tools-sqlmap) · [Payload Cheat Sheets](kb://11-security-payloads-payloads-index).

### Password attacks & cracking
Hashcat · John · John The Ripper Converter · hydra · medusa · Wordlists Generator.
→ vault: [Password Attacks & Hash Cracking](kb://11-security-playbook-password-attacks) · [hashcat / john](kb://11-security-tools-hashcat-john).

### Active Directory & Windows
AD Enumeration · AD Pentest · Active Directory Pentesting · Crackmapexec · NetExec (NXC) · Impacket · Mimikatz · PowerShell Empire · Windows Privileges · Windows Privs · Windows Meterpreter · Privs Tools.
→ vault: [Active Directory](kb://11-security-playbook-active-directory) · [Windows Privilege Escalation](kb://11-security-playbook-windows-privesc) · [impacket / netexec](kb://11-security-tools-impacket-netexec) · [BloodHound](kb://11-security-tools-bloodhound) · [Techniques Index](kb://11-security-techniques-techniques-index) (kerberoasting, LSASS dumping, pass-the-hash).

### Linux privilege escalation
Linux Privs · Capabilities Privilege Escalation (GTFOBins) · Privilege Escalation Cheatsheet.
→ vault: [Linux Privilege Escalation](kb://11-security-playbook-linux-privesc).

### Exploitation & C2 frameworks
Metasploit Framework · Windows Meterpreter · Meterpreter Android · PowerShell Empire.
→ vault: [Metasploit](kb://11-security-tools-metasploit) · [Reverse Shells & Payloads](kb://11-security-playbook-reverse-shells).

### Wireless, network & traffic
Aircrack-ng · Wireless Pentest Tools · Wireshark · Wireshark Display Filter · tcpdump · TShark · ICMP Status Code.
→ vault: [Wireshark](kb://11-security-tools-wireshark).

### Cloud, container & DevOps
Cloud Security Framework · Container Security · Docker Command Cheat Sheet · DevOps Roadmap · DevOps Tools · Web Application Pentest Lab (Docker) · Security Automation.

### Frameworks, compliance & governance
MITRE ATT&CK matrices (Enterprise, Windows, Linux, macOS, Cloud, Network, Containers, Android, iOS, Mobile Tactics, plus Credential Access / Defense Evasion / Command and Control tactic maps and a D3FEND map) · NIST Cybersecurity Framework · ISO 27001:2022 Controls · GDPR · HIPAA · FISMA · SOC 2.
→ vault: [Zero Trust Architecture — NIST](kb://11-security-zero-trust-architecture-nist); map ATT&CK techniques to live CVEs with the [crossview](kb://hub-11-security) skill.

### Blue team, DFIR & reversing
Blue Teaming · Digital Forensics Tools · IDA Pro Cheatsheet · Defensive Linux Security Tools.
→ vault: [Blue Team — Detection Engineering](kb://11-security-blue-team-detection-engineering) · [Malware Analysis Workflow](kb://11-security-malware-analysis-malware-analysis-workflow) · [Ghidra](kb://11-security-tools-ghidra).

### Tool collections
Bug Bounty Tools · Penetration Testing Tools · Red Team And Blue Team Tools · Offensive Linux Security Tools · Defensive Linux Security Tools · OSCP Practice Tools.
→ vault: [Offensive Tools Index](kb://11-security-tools-tools-index).

### Threat landscape
Types of Cyber Security Attacks · Types of Social Engineering Attacks · List of Ransomware · Famous Cyber Security Hacks · Zero-Day CVEs (2023) · Cyber Security Technologies · Security 360° · Red Teaming.
→ vault: [Threat Intel Index](kb://11-security-threat-intel-threat-intel-index).

### Training platforms
HTB Cheat Sheet · HTB BloodHound CTF · HTB Pivoting, Tunneling & Port Forwarding · HTB (Web) · TryHackMe.
→ vault: [Pivoting & Tunneling](kb://11-security-playbook-pivoting-tunneling); live logs in the HTB campaigns off the [Security Map](kb://01-maps-security-map).

### Privacy
Privacy Tools · Privacy Email Accounts · Privacy Search Engines.

## Related

- [Research Library](kb://11-security-research-library)
- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
