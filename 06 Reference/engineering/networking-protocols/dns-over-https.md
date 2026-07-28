---
summary: "Encapsulating DNS queries inside HTTPS to encrypt resolution traffic and resist on-path tampering and surveillance."
status: active
tags: [reference, engineering, networking, doh, privacy, encryption]
private: false
---

# DNS over HTTPS (DoH)

## Purpose

Encapsulating DNS queries inside HTTPS to encrypt resolution traffic and resist on-path tampering and surveillance.

## How It Works

- Clients send standard wire-format DNS messages (application/dns-message) to a DoH endpoint over an HTTPS connection.
- GET requests carry the base64url-encoded query in the `dns` query parameter, making them cacheable by HTTP infrastructure.
- POST requests place the raw DNS message in the request body, which is smaller but generally not cached by intermediaries.
- The HTTP response's Cache-Control max-age interacts with DNS TTLs, and servers are expected to bound it by the smallest record TTL.

## Tradeoffs

- DoH blends DNS into ordinary HTTPS traffic on port 443, making it hard to distinguish or selectively block versus DoT on port 853.
- DoT (RFC 7858) is easier for network operators to observe and manage but is also easier to block outright.
- Centralizing resolution on a few large DoH providers shifts visibility and trust away from the local network operator.
- DoH secures the client-to-resolver hop only; upstream resolver-to-authoritative traffic and query privacy at the resolver remain separate concerns.

## Sources

- RFC 8484 - DNS Queries over HTTPS (DoH) - https://www.rfc-editor.org/rfc/rfc8484

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
