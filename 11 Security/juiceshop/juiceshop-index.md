---
title: "Juice Shop — Campaign Index"
tags: [juiceshop, pentest, web, owned]
target: http://localhost:3000
app: OWASP Juice Shop v20.1.1
status: owned
authorization: authorized lab / deliberately-vulnerable training target
started: 2026-07-23
completed: 2026-07-23
---

# Juice Shop — `localhost:3000` — 🏴 owned (unauth → admin)

Authorized, non-persistent assessment of OWASP Juice Shop **v20.1.1**. No writes, no data mutation, no persistence. Full consolidated report: [[Juice Shop Assessment 2026-07-23]]. Tooling: Crossview MITRE silo + `osv-scanner` (via `nix develop`), `nmap`, `curl`.

## 🏁 Findings

| ID | Finding | Severity | CWE | Step |
|----|---------|----------|-----|------|
| F1 | SQLi authentication bypass → admin | 🔴 Critical | CWE-89 | [[juiceshop-04-sqli-auth-bypass\|04]] |
| F2 | Poison-Null-Byte access-control bypass on `/ftp` | 🟠 High | CWE-22 / CWE-158 | [[juiceshop-02-ftp-nullbyte\|02]] |
| F3 | BOLA — full user directory dump | 🟠 High | CWE-639 / CWE-284 | [[juiceshop-05-bola-user-dump\|05]] |
| F4 | 184 CVEs in dependencies | 🟠 High | CWE-1321 / CWE-347 | [[juiceshop-03-sca-dependencies\|03]] |
| F5 | Wildcard CORS | 🟡 Medium | CWE-942 | [[juiceshop-01-recon-nmap\|01]] |
| F6 | Directory listing + open Swagger | ⚪ Info | CWE-548 | [[juiceshop-01-recon-nmap\|01]] |

## Steps

1. [[juiceshop-01-recon-nmap]] — nmap, headers, CORS, `/ftp`, Swagger 🟢
2. [[juiceshop-02-ftp-nullbyte]] — Poison-Null-Byte leaks the lockfile 🟢
3. [[juiceshop-03-sca-dependencies]] — osv-scanner: 184 CVEs 🟢
4. [[juiceshop-04-sqli-auth-bypass]] — `' OR 1=1--` → admin JWT 🟢
5. [[juiceshop-05-bola-user-dump]] — stolen token dumps all 22 users 🟢
6. [[juiceshop-06-mitre-killchain]] — Crossview CAPEC→CWE→ATT&CK tree 🟢

## The full kill chain

```
/ftp dir listing (CWE-548)
   → GET /ftp/package-lock.json.bak%2500.md  (403→200, CWE-22+158)  ── leaks lockfile → SCA
   → POST /rest/user/login  ' OR 1=1--  (CWE-89)  ── admin RS256 JWT, no password
   → GET /api/Users + stolen token  (CWE-639)  ── dump all 22 users
```

## Loot / creds

- **Admin JWT** (RS256, `id=1 email=admin@juice-sh.op role=admin`) — obtained via SQLi, session-only.
- **package-lock.json.bak** (750 KB, legacy `6.2.0-SNAPSHOT`) — exfiltrated via null-byte bypass.
- **User directory** (22 accounts: id/email/role/lastLoginIp/deluxeToken) — password field stripped in v20.
- Ephemeral loot dir: `/tmp/js-assess/` (`sqli.json`, `users_auth.json`, `osv.clean.json`).

## Notes for cleanup / report

- All activity read-only; nothing persisted server-side. No accounts created, no data altered.
- SOC breadcrumb + detection IOCs logged in [[SIEM Review Log]] (2026-07-23 18:25, marked as authorized exercise).
- Root cause to fix first = **F1 (parameterize the login query)** — it collapses the whole chain.
- Related: [[Security Map]] · reusable methodology in `11 Security/playbook/` and `11 Security/payloads/`.
