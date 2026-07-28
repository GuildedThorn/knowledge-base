---
summary: "CSRF against the WebSocket handshake letting a cross-origin page open an authenticated socket and exfiltrate data."
status: active
tags: [security, web, websocket, cswsh, csrf]
private: false
---

# Cross-Site WebSocket Hijacking

## Purpose

CSRF against the WebSocket handshake letting a cross-origin page open an authenticated socket and exfiltrate data.

## How It Works

- The WebSocket opening handshake is an HTTP request; browsers attach cookies to it, and it is not protected by the same-origin policy for connection establishment.
- If the server authenticates the socket solely via ambient cookies and does not validate the `Origin` header or a CSRF token, any cross-origin page can open an authenticated connection.
- The attacker's page (CSWSH) opens the socket in the victim's session, then reads server-pushed messages and exfiltrates them to the attacker.
- Effectively a CSRF flaw at the handshake combined with the ability to read responses over the persistent channel.

## Defensive Notes

- Validate the `Origin` header on the handshake against an allowlist and reject unexpected origins.
- Require a CSRF token or session-bound value in the handshake, not just cookies.
- Prefer per-connection authentication tokens passed in the first message; keep tokens short-lived.
- Apply `SameSite` cookie attributes so cross-site requests do not carry session cookies.

## Sources

- PortSwigger Web Security Academy - https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking
- MDN WebSockets API - https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
