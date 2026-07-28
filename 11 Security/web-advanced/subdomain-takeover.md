---
summary: "Claiming a dangling DNS record pointing at a deprovisioned cloud service to serve content on a trusted subdomain."
status: active
tags: [security, web, dns, dangling-record, takeover]
private: false
---

# Subdomain Takeover

## Purpose

Claiming a dangling DNS record pointing at a deprovisioned cloud service to serve content on a trusted subdomain.

## How It Works

- A subdomain has a DNS record (usually a CNAME) pointing at a third-party service endpoint that no longer has a resource bound to it.
- The service provider lets anyone register that endpoint name, so an attacker claims it and now controls what the trusted subdomain serves.
- Because the subdomain is still under the victim's registered domain, browsers, users, and TLS trust it, enabling phishing, cookie theft, and CSP/CORS bypass.
- Vulnerable record classes include dangling CNAMEs to cloud storage, PaaS apps, CDNs, and SaaS pages, plus stale NS delegations.

## Security Notes

- Fingerprinting relies on provider-specific "not found" pages (e.g., a bucket-not-found or app-not-found banner) that signal a claimable endpoint.
- The community reference "Can I Take Over XYZ" catalogs providers and whether each is exploitable.
- Cookies scoped to the parent domain, OAuth redirect allowlists, and CSP `*.domain` rules amplify impact once a subdomain is controlled.

## Defensive Use

- Deprovision DNS records at the same time as the underlying resource; never leave a CNAME pointing at a released endpoint.
- Run periodic DNS hygiene scans that resolve every record and flag dangling targets.
- Use catch-all monitoring and inventory so retired services are decommissioned in DNS.
- Prefer claiming/locking service names before releasing them where the provider allows.

## Sources

- MDN Subdomain Takeovers - https://developer.mozilla.org/en-US/docs/Web/Security/Subdomain_takeovers
- Can I Take Over XYZ - https://github.com/EdOverflow/can-i-take-over-xyz

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
