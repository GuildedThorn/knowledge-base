---
title: "Juice Shop · 03 · SCA — osv-scanner on leaked lockfile"
tags: [juiceshop, sca, supply-chain, crossview]
verdict: confirmed
cwe: [CWE-1321, CWE-347, CWE-1035]
---

# 03 · Dependency SCA — 🟢 F4 confirmed (184 CVEs)

Source = `package-lock.json.bak` from [[juiceshop-02-ftp-nullbyte]]. Scanner = Crossview's bundled `osv-scanner`.

## Commands

```bash
cd ~/Documents/crossview
nix develop -c osv-scanner scan --lockfile=/tmp/js-assess/package-lock.json --format=json \
  > /tmp/js-assess/osv.json
# NB: dev-shell banner pollutes stdout — strip everything before the first '{' before parsing.
```

## Result

- **144** packages with known vulns · **324** advisories · **184** unique CVEs (1,458 packages scanned).
- Worst offenders (advisory count): `tar` 41 · `handlebars` 25 · `lodash` 23 · `minimatch` 15 · `js-yaml` 8 · `socket.io-parser` 8 · `xmldom` 8 · `jsonwebtoken` 7 · `qs` 7 · `sanitize-html` 7 · `brace-expansion` 6 · `minimist` 6 · `tmp` 6 · `ajv` 5 · `multer` 5.
- Themes: **prototype pollution** (lodash/handlebars/minimist → CWE-1321), **template-injection / RCE** (`babel-traverse` CVE-2023-45133, C:H/I:H/A:H), **JWT verification issues** (jsonwebtoken → CWE-347), **ReDoS/DoS** (tar, ajv, ansi-regex).

## Notes

- This is the *leaked historical* manifest, not the live v20 tree — but a full historical dep graph handed to an attacker is a gadget-chain roadmap.
- Fix: regenerate lockfile on current majors; add `osv-scanner`/Dependabot to CI, fail on High+.

## Next

- Move from supply-chain to the live app → [[juiceshop-04-sqli-auth-bypass]].
