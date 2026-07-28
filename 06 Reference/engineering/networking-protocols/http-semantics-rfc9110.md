---
summary: "HTTP defines resource-oriented request/response semantics independent of a specific wire version such as HTTP/1.1, HTTP/2, or HTTP/3."
status: active
tags: [reference, engineering, networking, http]
private: false
---

# HTTP Semantics (RFC 9110)

## Purpose

HTTP defines resource-oriented request/response semantics independent of a specific wire version such as HTTP/1.1, HTTP/2, or HTTP/3.

## Core Model

- Methods have semantics: GET is safe, PUT is idempotent, POST is general processing, PATCH is partial modification.
- Status codes communicate response class and action: 2xx success, 3xx redirection, 4xx client error, 5xx server error.
- Headers, content negotiation, caching, conditionals, ranges, and authentication compose protocol behavior.

## Engineering Notes

- Use method semantics honestly; caches, proxies, crawlers, and clients rely on them.
- Return precise status codes and machine-readable error bodies for API clients.
- Design idempotency explicitly for retries across flaky networks.

## Sources

- RFC 9110 - HTTP Semantics - https://www.rfc-editor.org/rfc/rfc9110
- MDN - HTTP - https://developer.mozilla.org/en-US/docs/Web/HTTP
- HTTP Working Group specs - https://httpwg.org/specs/

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
