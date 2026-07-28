---
summary: "HTTP mapped onto QUIC streams, eliminating TCP head-of-line blocking and using QPACK for order-independent header compression."
status: active
tags: [reference, engineering, networking, http3, quic, qpack]
private: false
---

# HTTP/3 over QUIC

## Purpose

HTTP mapped onto QUIC streams, eliminating TCP head-of-line blocking and using QPACK for order-independent header compression.

## Stream Mapping over QUIC

- HTTP/3 runs over QUIC, a transport built on UDP that provides encrypted, multiplexed streams with integrated TLS 1.3.
- Each HTTP request/response pair uses one bidirectional QUIC stream; independent streams mean a lost packet stalls only its own stream, not the whole connection.
- This removes the TCP-level head-of-line blocking that constrained HTTP/2 while retaining request multiplexing.
- Unidirectional streams carry control data, QPACK encoder/decoder streams, and server push; frame types (HEADERS, DATA, SETTINGS) mirror HTTP/2 semantics.

## QPACK Compression

- QPACK (RFC 9204) is the header-compression scheme for HTTP/3, adapting HPACK concepts to QUIC's out-of-order stream delivery.
- It uses static and dynamic reference tables but avoids head-of-line blocking by managing dynamic-table references through dedicated encoder/decoder streams.
- Encoders can trade off compression efficiency against the risk of blocking on unacknowledged dynamic-table insertions.

## Connection Setup and Discovery

- QUIC combines transport and cryptographic handshakes, enabling 1-RTT setup and 0-RTT resumption for repeat connections.
- Clients typically reach HTTP/3 via HTTP/1.1 or HTTP/2 first, then discover it through the Alt-Svc header (h3) advertising a QUIC endpoint.
- Connection migration is supported through connection IDs, so a session survives an IP or port change (e.g., Wi-Fi to cellular).

## Sources

- RFC 9114 - HTTP/3 - https://www.rfc-editor.org/rfc/rfc9114
- RFC 9204 - QPACK Field Compression for HTTP/3 - https://www.rfc-editor.org/rfc/rfc9204

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
