---
title: "Juice Shop · 01 · Recon — nmap, headers, surface"
tags: [juiceshop, recon, nmap]
verdict: multiple-leads
---

# 01 · Recon — 🟢 rich surface

## Commands

```bash
nmap -sV -p3000 localhost
curl -sI http://localhost:3000/
curl -s http://localhost:3000/rest/admin/application-version
curl -s http://localhost:3000/robots.txt
curl -s http://localhost:3000/ftp/
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/api-docs/
```

## Result

- `:3000` open — Express. Version endpoint → **`{"version":"20.1.1"}`**.
- Headers: `Access-Control-Allow-Origin: *` (**F5 — wildcard CORS, CWE-942**), `X-Recruiting: /#/jobs`, `X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`, `Feature-Policy: payment 'self'`.
- `robots.txt` → `Disallow: /ftp` (points right at it; doesn't restrict it).
- `/ftp/` returns a **directory listing** (**F6 — CWE-548**): `package-lock.json.bak`, `package.json.bak`, `coupons_2013.md.bak`, `incident-support.kdbx`, `encrypt.pyc`, `eastere.gg`, `suspicious_errors.yml`, `announcement_encrypted.md`, `acquisitions.md`, `legal.md`.
- `/api-docs/` (Swagger UI) → **HTTP 200**, unauthenticated.

## Next

- `.bak`/`.kdbx` in `/ftp` are the obvious target → try to pull them → [[juiceshop-02-ftp-nullbyte]].
- Open Swagger enumerates the API for later auth/BOLA testing.
