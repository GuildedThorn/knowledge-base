---
summary: "Auto-binding request parameters to internal object fields, letting attackers set privileged or hidden attributes."
status: active
tags: [security, web, mass-assignment, auto-binding]
private: false
---

# Mass Assignment

## Purpose

Auto-binding request parameters to internal object fields, letting attackers set privileged or hidden attributes.

## How It Works

- Frameworks that auto-bind request bodies to model objects copy every supplied field onto the object, including ones the developer never intended to expose.
- An attacker adds extra fields to a request (`{"email":"x","isAdmin":true}`) and the framework writes them straight to the model or ORM.
- Also called auto-binding, object injection, or (in Rails) allow-listing gaps; PHP/Node/Java/.NET ORMs all have equivalent binders.
- Common targets: `role`, `isAdmin`, `verified`, `balance`, `userId`, price/quantity, and internal status flags.

## Engineering Notes

- Impact ranges from privilege escalation and account takeover to price tampering and bypassing workflow state machines.
- Nested objects and array binding widen the attack surface beyond top-level fields.
- Read-only or server-computed fields are especially dangerous when they share a binder with user-editable ones.

## Defensive Use

- Bind to an explicit allowlist: use a dedicated DTO / view model that contains only the fields a client may set.
- Prefer allowlisting (permit these fields) over blocklisting (deny these fields), which fails open as models grow.
- Separate input models from persistence models; map fields explicitly rather than binding the ORM entity directly.
- Set sensitive attributes (role, ownership, pricing) exclusively from server-side logic.

## Sources

- OWASP Mass Assignment Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html
- OWASP API Security Top 10 - https://owasp.org/API-Security/

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
