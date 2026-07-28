---
summary: "BGP exchanges reachability between autonomous systems, while RPKI lets networks validate whether an AS is authorized to originate a prefix."
status: active
tags: [reference, engineering, networking, bgp]
private: false
---

# BGP Routing and RPKI

## Purpose

BGP exchanges reachability between autonomous systems, while RPKI lets networks validate whether an AS is authorized to originate a prefix.

## Core Model

- BGP is path-vector routing; policy and AS-path selection decide internet reachability.
- Route leaks and hijacks can spread globally when invalid or unexpected routes are accepted.
- RPKI ROAs support route-origin validation but do not solve every route-leak class.

## Engineering Notes

- Multihomed networks need route policy, prefix filters, max-prefix limits, monitoring, and rollback plans.
- Publish ROAs for owned prefixes and monitor invalid/unknown route origin state.
- Treat BGP changes as production deployments with peer/provider coordination.

## Sources

- RFC 4271 - BGP-4 - https://www.rfc-editor.org/rfc/rfc4271
- NIST RPKI Monitor - https://rpki-monitor.antd.nist.gov/
- MANRS routing security - https://www.manrs.org/

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
