---
summary: "Internet protocols, HTTP, TLS, QUIC, DNS, routing, load balancing, gRPC, and service connectivity notes."
status: active
tags: [reference, engineering, networking, protocols, index]
private: false
---

# Networking and Protocols - Index

## Purpose

Internet protocols, HTTP, TLS, QUIC, DNS, routing, load balancing, gRPC, and service connectivity notes.

## Notes

- [BGP Routing and RPKI](kb://06-reference-engineering-networking-protocols-bgp-routing-and-rpki) - BGP exchanges reachability between autonomous systems, while RPKI lets networks validate whether an AS is authorized to originate a prefix.
- [DNS Resolution and Operations](kb://06-reference-engineering-networking-protocols-dns-resolution-and-operations) - DNS translates names into records through recursive and authoritative systems with caching, delegation, TTLs, and security extensions.
- [gRPC and Protocol Buffers](kb://06-reference-engineering-networking-protocols-grpc-and-protobuf) - gRPC uses HTTP/2 and Protocol Buffers to define strongly typed service contracts, streaming calls, deadlines, metadata, and status codes.
- [HTTP Caching and CDNs](kb://06-reference-engineering-networking-protocols-http-caching-and-cdns) - HTTP caching uses freshness, validators, cache-control directives, and surrogate infrastructure to reduce latency and origin load.
- [HTTP Semantics (RFC 9110)](kb://06-reference-engineering-networking-protocols-http-semantics-rfc9110) - HTTP defines resource-oriented request/response semantics independent of a specific wire version such as HTTP/1.1, HTTP/2, or HTTP/3.
- [IPv6 Addressing and Subnetting](kb://06-reference-engineering-networking-protocols-ipv6-addressing-and-subnetting) - IPv6 changes addressing scale, neighbor discovery, autoconfiguration, extension headers, and operational assumptions compared with IPv4.
- [Load Balancing and Reverse Proxies](kb://06-reference-engineering-networking-protocols-load-balancing-and-reverse-proxies) - Load balancers and reverse proxies route traffic, terminate TLS, enforce policy, perform health checks, and shape failure behavior.
- [OSPF and Interior Routing](kb://06-reference-engineering-networking-protocols-ospf-and-interior-routing) - OSPF is a link-state interior routing protocol that floods topology information so routers can compute shortest paths.
- [QUIC and HTTP/3](kb://06-reference-engineering-networking-protocols-quic-and-http3) - QUIC runs over UDP to provide encrypted multiplexed streams, connection migration, and lower handshake latency for HTTP/3 and other protocols.
- [TCP/IP Stack Model](kb://06-reference-engineering-networking-protocols-tcp-ip-stack-model) - The TCP/IP stack composes link, internet, transport, and application layers, each with separate addressing and failure behavior.
- [TLS 1.3](kb://06-reference-engineering-networking-protocols-tls-13) - TLS 1.3 secures transport sessions with simplified handshakes, modern cipher suites, forward secrecy, and reduced legacy surface.
- [WebSockets and Server-Sent Events](kb://06-reference-engineering-networking-protocols-websockets-and-server-sent-events) - WebSockets and SSE keep long-lived application connections open for realtime updates, with different bidirectionality and infrastructure tradeoffs.

## Related

- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Engineering Source Corpus](kb://06-reference-engineering-engineering-source-corpus)
- [Reference Map](kb://01-maps-reference-map)
