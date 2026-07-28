---
summary: "Announcing one address from many locations so routing steers each client to a nearby instance for scale and resilience."
status: active
tags: [reference, engineering, networking, anycast, routing, resilience]
private: false
---

# IP Anycast

## Purpose

Announcing the same address from multiple locations so routing steers each client to a topologically nearby instance for scale and resilience.

## Routing-Based Nearest Selection

- The same prefix is originated from multiple physical sites; the routing system (BGP, or an IGP internally) delivers each packet to whichever advertisement is closest by routing metric.
- "Nearest" is topological, not geographic: it reflects AS-path length, IGP cost, and policy, so the chosen node may not be the physically closest one.
- Selection is stateless per packet and requires no client awareness; the client uses a single destination address like any unicast target.

## Operational Stability

- Anycast suits request/response and short-lived flows; long-lived stateful sessions can break if a routing change re-steers packets to a different node mid-flow.
- Withdrawing a failing node's advertisement fails traffic over to the next-nearest instance, giving fast, routing-driven resilience and load distribution.
- Operators must keep the anycast set consistent (same content, health-gated announcements) so any instance can serve any client.

## DNS and CDN Use Cases

- Root and authoritative DNS servers are widely deployed as anycast, spreading query load and absorbing volumetric DDoS across many sites.
- CDNs and public resolvers (e.g. large 8.8.8.8-style services) use anycast to shorten round trips and localize traffic to regional points of presence.
- Because DNS is largely single-packet UDP, it is a natural fit for the stateless, per-packet nature of anycast.

## Sources

- RFC 4786 - Operation of Anycast Services - https://www.rfc-editor.org/rfc/rfc4786
- RFC 1546 - Host Anycasting Service - https://www.rfc-editor.org/rfc/rfc1546

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
