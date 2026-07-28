---
summary: "OpenAPI describes HTTP APIs in a machine-readable contract for documentation, clients, servers, validation, and governance."
status: active
tags: [reference, engineering, architecture, openapi]
private: false
---

# OpenAPI Contracts

## Purpose

OpenAPI describes HTTP APIs in a machine-readable contract for documentation, clients, servers, validation, and governance.

## Core Model

- OpenAPI documents paths, operations, parameters, request/response bodies, schemas, security, examples, and metadata.
- JSON Schema vocabularies describe payload structure and validation semantics.
- Generated clients and servers are only as good as contract precision and compatibility discipline.

## Engineering Notes

- Treat OpenAPI as source-controlled interface, not a generated afterthought.
- Use examples and error schemas; clients need failure contracts too.
- Check breaking changes in CI with schema diff tooling.

## Sources

- OpenAPI Specification - https://spec.openapis.org/oas/latest.html
- JSON Schema specification - https://json-schema.org/specification
- Swagger documentation - https://swagger.io/docs/specification/

## Related

- [Software Architecture - Index](kb://06-reference-engineering-software-architecture-software-architecture-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
