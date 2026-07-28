---
summary: "The TCP/IP stack composes link, internet, transport, and application layers, each with separate addressing and failure behavior."
status: active
tags: [reference, engineering, networking, tcp-ip]
private: false
---

# TCP/IP Stack Model

## Purpose

The TCP/IP stack composes link, internet, transport, and application layers, each with separate addressing and failure behavior.

## Core Model

- Ethernet/Wi-Fi move frames on a local link; IP routes packets between networks.
- TCP provides reliable ordered byte streams; UDP provides datagrams without built-in reliability.
- Application protocols define semantics above transport: HTTP, DNS, SSH, TLS, gRPC, and more.

## Engineering Notes

- Debug from bottom up: link, IP route, transport connection, TLS/session, then application semantics.
- Use packet captures to verify assumptions about retransmits, fragmentation, MTU, DNS, TLS, and proxy behavior.
- Document which layer owns each timeout, retry, and error message.

## Sources

- RFC 1122 - Internet host requirements - https://www.rfc-editor.org/rfc/rfc1122
- TCP RFC 9293 - https://www.rfc-editor.org/rfc/rfc9293
- Beej's Guide to Network Programming - https://beej.us/guide/bgnet/

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
