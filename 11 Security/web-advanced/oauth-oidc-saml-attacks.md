---
summary: "OAuth/OIDC/SAML bugs usually come from trust-boundary mistakes in redirect validation, token validation, metadata, and assertion handling."
status: active
tags: [security, web, identity, oauth]
private: false
---

# OAuth, OIDC, and SAML Attacks

## Purpose

OAuth/OIDC/SAML bugs usually come from trust-boundary mistakes in redirect validation, token validation, metadata, and assertion handling.

## Key Ideas

- OAuth/OIDC attack surface includes redirect URI confusion, missing PKCE, token replay, dynamic-client-registration abuse, discovery metadata, and over-broad scopes.
- SAML attack surface includes signature validation mistakes, XML signature wrapping, audience/destination mismatch, replay windows, and weak algorithms.
- These protocols are security glue: small validation shortcuts can become account takeover or cross-tenant access.

## Defensive Use

- Use maintained libraries, exact redirect allowlists, PKCE, state/nonce validation, strong client auth, short token lifetime, and strict audience/issuer checks.
- For SAML, verify signed elements, destination, recipient, audience, time bounds, certificate trust, and SHA-256-or-stronger signatures.

## Sources

- OWASP OAuth2 Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html
- OWASP SAML Security Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html
- PortSwigger Research - Hidden OAuth attack vectors - https://portswigger.net/research/hidden-oauth-attack-vectors

## Related

- [Web-Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
