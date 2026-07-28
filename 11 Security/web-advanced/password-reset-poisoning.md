---
summary: "Manipulating Host or forwarded headers so password-reset links point to an attacker-controlled domain."
status: active
tags: [security, web, password-reset, host-header]
private: false
---

# Password Reset Poisoning

## Purpose

Manipulating Host or forwarded headers so password-reset links point to an attacker-controlled domain.

## How It Works

- Many reset flows build the link's base URL from the incoming request's `Host` header (or `X-Forwarded-Host`) rather than a fixed configured value.
- The attacker requests a reset for the victim's account while supplying a malicious host, so the emailed link embeds the attacker's domain with the valid token.
- When the victim clicks the link, their browser sends the secret reset token to the attacker's server, enabling account takeover.
- Variants abuse `X-Forwarded-Host`, dangling ambiguous headers, or Host override headers that reverse proxies pass through.

## Defensive Notes

- Generate reset URLs from a server-side configured canonical domain, never from request headers.
- Validate the incoming `Host` header against an allowlist and drop untrusted forwarding headers at the edge.
- Keep reset tokens short-lived, single-use, and unpredictable; invalidate on use or password change.
- Consider decoupling delivery (send a code the user enters) so the link's host cannot leak the token.

## Sources

- PortSwigger Password Reset Poisoning - https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning
- OWASP Forgot Password Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
