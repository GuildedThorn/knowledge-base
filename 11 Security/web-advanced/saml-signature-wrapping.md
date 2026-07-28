---
summary: "XML signature wrapping attacks that alter SAML assertions while keeping a valid signature to bypass SSO auth."
status: active
tags: [security, web, saml, xml-signature, sso]
private: false
---

# SAML Signature Wrapping

## Purpose

XML signature wrapping attacks that alter SAML assertions while keeping a valid signature to bypass SSO auth.

## How It Works

- XML Signature Wrapping (XSW) exploits the gap between the element a signature references and the element the application processes for authorization.
- The attacker keeps the original signed assertion (which validates) but injects a forged assertion elsewhere in the document that the SP business logic reads instead.
- Root cause is that signature validation and assertion consumption resolve the target element independently, often by ID, XPath, or first-match — allowing them to diverge.
- Somorovsky et al. (USENIX 2012) demonstrated 8 XSW variants defeating major SAML frameworks and cloud SSO providers.

## Defensive Notes

- Validate the signature over exactly the same element the application later trusts; process only the specific signed assertion, not a re-queried one.
- Use secure, schema-validated XML parsing; reject documents with multiple assertions or duplicate IDs.
- Verify the signature references the expected element by strict, absolute reference rather than loose ID lookups.
- Check assertion conditions: `NotBefore`/`NotOnOrAfter`, `Audience`, recipient, and `InResponseTo`.

## Sources

- On Breaking SAML (USENIX Security 2012) - https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/somorovsky
- SAML 2.0 (Wikipedia) - https://en.wikipedia.org/wiki/SAML_2.0
- OWASP SAML Security Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
