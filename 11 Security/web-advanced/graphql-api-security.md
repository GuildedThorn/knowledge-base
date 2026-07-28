---
summary: "GraphQL security failures cluster around authorization, introspection exposure, batching abuse, expensive queries, and resolver injection."
status: active
tags: [security, web, graphql, api-security]
private: false
---

# GraphQL API Security

## Purpose

GraphQL security failures cluster around authorization, introspection exposure, batching abuse, expensive queries, and resolver injection.

## Key Ideas

- GraphQL's flexible query model changes the attack surface: one endpoint can expose many object paths, nested relations, and resolver behaviors.
- Common failures include object-level authorization gaps, introspection/schema leakage, alias/batching brute force, CSRF, and query-cost DoS.
- Resolver code still calls databases, HTTP services, and business logic; injection flaws do not disappear because the API is GraphQL.

## Defensive Use

- Enforce authorization in resolvers for nodes and edges, not just at the outer request.
- Use depth/amount/cost limits, pagination, rate limits, production introspection restrictions, and consistent input validation.

## Sources

- OWASP GraphQL Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html
- PortSwigger - GraphQL API vulnerabilities - https://portswigger.net/web-security/learning-paths/graphql-api-vulnerabilities
- PortSwigger - Working with GraphQL in Burp Suite - https://portswigger.net/burp/documentation/desktop/testing-workflow/working-with-graphql

## Related

- [Web-Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
