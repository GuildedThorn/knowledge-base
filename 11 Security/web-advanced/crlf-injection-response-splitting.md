---
summary: "Injecting carriage-return/line-feed sequences into headers to split responses, poison caches, or forge headers."
status: active
tags: [security, web, crlf, header-injection]
private: false
---

# CRLF Injection and HTTP Response Splitting

## Purpose

Injecting carriage-return/line-feed sequences into headers to split responses, poison caches, or forge headers.

## How It Works

- HTTP uses `\r\n` (CRLF) to delimit headers and a blank line (`\r\n\r\n`) to end the header block.
- If user input reaches a response header (e.g. a redirect `Location`, `Set-Cookie`, or custom header) unfiltered, injected CRLF sequences create new headers or a whole second response body.
- Encoded forms like `%0d%0a` are used to smuggle the sequence through the request.

## Impact

- Response splitting can inject a crafted second response that a caching proxy stores, poisoning the cache for other users.
- Injected `<script>` in the split body yields XSS; injected `Set-Cookie` enables session fixation.
- Header forging can also manipulate redirects, content type, or security headers.

## Defensive Use

- Strip or reject CR (`\r`, `%0d`) and LF (`\n`, `%0a`) from any value placed in a header.
- Prefer framework APIs that set headers safely and reject control characters by default (many modern stacks block CRLF automatically).
- URL-encode untrusted data used in redirect targets and validate against an allowlist.

## Sources

- OWASP HTTP Response Splitting - https://owasp.org/www-community/attacks/HTTP_Response_Splitting
- OWASP CRLF Injection - https://owasp.org/www-community/vulnerabilities/CRLF_Injection

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
