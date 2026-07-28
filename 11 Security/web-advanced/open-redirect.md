---
summary: "Unvalidated redirect targets that send users to attacker sites, enabling phishing and OAuth token theft."
status: active
tags: [security, web, open-redirect, phishing]
private: false
---

# Open Redirect

## Purpose

Unvalidated redirect targets that send users to attacker sites, enabling phishing and OAuth token theft.

## How It Works

- An app reads a destination from user-controlled input (query param, form field, path) and issues an HTTP 3xx or client-side redirect without validating it.
- Common sink names: `url`, `next`, `return`, `returnUrl`, `redirect`, `dest`, `continue`, `RelayState`.
- Because the initial link points at a trusted domain, users and email filters trust it before the browser silently lands on the attacker host.
- OAuth/SSO flows are high value: a permissive `redirect_uri` can leak authorization codes or access tokens to an attacker-controlled endpoint.

## Bypasses

- Scheme abuse: `javascript:`, `data:`, or protocol-relative `//evil.com` that inherits the current scheme.
- Backslash and mixed slashes: `/\evil.com`, `https:/evil.com` parsed differently by browser vs. server.
- Userinfo trick: `https://trusted.com@evil.com` where everything before `@` is credentials, not host.
- Encoding and whitespace: percent-encoding, embedded newlines, or Unicode lookalikes to defeat naive string checks.

## Defensive Use

- Prefer indirection: map an allowlisted key to a server-side URL rather than accepting a raw URL.
- If URLs are unavoidable, enforce a strict allowlist of hosts and require relative paths starting with a single `/` (reject `//` and `\`).
- Parse the URL and compare the resolved host against the allowlist; do not use substring matching.
- For OAuth, register exact `redirect_uri` values and match them literally.

## Sources

- OWASP Unvalidated Redirects and Forwards Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html
- CWE-601 URL Redirection to Untrusted Site - https://cwe.mitre.org/data/definitions/601.html

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
