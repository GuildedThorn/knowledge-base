---
summary: "Client-side XSS where a JavaScript source flows to a dangerous sink entirely within the browser DOM."
status: active
tags: [security, web, xss, dom, client-side]
private: false
---

# DOM-Based Cross-Site Scripting

## Purpose

Client-side XSS where a JavaScript source flows to a dangerous sink entirely within the browser DOM.

## How It Works

- The vulnerability lives in client-side JavaScript: a source reads attacker-controllable data and passes it to a sink that executes or renders it, with no server round-trip required.
- Common sources include `location`, `location.hash`, `document.URL`, `document.referrer`, `window.name`, and `postMessage` data.
- Common sinks include `innerHTML`/`outerHTML`, `document.write`, `eval`, `setTimeout` with a string, and `element.src`/`location` assignments.

## Detection

- Trace taint from source to sink by reading the page's JavaScript; the payload often never appears in the HTTP response body.
- Fragment-based payloads (after `#`) are not sent to the server, so server-side filters and logs miss them.
- Tools such as Burp's DOM Invader automate source-to-sink tracing and highlight exploitable flows.

## Defensive Use

- Avoid dangerous sinks; prefer safe DOM APIs like `textContent` and `setAttribute` over `innerHTML`.
- Enforce Trusted Types (`require-trusted-types-for 'script'`) so the browser blocks string assignments to injection sinks.
- Encode/validate data for its DOM context and keep client-side routing/templating within safe framework bindings.

## Sources

- PortSwigger Web Security Academy - https://portswigger.net/web-security/cross-site-scripting/dom-based
- OWASP DOM Based XSS - https://owasp.org/www-community/attacks/DOM_Based_XSS

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
