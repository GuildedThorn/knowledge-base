---
summary: SSRF coerces a server into making attacker-controlled requests to internal services, loopback, or cloud metadata (169.254.169.254), abusing network trust to reach unroutable systems and steal IAM credentials.
status: active
tags: [security, web, ssrf, appsec]
private: false
---

# Server-Side Request Forgery (SSRF)

SSRF is a web vulnerability where an attacker induces the server-side application to issue HTTP (or other-protocol) requests to an unintended destination, abusing the trust the server has in its own network. It ranges from full-response ("basic") to fire-and-forget ("blind").

## The vulnerability
Any feature that fetches a user-supplied URL — webhooks, PDF/image renderers, link previews, XML/SVG parsers, import-by-URL — is a candidate. The server acts as a confused deputy, reaching localhost admin panels, RFC1918 back-end hosts, and cloud metadata endpoints that are unreachable from the internet. Impacts: internal port scanning, reading local files, credential theft, and pivoting to RCE.

## Exploitation techniques
- **Loopback / internal**: `http://127.0.0.1/admin`, `http://localhost`, private ranges `http://192.168.0.68`.
- **Cloud metadata**: `http://169.254.169.254/latest/meta-data/iam/security-credentials/` yields temporary IAM keys under IMDSv1.
- **Blacklist bypass**: alternate IP encodings — decimal `2130706433`, octal `017700000001`, short form `127.1`, `[::]`, or a custom domain resolving to `127.0.0.1`; URL-encoding and redirect chains.
- **Whitelist bypass**: credentials trick `https://expected-host@evil-host`, fragment `https://evil-host#expected-host`, subdomain `https://expected-host.evil-host`.
- **Parser confusion**: inconsistency between a URL's validator and its requester (Orange Tsai, "A New Era of SSRF"); `@` and userinfo tricks reroute reverse proxies (Kettle: `Host: incapsula-client.net:80@collaborator.net`).
- **Alternate schemes**: `gopher://`, `dict://`, `file://` for protocol smuggling.
- **Header/blind vectors**: malformed `Host`, absolute-URI request line, `X-Forwarded-For`, `Referer`; detect blind cases via out-of-band pingbacks (Burp Collaborator).

## Real-world cases (sourced)
- **Capital One (March 2019)**: SSRF in a ModSecurity WAF relayed requests to EC2 IMDS, retrieving the WAF role's credentials; combined with over-privileged IAM it exposed ~100M+ credit applications (~30GB) from private S3 buckets. Drove AWS's IMDSv2.
- **James Kettle, "Cracking the Lens" (Black Hat 2017)**: Host-header and proxy misrouting perforated DoD/ISP networks, ~$33k in bounties.

## Detection & prevention
Allowlist destination hosts/schemes (HTTP/HTTPS only) with strict string comparison; never pass raw user URLs to fetchers. Resolve the hostname and reject private/loopback/link-local/multicast IPs, guarding DNS-rebinding/TOCTOU by pinning the resolved IP. Disable HTTP redirect following; don't return raw upstream responses. Network-layer: egress firewalls and segmentation. Cloud: enforce IMDSv2 (PUT session token + header, hop limit) and least-privilege roles.

## Sources
- What is SSRF? — https://portswigger.net/web-security/ssrf
- OWASP SSRF Prevention Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html
- Cracking the Lens (James Kettle, PortSwigger Research) — https://portswigger.net/research/cracking-the-lens-targeting-https-hidden-attack-surface
- Capital One incident, March 2019 (Wiz Cloud Threat Landscape) — https://threats.wiz.io/all-incidents/capital-one-incident-march-2019

## Related
- [Web-Advanced — Index](kb://11-security-web-advanced-web-advanced-index)
- [Web App Testing](kb://11-security-playbook-web-app-testing)
- [Payload Cheat Sheets — Index](kb://11-security-payloads-payloads-index)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
