---
summary: HTB Cobblestone engagement log — custom PHP app suite (Billy 1.9.2), vote SSRF/XSS reviewer lead.
status: in-progress
tags: [security, htb, engagement, cobblestone]
private: false
---

# HTB: Cobblestone — 10.129.67.87

Authorized Hack The Box engagement. Step log; each step tagged 🟢 lead / 🐇 rabbit hole / 🔴 dead end.

> **IP rotated** — box respawned from `10.129.232.170` → **`10.129.67.87`** (2026-07-23). Service profile identical (re-confirmed below). Fresh spawn = prior `vote` registration (`thornpwn`) wiped; re-register.

## Surface (recon) — re-confirmed at new IP

- **22/tcp** — OpenSSH 9.2p1 Debian 2+deb12u7 (Debian 12 bookworm). Host keys unchanged from prior spawn.
- **80/tcp** — Apache 2.4.62 (Debian). Redirects to **`cobblestone.htb`** (vhost-based). Minecraft-server theme.
- Custom PHP app suite **"Proudly coded by Billy (bybilly.uk) — Version: 1.9.2"** across all vhosts.
- Full TCP sweep re-running → `~/htb/cobblestone/ports.txt`.

### vhosts / apps
- **cobblestone.htb** — marketing site. Local **`skins.php`** (empty on GET — needs param?). Links out to deploy + vote.
- **deploy.cobblestone.htb** — "Deploy Minecraft Server". Home = team blurb (imgs: jeremy, josh, katrina, sam), **no visible form yet** — enumerate endpoints. 🟢 (deploy = likely RCE/SSRF)
- **vote.cobblestone.htb** — login-gated voting app. Open **registration** (`register.php`), login (`login_verify.php`). 🟢

## Leads (carried over — re-verify against fresh spawn)
- **vote `suggest.php`** (POST `url`) stores a "server suggestion" pending **`Approved: false`** → an approver (admin/bot) likely reviews it. URL rendered as plain text in `details.php?id=N`. Test **stored XSS / SSRF via the reviewer**. 🟢 PRIMARY
- **vote `details.php?id=`** renders Suggestion name / Approved / Owner-ID / Votes. `id=1'` == `id=1` length → looks `intval()`'d, **probably not SQLi**. 🐇
- Team names = candidate usernames/SSH: **jeremy, josh, katrina, sam**.

## Env notes
- Attacker tun0: **10.10.14.136**.
- `/etc/hosts` is **read-only** on this box → use `curl --resolve <vhost>:80:10.129.67.87` (new IP).
- HTTP catcher for SSRF: port 8000 was in use; use an alt port (e.g. 8888).

## TODO
- Re-register on `vote`, re-test `suggest.php` reviewer behaviour (SSRF fetch vs plain XSS render).
- Fuzz endpoints on deploy + vote; vhost-fuzz for more subdomains (dev? git?).
- Inspect `skins.php` params; check for `.git`/source exposure of Billy's app.

## Methodology
- Playbook: [Web App Testing](kb://11-security-playbook-web-app-testing) · [Recon](kb://11-security-playbook-recon-enumeration) · payload sheets: [SSRF via XSS/reviewer]→[XSS](kb://11-security-payloads-xss-payloads), [LFI](kb://11-security-payloads-lfi-payloads).
