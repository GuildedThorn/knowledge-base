---
summary: "Injecting harmful content into cached responses via unkeyed inputs so it is served to many later victims."
status: active
tags: [security, web, cache, unkeyed-input]
private: false
---

# Web Cache Poisoning

## Purpose

Injecting harmful content into cached responses via unkeyed inputs so it is served to many later victims.

## How It Works

- A cache stores responses under a cache key, typically derived from the request line and a subset of headers (e.g. Host, path).
- Inputs that influence the response but are not part of the key are "unkeyed" - an attacker can vary them without changing which cache entry is written.
- The attacker sends a request whose unkeyed input triggers a harmful response; the cache stores it and serves the poisoned copy to everyone hitting that key.
- Common unkeyed vectors: `X-Forwarded-Host`, `X-Forwarded-Scheme`, `X-Host`, and other custom headers reflected into links, scripts, or redirects.

## Discovery

- Identify inputs reflected in the response, then confirm they are unkeyed by checking whether varying them still returns a cached hit for the same key.
- Watch cache-status headers (`X-Cache`, `Age`, `Cache-Control`) to distinguish hits from misses while probing.
- Chain with header injection, XSS, or open redirect to escalate a reflected value into stored impact across all cache consumers.

## Mitigation

- Avoid supporting unkeyed inputs; if reflected, include them in the cache key or strip them at the cache tier.
- Do not cache responses that vary by request-specific headers, and disable caching for dynamic/authenticated content.
- Sanitize and encode all header-derived values before reflecting them into responses.

## Sources

- PortSwigger Web Security Academy - https://portswigger.net/web-security/web-cache-poisoning
- Practical Web Cache Poisoning (James Kettle) - https://portswigger.net/research/practical-web-cache-poisoning

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
