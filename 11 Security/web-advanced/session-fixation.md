---
summary: "Forcing a victim to use an attacker-known session identifier so the session is hijacked after authentication."
status: active
tags: [security, web, session, fixation]
private: false
---

# Session Fixation

## Purpose

Forcing a victim to use an attacker-known session identifier so the session is hijacked after authentication.

## How It Works

- The attacker obtains or sets a valid session ID, then induces the victim to authenticate under that same ID.
- Because the application does not issue a fresh ID at login, the attacker's pre-known identifier becomes an authenticated session.
- Common vectors: session IDs accepted in the URL query string, a `Set-Cookie` planted via an XSS or a permissive subdomain, or a login form that carries a pre-set token.
- Distinct from session hijacking by theft: here the ID is chosen before authentication rather than stolen afterward.

## Defensive Notes

- Regenerate the session identifier on every privilege change, especially at successful login, and invalidate the pre-login ID.
- Never accept session IDs from URL parameters; store them only in cookies.
- Set `HttpOnly`, `Secure`, and `SameSite` on session cookies and scope them to the exact host.
- Bind sessions to attributes (e.g. user agent) with care, enforce idle/absolute timeouts, and reject unknown incoming session IDs.

## Sources

- OWASP Session Fixation - https://owasp.org/www-community/attacks/Session_fixation
- ACROS Session Fixation Paper - https://www.acrossecurity.com/papers/session_fixation.pdf

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
