---
summary: "An OSI-derived link-state IGP that routes IP and CLNS over a two-level area hierarchy using TLV-encoded link-state PDUs."
status: active
tags: [reference, engineering, networking, isis, linkstate, igp]
private: false
---

# IS-IS Routing Protocol

## Purpose

An OSI-derived link-state IGP that routes IP and CLNS over a two-level area hierarchy using TLV-encoded link-state PDUs.

## Core Model

- Intermediate System to Intermediate System runs directly over the data link layer, not inside IP, using CLNS addressing (NET/NSAP).
- Routers flood Link-State PDUs (LSPs) so each builds an identical link-state database and runs SPF for shortest paths.
- Information is carried in TLVs, which let the protocol extend to new address families without a new packet format.
- RFC 1195 (Integrated IS-IS) added the TLVs needed to carry IPv4 reachability alongside OSI CLNS in dual environments.

## Hierarchy and Adjacencies

- Level 1 routers know only their own area; Level 2 routers form the inter-area backbone, and L1/L2 routers bridge the two.
- L1 routers reach outside their area via the nearest attached L1/L2 router, keeping intra-area databases small.
- Adjacencies form after IIH Hello exchange; on LAN segments a Designated Intermediate System (DIS) generates a pseudonode LSP.

## Engineering Notes

- The TLV design made IS-IS straightforward to extend for IPv6, making it common in large ISP and data-center cores.
- Area boundaries fall on links between routers, unlike OSPF where they fall on interfaces within a router.
- Tune LSP lifetimes, SPF timers, and DIS priority to balance convergence against stability.

## Sources

- RFC 1195 - Use of OSI IS-IS for Routing in TCP/IP and Dual Environments - https://www.rfc-editor.org/rfc/rfc1195

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
