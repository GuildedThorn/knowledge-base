---
summary: "Tricking a cache into storing a victim's private authenticated response under a static-looking URL path."
status: active
tags: [security, web, cache, deception, path-confusion]
private: false
---

# Web Cache Deception

## Purpose

Tricking a cache into storing a victim's private authenticated response under a static-looking URL path.

## How It Works

- The attacker crafts a URL that appends a static-looking suffix (e.g. `/account/settings/foo.css`) to a dynamic, authenticated endpoint.
- The application ignores the extra path segment and returns the victim's private page; the cache, keyed on the `.css` extension, treats it as a cacheable static asset.
- When the victim visits the crafted link, their sensitive response is stored in the shared cache; the attacker then retrieves it unauthenticated.
- Unlike cache poisoning, the goal is disclosure of another user's response, not injection of malicious content.

## Path Confusion

- Root cause is a mismatch between how the origin routes/normalizes the path and how the cache decides cacheability from the path or extension.
- Delimiter differences (`;`, `%2F`, `%00`, `#`, `?`) and lenient path handling widen the set of URLs that map to the same sensitive resource.
- Static-extension rules (`.css`, `.js`, `.jpg`) and directory-prefix caching rules are the usual trigger for an unintended cache write.

## Defenses

- Cache only responses whose `Content-Type` matches the requested extension, and honor origin `Cache-Control`/`Vary` instead of extension heuristics.
- Normalize and validate paths consistently between the cache and origin; reject unexpected suffixes on dynamic endpoints.
- Never cache authenticated or personalized responses; set `Cache-Control: no-store` on them.

## Sources

- PortSwigger Web Security Academy - https://portswigger.net/web-security/web-cache-deception
- Web Cache Deception Attack (Omer Gil) - https://omergil.blogspot.com/2017/02/web-cache-deception-attack.html

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
