---
summary: "DNS translates names into records through recursive and authoritative systems with caching, delegation, TTLs, and security extensions."
status: active
tags: [reference, engineering, networking, dns]
private: false
---

# DNS Resolution and Operations

## Purpose

DNS translates names into records through recursive and authoritative systems with caching, delegation, TTLs, and security extensions.

## Core Model

- Stub resolvers ask recursive resolvers, which chase delegations from root to TLD to authoritative servers.
- Records include A/AAAA, CNAME, MX, NS, TXT, SRV, CAA, SOA, and DNSSEC material.
- TTL controls cache lifetime, but negative caching and resolver behavior also affect propagation.

## Engineering Notes

- Lower TTLs before planned migrations; do not expect instant propagation after changing records.
- Use CAA, DNSSEC where appropriate, and monitor authoritative health from multiple networks.
- Treat split-horizon DNS and search domains as operational state that can break debugging.

## Sources

- RFC 1034 - Domain names concepts - https://www.rfc-editor.org/rfc/rfc1034
- RFC 1035 - Domain names implementation - https://www.rfc-editor.org/rfc/rfc1035
- Cloudflare - Learning DNS - https://www.cloudflare.com/learning/dns/what-is-dns/

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
