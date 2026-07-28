---
summary: "OSPF is a link-state interior routing protocol that floods topology information so routers can compute shortest paths."
status: active
tags: [reference, engineering, networking, ospf]
private: false
---

# OSPF and Interior Routing

## Purpose

OSPF is a link-state interior routing protocol that floods topology information so routers can compute shortest paths.

## Core Model

- Routers form adjacencies, exchange link-state advertisements, and run SPF over a shared topology database.
- Areas reduce flooding and computation scope, with area 0 as the backbone.
- Cost normally represents interface path preference and should match bandwidth/operations policy.

## Engineering Notes

- Use dynamic routing when redundant paths and automatic convergence matter.
- Keep area design simple until scale forces hierarchy.
- Monitor neighbor state, LSA churn, route flaps, and asymmetric path surprises.

## Sources

- RFC 2328 - OSPF Version 2 - https://www.rfc-editor.org/rfc/rfc2328
- FRRouting OSPF docs - https://docs.frrouting.org/en/latest/ospfd.html
- Cisco OSPF design guide - https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/7039-1.html

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
