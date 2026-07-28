---
summary: "A MAC-in-UDP encapsulation that stretches Layer 2 segments across Layer 3 fabrics using a 24-bit VNI for tenant isolation."
status: active
tags: [reference, engineering, networking, vxlan, overlay, encapsulation]
private: false
---

# VXLAN Overlay Networking

## Purpose

A MAC-in-UDP encapsulation that stretches Layer 2 segments across Layer 3 fabrics using a 24-bit VNI for tenant isolation.

## Frame Format

- The original Ethernet frame is wrapped in a VXLAN header, then UDP, IP, and outer Ethernet headers (MAC-in-UDP).
- VXLAN uses UDP destination port 4789; the source port is typically a hash of inner headers to aid ECMP load spreading.
- The 24-bit VXLAN Network Identifier (VNI) allows about 16 million segments, far beyond the 4094 usable 802.1Q VLANs.
- Encapsulation adds roughly 50 bytes of overhead, so underlay MTU must be raised or inner MTU reduced to avoid fragmentation.

## VTEPs and BUM Traffic

- VXLAN Tunnel Endpoints (VTEPs) perform encapsulation and decapsulation, mapping local MACs to remote VTEP IPs.
- Broadcast, unknown-unicast, and multicast (BUM) traffic must be delivered to all VTEPs in a VNI.
- The original RFC uses IP multicast groups per VNI with flood-and-learn to populate MAC-to-VTEP mappings.
- Modern deployments often replace flood-and-learn with an EVPN/BGP control plane for MAC and IP advertisement.

## Sources

- RFC 7348 - Virtual eXtensible Local Area Network (VXLAN) - https://www.rfc-editor.org/rfc/rfc7348

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
