---
summary: "SSTI occurs when user input is interpreted as server-side template code instead of data, often escalating to server compromise."
status: active
tags: [security, web, ssti, appsec]
private: false
---

# Server-Side Template Injection

## Purpose

SSTI occurs when user input is interpreted as server-side template code instead of data, often escalating to server compromise.

## Key Ideas

- The bug appears when untrusted input is concatenated into a template or users can author templates without a strong sandbox.
- Impact varies by engine and context, but server-side evaluation can expose objects, files, secrets, or command execution paths.
- SSTI is easy to misclassify as XSS because initial proof often renders in HTML.

## Defensive Use

- Never build templates from user input; pass input as data into fixed templates.
- If user-authored templates are a business requirement, use a deliberately constrained engine and isolate rendering with strict resource and object boundaries.

## Sources

- PortSwigger Research - Server-Side Template Injection - https://portswigger.net/research/server-side-template-injection
- PortSwigger Web Security Academy - SSTI - https://portswigger.net/web-security/server-side-template-injection
- PortSwigger KB - Server-side template injection - https://portswigger.net/kb/issues/00101080_server-side-template-injection

## Related

- [Web-Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
