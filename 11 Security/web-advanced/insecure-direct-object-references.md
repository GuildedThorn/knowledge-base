---
summary: "Broken object-level authorization where users access others' records by tampering with identifiers."
status: active
tags: [security, web, idor, bola, access-control]
private: false
---

# Insecure Direct Object References

## Purpose

Broken object-level authorization where users access others' records by tampering with identifiers.

## Core Model

- An endpoint exposes a direct reference to an internal object (`/account?id=123`, `/orders/456`) and trusts the client-supplied identifier.
- The server authenticates the user but fails to verify that the authenticated user is authorized for the specific object requested.
- Horizontal access: reaching peer records at the same privilege level (another user's invoice).
- Vertical access: reaching higher-privileged objects or actions (admin-only records).
- In API terms this is Broken Object Level Authorization (BOLA), the top item in the OWASP API Security Top 10.

## Key Ideas

- Predictable or enumerable identifiers (sequential integers) make discovery trivial; UUIDs raise the bar but are not an authorization control.
- Sinks appear in query params, path segments, request bodies, headers, and JSON fields.
- Mass enumeration of IDs often surfaces the flaw across a whole object collection.

## Defensive Use

- Enforce authorization on every request by checking ownership/role against the requested object server-side, never by hiding the ID.
- Scope queries to the current principal (e.g., `WHERE owner_id = :session_user`) rather than fetching then checking.
- Centralize access-control decisions so each new endpoint inherits enforcement.
- Treat unpredictable identifiers as defense-in-depth, not a substitute for authorization.

## Sources

- PortSwigger IDOR - https://portswigger.net/web-security/access-control/idor
- OWASP API Security Top 10 - Broken Object Level Authorization - https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
