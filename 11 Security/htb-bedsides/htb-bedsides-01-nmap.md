---
title: "HTB Bedsides · 01 · Nmap service scan"
tags: [htb, recon, nmap]
verdict: could-go-somewhere
---

# 01 · Nmap `-sC -sV -Pn` — 🟢 could go somewhere

Command: `nmap -sC -sV -Pn 10.129.66.223`

## Result

| Port | State | Service | Version |
|------|-------|---------|---------|
| 22   | open  | ssh     | OpenSSH 10.0p2 Debian 7+deb13u4 |
| 80   | open  | http    | Apache 2.4.68 (Debian) |
| 3000 | filtered | ppp | — |

- Port 80 does **not follow redirect** to `http://bedside.htb/` → virtual host. Need `/etc/hosts` entry.
- Port 3000 **filtered** — classic dev-app port (Gitea/Node/Grafana). Likely reachable only after a foothold or via SSRF/proxy. Note for later.
- OpenSSH 10.0p2 / Apache 2.4.68 are very recent (Debian 13) → version-based CVE path unlikely; focus on the web app.

## Verdict — 🟢

Web on 80 is the front door. Next: add `bedside.htb` to hosts, browse, then vhost/dir fuzz. Port 3000 is a 🟢 parked lead once we have any internal access.

→ next: [[htb-bedsides-02-web-80]]
