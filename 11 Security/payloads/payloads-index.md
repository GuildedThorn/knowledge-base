---
summary: Web-injection payload cheat sheets distilled from PayloadsAllTheThings + HackTricks — SQLi, XSS, LFI, cmdi, upload, LOLBins.
status: active
tags: [security, payloads, web, reference, index]
private: false
---

# Payload Cheat Sheets — Index

Copy-paste payload libraries for the web attack classes, distilled from **[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)** and **[HackTricks](https://book.hacktricks.xyz)**. Methodology (when/why) lives in [Web Application Testing](kb://11-security-playbook-web-app-testing); this is the "what do I paste" layer.

> Each note links its upstream source — go there for the exhaustive list; these are the reliable subset.

## Cheat sheets

- [SQL Injection payloads](kb://11-security-payloads-sqli-payloads) — auth bypass, UNION, blind, WAF bypass
- [XSS payloads](kb://11-security-payloads-xss-payloads) — PoC, filter bypasses, context breakouts, exfil
- [LFI / Path Traversal payloads](kb://11-security-payloads-lfi-payloads) — traversal, PHP wrappers, LFI→RCE
- [Command Injection payloads](kb://11-security-payloads-command-injection-payloads) — separators, blind, filter/space bypass
- [File Upload bypass payloads](kb://11-security-payloads-upload-bypass-payloads) — extension/MIME/magic-byte tricks, webshells
- [GTFOBins / LOLBAS Quick Reference](kb://11-security-payloads-gtfobins-lolbas-quickref) — living-off-the-land privesc & download/exec

Reverse-shell one-liners live in [Reverse Shells & Payloads](kb://11-security-playbook-reverse-shells).

## Related

- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index)
- [Web Application Testing](kb://11-security-playbook-web-app-testing)
- [Offensive Tools — Index](kb://11-security-tools-tools-index)
