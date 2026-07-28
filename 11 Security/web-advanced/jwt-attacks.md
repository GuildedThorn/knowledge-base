---
summary: JWT attacks forge or bypass token signatures via alg:none, weak-HMAC brute force, jwk/jku/kid header injection, RS256->HS256 key confusion, and ECDSA psychic signatures to achieve authentication and authorization bypass.
status: active
tags: [security, web, jwt, appsec]
private: false
---

# JWT Attacks

A JSON Web Token (JWT, RFC 7519) is a base64url-encoded header.payload.signature triple whose trust rests entirely on the signature — since servers usually keep no server-side state about issued tokens. Attacks target flaws in how servers verify (or fail to verify) that signature.

## The vulnerability
JWT security collapses when the server trusts the token's self-described algorithm or skips verification. Because the `alg` header is attacker-controlled, an implementation that honors it — or confuses `decode()` with `verify()` — lets an attacker rewrite claims (e.g. `admin: true`, a different `sub`) and have them accepted. RFC 7519 states that unless the algorithms are acceptable to the application it SHOULD reject the JWT, but many libraries historically did not enforce this.

## Exploitation techniques
- **alg:none** — set `"alg":"none"` and strip the signature; vulnerable libs accept the unsigned token. Bypass string filters with mixed capitalization (`NoNe`).
- **Weak HMAC secret brute force** — HS256 uses a shared string secret; crack it offline with `hashcat -a 0 -m 16500 <jwt> <wordlist>` or jwt_tool, then sign forged tokens.
- **jwk header injection** — embed an attacker RSA public key directly in the token header (automatable with Burp's JWT Editor).
- **jku header injection** — point `jku` at an attacker-hosted JWK Set, abusing URL-parsing discrepancies to defeat host allowlists.
- **kid path traversal** — point `kid` at a predictable static file such as `/dev/null` and sign with an empty string.
- **Algorithm confusion (RS256->HS256)** — a server expecting RSA verifies with its public key; sign the token with HMAC using that public key as the HMAC secret, and the server treats the public key as the shared secret.

## Real-world cases (sourced)
Tim McLean's 2015 Auth0 advisory disclosed both alg:none and RS256->HS256 key confusion across node-jsonwebtoken, pyjwt, namshi/jose, php-jwt, and jsjwt. **CVE-2022-21449 "Psychic Signatures"** (Java 15-18) let a fully blank ECDSA signature (r=0, s=0) validate for ES256/ES384/ES512, breaking signed JWTs, SAML, OIDC, and WebAuthn — ForgeRock rated it 10.0.

## Detection & prevention
Explicitly pin and validate the expected `alg`; reject `none`. Use 64+ char random HMAC secrets or asymmetric keys (RS256/ES256/EdDSA). Allowlist `jku` hosts and sanitize `kid` against traversal/injection. Add token context binding to resist sidejacking, and maintain a `jti`/`iss` denylist for revocation. Patch JVMs against CVE-2022-21449.

## Sources
- JWT attacks — Web Security Academy (PortSwigger) — https://portswigger.net/web-security/jwt
- Critical vulnerabilities in JSON Web Token libraries (Tim McLean, Auth0) — https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/
- Psychic Signatures in Java / CVE-2022-21449 (Neil Madden) — https://neilmadden.blog/2022/04/19/psychic-signatures-in-java/
- JSON Web Token Cheat Sheet (OWASP) — https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html
- RFC 7519 JSON Web Token (IETF) — https://datatracker.ietf.org/doc/html/rfc7519

## Related
- [Web-Advanced — Index](kb://11-security-web-advanced-web-advanced-index)
- [Web App Testing](kb://11-security-playbook-web-app-testing)
- [Payload Cheat Sheets — Index](kb://11-security-payloads-payloads-index)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
