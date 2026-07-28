---
summary: "HTTP caching uses freshness, validators, cache-control directives, and surrogate infrastructure to reduce latency and origin load."
status: active
tags: [reference, engineering, networking, caching]
private: false
---

# HTTP Caching and CDNs

## Purpose

HTTP caching uses freshness, validators, cache-control directives, and surrogate infrastructure to reduce latency and origin load.

## Core Model

- Cache-Control, Expires, ETag, Last-Modified, Vary, and conditional requests define cache behavior.
- Shared caches and browser caches have different trust and privacy implications.
- CDNs add edge routing, shielding, invalidation, compression, TLS termination, and sometimes application security.

## Engineering Notes

- Cache immutable versioned assets aggressively; cache personalized responses only with explicit controls.
- Use ETags/Last-Modified for revalidation and Vary carefully to avoid cache fragmentation.
- Plan purge/invalidation strategy before caching dynamic content.

## Sources

- RFC 9111 - HTTP Caching - https://www.rfc-editor.org/rfc/rfc9111
- MDN - HTTP caching - https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching
- Cloudflare - What is a CDN? - https://www.cloudflare.com/learning/cdn/what-is-a-cdn/

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
