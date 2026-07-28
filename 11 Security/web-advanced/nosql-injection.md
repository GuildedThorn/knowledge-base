---
summary: "Injecting operators and JavaScript into document-store queries (e.g. MongoDB) to bypass auth or extract data."
status: active
tags: [security, web, nosql, sqli, mongodb, query-operator]
private: false
---

# NoSQL Injection

## Purpose

Injecting operators and JavaScript into document-store queries (e.g. MongoDB) to bypass auth or extract data.

## Operator Injection

- When user input reaches a query object unsanitized, an attacker supplies query operators instead of scalar values.
- `$ne` (not equal), `$gt`/`$lt`, `$regex`, and `$in` alter match logic; e.g. `{"username":"admin","password":{"$ne":null}}` can bypass an auth check.
- Injection often enters via JSON bodies or via bracket-parsed query strings (`user[$ne]=`) that frameworks deserialize into nested objects.
- Mitigation is input type validation, casting values to strings, and rejecting keys beginning with `$`.

## Syntax vs JavaScript Injection

- Syntax injection breaks or manipulates the query structure itself, analogous to classic SQLi.
- JavaScript injection targets server-side evaluation via `$where`, `mapReduce`, or `$accumulator`, allowing arbitrary JS conditions.
- A `$where` payload can smuggle boolean logic or, in older/misconfigured setups, sleep loops for timing inference.

## Blind NoSQL Extraction

- With no direct output, attackers use `$regex` anchored guesses to reveal field values character by character via response differences.
- Boolean and time-based inference mirror blind SQLi, using JS loops or regex matches as the true/false oracle.
- The OWASP WSTG documents systematic testing for both operator and JavaScript-based NoSQL injection.

## Sources

- PortSwigger Web Security Academy - https://portswigger.net/web-security/nosql-injection
- OWASP Web Security Testing Guide - https://owasp.org/www-project-web-security-testing-guide/

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
