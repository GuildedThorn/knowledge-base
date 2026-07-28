---
summary: "Forging JSON Web Tokens via alg:none, weak secrets, and RS256-to-HS256 algorithm confusion flaws."
status: active
tags: [security, web, jwt, algorithm-confusion, signature]
private: false
---

# JWT Attacks and Algorithm Confusion

## Purpose

Forging JSON Web Tokens via alg:none, weak secrets, and RS256-to-HS256 algorithm confusion flaws.

## Attack Techniques

- `alg: none`: a token with the signature stripped is accepted if the server trusts the header's declared algorithm and skips verification.
- Weak HMAC secrets: HS256 tokens can be brute-forced or dictionary-cracked offline (e.g. with hashcat mode 16500) to recover the signing key.
- RS256-to-HS256 confusion: the server's RSA public key is passed as the HMAC secret; an attacker signs with HS256 using that known public key and the server verifies it as valid.
- Header injection: attacker-controlled `jwk` (embedded key), `jku` (remote key URL), and `kid` (key selector, exploitable via path traversal or SQL injection) can point verification at a key the attacker controls.

## Defensive Notes

- Pin the accepted algorithm server-side; never trust the token header's `alg` field to select the verification method.
- Reject `alg: none` outright and use libraries that separate symmetric and asymmetric verification APIs.
- Use high-entropy secrets for HMAC and rotate keys; validate `kid` against an allowlist and never fetch `jku`/`jwk` from untrusted origins.
- Enforce `exp`, `nbf`, `aud`, and `iss` claim checks on every request.

## Sources

- RFC 7519 JSON Web Token - https://datatracker.ietf.org/doc/html/rfc7519
- PortSwigger Web Security Academy - https://portswigger.net/web-security/jwt
- Auth0 Critical Vulnerabilities in JWT Libraries - https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
