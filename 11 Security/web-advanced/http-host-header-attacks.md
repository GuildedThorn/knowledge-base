---
summary: "Abusing the Host and forwarding headers to poison links, bypass auth, or reach virtual-host routing flaws."
status: active
tags: [security, web, host-header, virtual-host]
private: false
---

# HTTP Host Header Attacks

## Purpose

Abusing the Host and forwarding headers to poison links, bypass auth, or reach virtual-host routing flaws.

## Core Model

- The `Host` header (and forwarding headers like `X-Forwarded-Host`) is attacker-controllable but often trusted as if it were server configuration.
- Applications that build absolute URLs from the Host header can be steered to attacker domains without changing the target site.
- Virtual-host routing and reverse proxies use the Host header to select a back-end, so a spoofed value can cross trust or routing boundaries.

## Impact Vectors

- Password-reset poisoning: a reset link built from the Host header points the token at an attacker domain, leaking it when the victim clicks.
- Web cache poisoning: a Host-derived value reflected into cached responses redirects or defaces content for many users.
- Auth and access bypass: internal-only or admin virtual hosts reached by forging the Host header past a front-end that keys access on it.
- Routing-based SSRF where the proxy forwards to a back-end named in the header.

## Defenses

- Do not derive URLs from the incoming Host header; use a server-configured canonical domain (allowlist of trusted hosts).
- Reject or normalize requests whose Host does not match an expected value; validate forwarding headers only from trusted proxies.
- Configure a default/catch-all virtual host that refuses unknown hosts rather than routing them to a real application.

## Sources

- PortSwigger Web Security Academy - https://portswigger.net/web-security/host-header
- Practical HTTP Host Header Attacks (James Kettle) - https://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
