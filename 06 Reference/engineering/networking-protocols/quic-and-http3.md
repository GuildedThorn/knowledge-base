---
summary: "QUIC runs over UDP to provide encrypted multiplexed streams, connection migration, and lower handshake latency for HTTP/3 and other protocols."
status: active
tags: [reference, engineering, networking, quic]
private: false
---

# QUIC and HTTP/3

## Purpose

QUIC runs over UDP to provide encrypted multiplexed streams, connection migration, and lower handshake latency for HTTP/3 and other protocols.

## Core Model

- QUIC integrates TLS 1.3 and transport features instead of layering TLS over TCP.
- Streams avoid TCP head-of-line blocking between independent HTTP requests.
- Connection IDs support migration across network changes without losing the logical connection.

## Engineering Notes

- Ensure UDP paths, firewalls, load balancers, and observability support QUIC before enabling broadly.
- Keep HTTP/2 fallback; some networks still block or degrade UDP.
- Measure tail latency and error rates by protocol version, not only aggregate request latency.

## Sources

- RFC 9000 - QUIC - https://www.rfc-editor.org/rfc/rfc9000
- RFC 9114 - HTTP/3 - https://www.rfc-editor.org/rfc/rfc9114
- Cloudflare - HTTP/3 from root to tip - https://blog.cloudflare.com/http3-the-past-present-and-future/

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
