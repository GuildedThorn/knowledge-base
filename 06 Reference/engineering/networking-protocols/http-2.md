---
summary: "A binary framing layer that multiplexes concurrent streams over one TCP connection with header compression, prioritization, and server push."
status: active
tags: [reference, engineering, networking, http2, multiplexing, hpack]
private: false
---

# HTTP/2 Multiplexing

## Purpose

A binary framing layer that multiplexes concurrent streams over one TCP connection with header compression, prioritization, and server push.

## Binary Framing and Streams

- Replaces HTTP/1.1 text with a binary framing layer; messages become sequences of typed frames (HEADERS, DATA, SETTINGS, WINDOW_UPDATE, RST_STREAM).
- A single TCP connection carries many independent, bidirectional streams, each identified by an integer stream ID (odd for client-initiated, even for server).
- Interleaving frames from different streams enables full request/response multiplexing without opening parallel connections.
- Priority was signalled via dependency weights in RFC 7540; RFC 9113 deprecates that scheme in favor of the Extensible Priorities extension.
- Server push (PUSH_PROMISE) lets a server preemptively send resources, though it is widely disabled and effectively deprecated in practice.

## HPACK, Flow Control, and HOL Blocking

- HPACK (RFC 7541) compresses headers with a static table, a per-connection dynamic table, and Huffman coding, reducing redundant header bytes.
- Flow control is credit-based per stream and per connection, managed with WINDOW_UPDATE frames to prevent a fast sender from overwhelming a receiver.
- Application-layer head-of-line blocking within one stream is removed, but TCP-level HOL blocking remains: a lost segment stalls all streams on the connection.
- HTTP/3 over QUIC addresses the residual transport HOL blocking that HTTP/2 cannot solve.

## Sources

- RFC 9113 - HTTP/2 - https://www.rfc-editor.org/rfc/rfc9113
- RFC 7541 - HPACK Header Compression for HTTP/2 - https://www.rfc-editor.org/rfc/rfc7541

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
