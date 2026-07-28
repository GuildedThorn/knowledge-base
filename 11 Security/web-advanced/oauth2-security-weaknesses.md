---
summary: "Common OAuth 2.0 flaws including redirect_uri manipulation, CSRF via missing state, and token leakage."
status: active
tags: [security, web, oauth, redirect-uri, token]
private: false
---

# OAuth 2.0 Security Weaknesses

## Purpose

Common OAuth 2.0 flaws including redirect_uri manipulation, CSRF via missing state, and token leakage.

## Key Weaknesses

- `redirect_uri` manipulation: loose matching (prefix, substring, or open-redirect chaining) lets an attacker redirect the authorization code or token to a domain they control.
- Missing/unvalidated `state`: without a bound, unguessable state value the authorization callback is vulnerable to CSRF, letting an attacker link their account to a victim's session.
- Implicit-flow token leakage: access tokens returned in the URL fragment can leak via Referer headers, browser history, or a compromised redirect target.
- Authorization-code injection and replay when PKCE is absent on public clients.

## Defensive Notes

- Require exact, pre-registered `redirect_uri` matching; disallow wildcards and open redirects on registered hosts.
- Enforce a cryptographically random `state` bound to the user session, and use PKCE (S256) for all clients per RFC 9700.
- Prefer the authorization-code flow; RFC 9700 deprecates the implicit grant and resource-owner password grant.
- Bind tokens to clients, keep token lifetimes short, and validate `aud`/`iss` at the resource server.

## Sources

- RFC 6749 OAuth 2.0 - https://datatracker.ietf.org/doc/html/rfc6749
- OAuth 2.0 Security Best Current Practice (RFC 9700) - https://datatracker.ietf.org/doc/html/rfc9700
- PortSwigger Web Security Academy - https://portswigger.net/web-security/oauth

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
