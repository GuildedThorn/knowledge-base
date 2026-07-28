---
summary: "WebSockets and SSE keep long-lived application connections open for realtime updates, with different bidirectionality and infrastructure tradeoffs."
status: active
tags: [reference, engineering, networking, realtime]
private: false
---

# WebSockets and Server-Sent Events

## Purpose

WebSockets and SSE keep long-lived application connections open for realtime updates, with different bidirectionality and infrastructure tradeoffs.

## Core Model

- WebSocket upgrades an HTTP request into a bidirectional message channel.
- SSE streams server-to-client events over regular HTTP response semantics.
- Both need heartbeat, reconnect, backpressure, auth refresh, and load-balancer timeout design.

## Engineering Notes

- Use SSE for simple server-to-browser updates and WebSockets for bidirectional low-latency interaction.
- Design reconnection and resume semantics; clients will disconnect.
- Monitor connection count, per-connection memory, send queue depth, and fanout latency.

## Sources

- RFC 6455 - The WebSocket Protocol - https://www.rfc-editor.org/rfc/rfc6455
- WHATWG - Server-sent events - https://html.spec.whatwg.org/multipage/server-sent-events.html
- MDN - WebSocket API - https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
