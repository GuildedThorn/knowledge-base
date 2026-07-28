---
summary: "Cryptographic signatures over DNS records that let resolvers authenticate origin and integrity via a chain of trust from the root."
status: active
tags: [reference, engineering, networking, dnssec, signing, authentication]
private: false
---

# DNS Security Extensions (DNSSEC)

## Purpose

Cryptographic signatures over DNS records that let resolvers authenticate origin and integrity via a chain of trust from the root.

## Core Model

- DNSKEY records publish a zone's public keys; RRSIG records carry signatures over each resource record set (RRset).
- A DS record in the parent zone holds a hash of the child's key, linking one zone's trust to the next.
- Validation walks the delegation chain from a configured trust anchor (the root zone key) down to the queried name.
- DNSSEC provides origin authentication and integrity only; it does not encrypt queries or hide the answer.

## Authenticated Denial

- NSEC records prove a name or type does not exist by pointing to the next canonical name, which enables zone walking.
- NSEC3 hashes owner names to hinder enumeration and supports opt-out for unsigned delegations.
- Signed negative answers let resolvers cache and trust "no such record" responses rather than accept forged ones.

## Engineering Notes

- Key rollover (ZSK and KSK) must be staged with TTL-aware timing to avoid validation failures.
- Broken chains or expired RRSIGs cause SERVFAIL for validating resolvers, not silent fallback.
- Signing enlarges responses, raising UDP fragmentation and amplification concerns.

## Sources

- RFC 4033 - DNS Security Introduction and Requirements - https://www.rfc-editor.org/rfc/rfc4033
- RFC 4035 - Protocol Modifications for the DNS Security Extensions - https://www.rfc-editor.org/rfc/rfc4035

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
