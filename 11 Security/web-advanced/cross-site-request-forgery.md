---
summary: "Forcing an authenticated user's browser to issue unwanted state-changing requests to a trusting application."
status: active
tags: [security, web, csrf, token, samesite]
private: false
---

# Cross-Site Request Forgery

## Purpose

Forcing an authenticated user's browser to issue unwanted state-changing requests to a trusting application.

## Attack Model

- Exploits ambient authority: browsers automatically attach cookies (and Basic/NTLM credentials) to any request to a site, regardless of who initiated it.
- An attacker-controlled page auto-submits a form or fires a request to the target; the victim's session cookie authorizes it.
- Requires a state-changing action, cookie-based session handling, and no unpredictable request parameters the attacker cannot guess.

## Defenses

- Synchronizer token pattern: server issues a per-session (or per-request) unguessable token that must accompany state-changing requests and is validated server-side.
- `SameSite` cookie attribute (`Lax` or `Strict`) stops cookies riding on cross-site requests; `Lax` is the modern browser default but still allows top-level GET navigations.
- Double-submit cookie and custom-header checks (e.g. requiring `X-Requested-With`) work when tokens cannot be stored server-side.
- Validating the `Origin`/`Referer` header provides defense in depth.

## Common Bypasses

- Tokens not tied to the user session, or accepted when omitted/blank, defeat the protection.
- `SameSite=Lax` gaps: GET requests that change state, or method override tricks, can slip through.
- CSRF combined with GET-based actions, weak referer checks, or token leakage via referer to third parties.

## Sources

- PortSwigger Web Security Academy - https://portswigger.net/web-security/csrf
- OWASP CSRF Prevention Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
