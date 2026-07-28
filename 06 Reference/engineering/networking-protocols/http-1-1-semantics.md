---
summary: "The request/response model, methods, status codes, and persistent-connection message framing that define classic HTTP over TCP."
status: active
tags: [reference, engineering, networking, http, messaging, keepalive]
private: false
---

# HTTP/1.1 Semantics and Message Syntax

## Purpose

The request/response model, methods, status codes, and persistent-connection message framing that define classic HTTP over TCP.

## Methods and Status Codes

- HTTP is a stateless request/response protocol: a client sends a method, target, and headers; the server returns a status line, headers, and optional body.
- Methods carry defined properties: GET/HEAD are safe (read-only), and GET, HEAD, PUT, DELETE are idempotent, while POST is neither.
- Status codes group by class: 1xx informational, 2xx success, 3xx redirection, 4xx client error, 5xx server error (e.g. 200, 301, 404, 500).

## Header Semantics and Caching

- Headers convey metadata such as Content-Type, Content-Length, Host (mandatory in HTTP/1.1), and conditional/caching fields.
- Caching is driven by Cache-Control, ETag with If-None-Match, and Last-Modified with If-Modified-Since, enabling 304 Not Modified revalidation.
- Content negotiation (Accept, Accept-Encoding, Accept-Language) lets a server select an appropriate representation.

## Persistent Connections and Framing

- HTTP/1.1 keeps connections alive by default, reusing one TCP connection for multiple request/response exchanges to amortize handshake cost.
- Message bodies are framed either by an explicit Content-Length or by chunked transfer-encoding, which streams size-prefixed chunks terminated by a zero-length chunk.
- Requests are still answered in order on a connection, so an early slow response causes head-of-line blocking, a limitation later addressed by HTTP/2 and HTTP/3.

## Sources

- RFC 9110 - HTTP Semantics - https://www.rfc-editor.org/rfc/rfc9110
- RFC 9112 - HTTP/1.1 - https://www.rfc-editor.org/rfc/rfc9112

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
