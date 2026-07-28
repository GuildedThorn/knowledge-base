---
summary: "Coercing a server into making attacker-directed requests to internal services, cloud metadata, or arbitrary hosts."
status: active
tags: [security, web, ssrf, internal-network]
private: false
---

# Server-Side Request Forgery

## Purpose

Coercing a server into making attacker-directed requests to internal services, cloud metadata, or arbitrary hosts.

## How It Works

- An app fetches a URL supplied or influenced by the user (webhooks, URL previews, PDF/image fetchers, import-from-URL) without restricting the destination.
- The request originates from the server, so it can reach internal-only hosts, `localhost` services, and cloud metadata endpoints unreachable from the internet.
- Basic SSRF returns the response to the attacker; blind SSRF gives no response body, detected via out-of-band interactions (DNS/HTTP callbacks).
- High-value targets include cloud instance metadata (e.g., `169.254.169.254`) for credential theft, internal admin panels, and container orchestration APIs.

## Bypasses

- Alternate IP encodings: decimal, octal, hex, and IPv6-mapped addresses for `127.0.0.1` / link-local ranges.
- DNS rebinding: a hostname that resolves to an allowed IP at validation time and an internal IP at fetch time.
- Redirect chains where an allowlisted URL 3xx-redirects to an internal target.
- Non-HTTP schemes (`file://`, `gopher://`, `dict://`) to reach the filesystem or raw TCP services.

## Defensive Use

- Enforce a strict allowlist of destination hosts/schemes and resolve-then-validate the final IP, rejecting private, loopback, and link-local ranges.
- Disable unneeded URL schemes and follow-redirect behavior, or re-validate each hop.
- Segment the network so app servers cannot reach internal management or metadata endpoints; require IMDSv2-style token auth.
- Return no raw fetch responses to the client and monitor for out-of-band callbacks.

## Sources

- PortSwigger Web Security Academy - https://portswigger.net/web-security/ssrf
- OWASP SSRF Prevention Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
