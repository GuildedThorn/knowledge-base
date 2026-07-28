---
summary: "IP-layer security suite providing authenticated, encrypted tunnels via ESP/AH with keys negotiated by the IKEv2 exchange."
status: active
tags: [reference, engineering, networking, ipsec, ikev2, tunnel]
private: false
---

# IPsec and IKEv2

## Purpose

The IP-layer security suite providing authenticated, encrypted tunnels via ESP/AH with keys negotiated by the IKEv2 exchange.

## ESP/AH and Security Associations

- A Security Association (SA) is a one-way agreement on algorithms, keys, and parameters, identified by a Security Parameter Index (SPI) and destination.
- Encapsulating Security Payload (ESP) provides confidentiality plus integrity; Authentication Header (AH) provides integrity and origin authentication only, and is rarely used today.
- The Security Policy Database (SPD) decides per packet whether to protect, bypass, or discard; the SA Database (SAD) holds active SA state.
- Anti-replay uses monotonic sequence numbers within each SA to reject duplicated or replayed packets.

## IKEv2 SA Negotiation

- IKEv2 establishes an IKE SA in the initial IKE_SA_INIT exchange (Diffie-Hellman + nonces), then authenticates peers and creates the first Child SA in IKE_AUTH.
- Peers authenticate via pre-shared keys, certificates, or EAP; both directions are confirmed before data flows.
- Additional Child SAs and rekeying use CREATE_CHILD_SA; liveness is checked with INFORMATIONAL exchanges (dead-peer detection).

## Transport vs Tunnel Mode

- Transport mode protects the IP payload but keeps the original IP header, suited to host-to-host traffic.
- Tunnel mode encapsulates the entire original packet inside a new IP header, the basis for site-to-site and remote-access VPN gateways.

## Sources

- RFC 4301 - Security Architecture for the Internet Protocol - https://www.rfc-editor.org/rfc/rfc4301
- RFC 7296 - Internet Key Exchange Protocol Version 2 (IKEv2) - https://www.rfc-editor.org/rfc/rfc7296

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
