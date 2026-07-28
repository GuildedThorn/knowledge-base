---
summary: "Hosts lease IP addresses and network configuration from servers through the DISCOVER/OFFER/REQUEST/ACK exchange."
status: active
tags: [reference, engineering, networking, dhcp, addressing, lease]
private: false
---

# Dynamic Host Configuration Protocol (DHCP)

## Purpose

The protocol by which hosts lease IP addresses and network configuration from servers through the DISCOVER/OFFER/REQUEST/ACK exchange.

## DORA Exchange

- The client broadcasts DHCPDISCOVER to find any available server on the segment.
- One or more servers reply with DHCPOFFER proposing an address and parameters.
- The client broadcasts DHCPREQUEST naming the chosen server, so unselected offers are released.
- The selected server confirms with DHCPACK, binding the address; DHCPNAK signals the request cannot be honored.

## Lease Lifecycle

- Each binding carries a lease time plus T1 (renewal, ~50%) and T2 (rebinding, ~87.5%) timers.
- At T1 the client unicasts a renewal to its server; at T2 it broadcasts to any server if renewal failed.
- DHCPRELEASE returns an address early; expiry without renewal frees it back to the pool.

## Options and Relay

- Options (RFC 2132) carry subnet mask, default gateway, DNS servers, domain name, NTP, and vendor extensions in a TLV format.
- Relay agents (giaddr) forward broadcasts to servers on other subnets so one server can serve many segments.
- Option 82 lets relays tag requests with circuit/port information for policy and tracking.

## Sources

- RFC 2131 - Dynamic Host Configuration Protocol - https://www.rfc-editor.org/rfc/rfc2131
- RFC 2132 - DHCP Options and BOOTP Vendor Extensions - https://www.rfc-editor.org/rfc/rfc2132

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
