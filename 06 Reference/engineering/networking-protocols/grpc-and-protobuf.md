---
summary: "gRPC uses HTTP/2 and Protocol Buffers to define strongly typed service contracts, streaming calls, deadlines, metadata, and status codes."
status: active
tags: [reference, engineering, networking, grpc]
private: false
---

# gRPC and Protocol Buffers

## Purpose

gRPC uses HTTP/2 and Protocol Buffers to define strongly typed service contracts, streaming calls, deadlines, metadata, and status codes.

## Core Model

- Protocol Buffers define messages and services with language-specific generated code.
- gRPC supports unary, server-streaming, client-streaming, and bidirectional-streaming calls.
- Deadlines, cancellation, metadata, interceptors, reflection, and health checks are part of production use.

## Engineering Notes

- Version protobuf fields with additive changes; never reuse field numbers.
- Set deadlines on clients and propagate cancellation across service calls.
- Use HTTP/JSON APIs at public edges when browser/proxy compatibility matters, and gRPC for internal typed RPC where it fits.

## Sources

- gRPC documentation - https://grpc.io/docs/
- Protocol Buffers documentation - https://protobuf.dev/
- gRPC health checking - https://grpc.io/docs/guides/health-checking/

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
