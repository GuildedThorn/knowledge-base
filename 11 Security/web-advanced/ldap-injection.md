---
summary: "Manipulating LDAP search filters via unsanitized input to bypass authentication or enumerate directory data."
status: active
tags: [security, web, ldap, filter, directory]
private: false
---

# LDAP Injection

## Purpose

Manipulating LDAP search filters via unsanitized input to bypass authentication or enumerate directory data.

## How It Works

- LDAP filters use a prefix (Polish) notation with parentheses and logical operators, e.g. `(&(uid=alice)(userPassword=secret))`.
- When input is concatenated into a filter string, metacharacters `( ) & | ! * = \` and NUL let an attacker rewrite the query.
- A classic auth bypass injects `*` into a username or appends `)(uid=*))(|(uid=*` to force the filter to always match.

## Attack Techniques

- Authentication bypass: wildcards and always-true clauses make the bind or search succeed without valid credentials.
- Blind enumeration: no direct output, so attackers infer directory contents character-by-character using boolean filter conditions and response differences.
- Attribute disclosure can widen a query with `|` to return records or attributes the application never intended to expose.

## Defensive Use

- Escape filter input per RFC 4515: encode `*` `(` `)` `\` and NUL as `\2a \28 \29 \5c \00`; escape distinguished-name special characters separately.
- Prefer parameterized/framework LDAP APIs and strict input allowlisting over hand-built filter strings.
- Bind with least-privilege service accounts and validate that returned entries match the expected scope.

## Sources

- OWASP LDAP Injection - https://owasp.org/www-community/attacks/LDAP_Injection
- OWASP LDAP Injection Prevention Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
