---
summary: "Reflected and stored XSS that inject script into pages, hijacking sessions and actions in the victim context."
status: active
tags: [security, web, xss, reflected, stored]
private: false
---

# Cross-Site Scripting Fundamentals

## Purpose

Reflected and stored XSS that inject script into pages, hijacking sessions and actions in the victim context.

## Core Model

- XSS occurs when an application places attacker-controlled data into a page without proper context-aware encoding, so the browser executes it as script.
- Script runs in the victim's origin, so it can read cookies (absent `HttpOnly`), steal session tokens, and issue authenticated requests as the user.
- Two server-side variants: reflected (payload echoed from the request) and stored/persistent (payload saved and served to later victims).

## Reflected vs Stored

- Reflected XSS delivers via a crafted link or form; the payload appears in the response to that single request and requires the victim to trigger it.
- Stored XSS persists in a database, comment, profile, or log and executes for every user who views the affected page, giving broader reach.
- Both depend on the output sink's context: HTML body, attribute, URL, JavaScript string, or CSS each require different escaping.

## Defensive Use

- Apply context-aware output encoding at the sink (HTML-entity, attribute, JS, URL) rather than a single global filter.
- Validate/allowlist input where feasible, set `HttpOnly` and `Secure` cookie flags, and deploy a restrictive Content Security Policy as defense in depth.
- Use framework auto-escaping templates and avoid unsafe raw-HTML APIs.

## Sources

- OWASP Cross Site Scripting - https://owasp.org/www-community/attacks/xss/
- PortSwigger Web Security Academy - https://portswigger.net/web-security/cross-site-scripting
- OWASP XSS Prevention Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
