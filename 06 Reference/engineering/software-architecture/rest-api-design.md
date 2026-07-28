---
summary: "REST-style APIs model resources, representations, links, methods, status codes, caching, and stateless interactions over HTTP."
status: active
tags: [reference, engineering, architecture, api]
private: false
---

# REST API Design

## Purpose

REST-style APIs model resources, representations, links, methods, status codes, caching, and stateless interactions over HTTP.

## Core Model

- REST is an architectural style, not just JSON over HTTP.
- Resource identifiers, method semantics, media types, status codes, and hypermedia constraints define the interface.
- Most practical web APIs are REST-ish and should at least use HTTP semantics correctly.

## Engineering Notes

- Use nouns/resources for stable concepts and let methods express actions where possible.
- Version compatibility through additive fields and clear deprecation policy before URL version churn.
- Design errors, pagination, filtering, sorting, auth, idempotency, and rate limits as first-class contract features.

## Sources

- Fielding dissertation - REST - https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
- RFC 9110 - HTTP Semantics - https://www.rfc-editor.org/rfc/rfc9110
- Microsoft REST API Guidelines - https://github.com/microsoft/api-guidelines

## Related

- [Software Architecture - Index](kb://06-reference-engineering-software-architecture-software-architecture-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
