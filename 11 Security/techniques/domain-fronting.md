---
summary: "Hiding C2 destination by presenting an innocuous SNI/host while routing to a hidden origin via a shared CDN."
status: active
tags: [security, techniques, c2, cdn, evasion]
private: false
---

# Domain Fronting

## Purpose

Hiding C2 destination by presenting an innocuous SNI/host while routing to a hidden origin via a shared CDN.

## How It Works

- The TLS ClientHello SNI and the certificate name reference an innocuous, high-reputation domain hosted on a shared CDN.
- Inside the encrypted HTTP request, the `Host` header names the attacker's hidden origin served by the same CDN edge.
- The CDN terminates TLS, reads the encrypted `Host` header, and routes to the real backend, so network observers only see the benign front.
- This works because the routing layer trusts the inner `Host` header over the outer SNI on shared infrastructure.

## Engineering Notes

- Historically abused Google, Amazon CloudFront, and Azure fronts; maps to MITRE ATT&CK T1090.004 (Domainless/Domain Fronting).
- Major CDNs deployed SNI/Host-match enforcement (2018) that broke classic fronting on their platforms.
- Encrypted Client Hello (ECH), successor to ESNI, encrypts the SNI itself, reviving front-like concealment where deployed.

## Defensive Use

- Inspect for SNI-to-Host mismatch at TLS-terminating proxies that can see the decrypted `Host` header.
- Apply CDN provider controls that reject requests whose inner host differs from the fronted SNI domain.
- Monitor for unexpected traffic volume to CDN domains and enforce egress allow-lists with decryption where policy permits.

## Sources

- MITRE ATT&CK T1090.004 - https://attack.mitre.org/techniques/T1090/004/
- Blocking-resistant Communication through Domain Fronting - https://www.bamsoftware.com/papers/fronting/

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
