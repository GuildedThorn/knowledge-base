---
summary: "Forwarding architecture that switches packets by short labels along label-switched paths, enabling traffic engineering and VPNs."
status: active
tags: [reference, engineering, networking, mpls, labels, forwarding]
private: false
---

# Multiprotocol Label Switching (MPLS)

## Purpose

A forwarding architecture that switches packets by short labels along label-switched paths, enabling traffic engineering and VPNs.

## Labels and FEC Binding

- Ingress routers classify packets into a Forwarding Equivalence Class (FEC) once, then attach a fixed-length label; downstream routers forward on the label alone, not a full IP lookup.
- A label has only local significance on a link; each Label Switching Router (LSR) swaps the incoming label for the next-hop's outgoing label.
- Label bindings are distributed by LDP, RSVP-TE, or BGP, mapping FECs to labels across the network.
- Penultimate-hop popping lets the second-to-last LSR remove the label so the egress does a single native lookup.

## LSPs, Stacking, and Traffic Engineering

- A Label Switched Path (LSP) is a unidirectional sequence of LSRs a labeled packet follows from ingress to egress.
- Labels form a stack (LIFO); operations act on the top entry, enabling nested services such as VPN-over-transport tunnels.
- RSVP-TE can pin LSPs onto explicit paths with reserved bandwidth, decoupling forwarding from shortest-path IGP metrics.
- MPLS L3VPNs use a two-label stack: an outer transport label reaches the egress PE, an inner VPN label selects the customer VRF.

## Sources

- RFC 3031 - Multiprotocol Label Switching Architecture - https://www.rfc-editor.org/rfc/rfc3031
- RFC 3032 - MPLS Label Stack Encoding - https://www.rfc-editor.org/rfc/rfc3032

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
