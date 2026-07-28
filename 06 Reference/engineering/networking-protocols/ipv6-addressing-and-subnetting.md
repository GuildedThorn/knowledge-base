---
summary: "IPv6 changes addressing scale, neighbor discovery, autoconfiguration, extension headers, and operational assumptions compared with IPv4."
status: active
tags: [reference, engineering, networking, ipv6]
private: false
---

# IPv6 Addressing and Subnetting

## Purpose

IPv6 changes addressing scale, neighbor discovery, autoconfiguration, extension headers, and operational assumptions compared with IPv4.

## Core Model

- IPv6 addresses are 128 bits; /64 subnets are the common LAN unit for SLAAC.
- Neighbor Discovery replaces ARP and depends on ICMPv6.
- Global unicast, unique local, link-local, multicast, and temporary privacy addresses serve different roles.

## Engineering Notes

- Do not block all ICMPv6; path MTU discovery and neighbor discovery require it.
- Document prefix delegation, router advertisements, DNS, firewall rules, and dual-stack behavior.
- Avoid IPv4 habits such as tiny subnets unless there is a clear routing/security reason.

## Sources

- RFC 8200 - IPv6 Specification - https://www.rfc-editor.org/rfc/rfc8200
- RFC 4861 - Neighbor Discovery - https://www.rfc-editor.org/rfc/rfc4861
- RIPE IPv6 address planning - https://www.ripe.net/publications/docs/ripe-690/

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
