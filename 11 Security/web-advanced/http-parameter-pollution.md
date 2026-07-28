---
summary: "Supplying duplicate parameters to exploit inconsistent parsing between application layers and WAFs."
status: active
tags: [security, web, hpp, parameter-parsing]
private: false
---

# HTTP Parameter Pollution

## Purpose

Supplying duplicate parameters to exploit inconsistent parsing between application layers and WAFs.

## Core Model

- HTTP does not define how duplicate query/body parameters (e.g. `id=1&id=2`) should be handled, so each stack picks its own behavior.
- Precedence varies: some platforms take the first value, some the last, some concatenate, and some expose all as an array.
- When a front-end control (WAF, router, framework) and the back-end application resolve duplicates differently, an attacker can smuggle a value past one layer that the other acts on.

## Server-Side vs Client-Side

- Server-side HPP targets back-end parsing to bypass input validation, alter application logic, or reach a value a WAF only inspected the first copy of.
- Client-side HPP injects extra parameters into URLs the application builds (links, forms, redirects), polluting parameters the browser or downstream request later uses.
- Both hinge on a value being reflected or forwarded into a context that re-parses parameters with different precedence.

## Bypass and Defense

- WAF/logic bypass: place a benign value where the filter reads and the payload where the app reads, exploiting the parsing gap.
- Test known platform behaviors (ASP.NET concatenates, PHP/last-wins, JSP/first-wins) to predict which duplicate is honored.
- Defend by canonicalizing parameters early, rejecting unexpected duplicates, and validating on the same parsed representation the application logic uses.

## Sources

- OWASP Web Security Testing Guide - https://owasp.org/www-project-web-security-testing-guide/
- OWASP Testing for HTTP Parameter Pollution - https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
