---
summary: "Cloudflare's 2019 WAF outage shows how unsafe regex, global rollout, and operational coupling can create a global CPU-exhaustion incident."
status: active
tags: [reference, engineering, sre, incident, postmortem, cloudflare]
private: false
---

# Cloudflare 2019 WAF Outage

## Purpose

Cloudflare's July 2, 2019 outage is a high-value incident study in global rollout safety, regex performance hazards, CPU exhaustion, status-page dependencies, and rollback design.

## Incident Pattern

- A WAF rule change introduced catastrophic regular-expression backtracking.
- The change was deployed globally rather than gradually.
- CPU exhaustion caused widespread 502 errors.
- Mitigation required disabling the managed WAF ruleset globally, then correcting and re-enabling the rule path.

## Lessons

- Performance tests need adversarial inputs, not just functional correctness.
- Regex engines and rule DSLs need runtime limits or safer matching engines for untrusted inputs.
- Progressive rollout is required for globally deployed edge logic.
- Rollback paths must be faster than the incident they are meant to mitigate.
- Status pages, dashboards, and emergency controls should not depend entirely on the impaired production path.

## Operational Controls

- Stage edge-rule deployments by PoP, region, customer cohort, or traffic slice.
- Add CPU/time budget tests for rule sets.
- Prefer regex engines with guaranteed linear-time behavior where feasible.
- Maintain bypass procedures and rehearse them.
- Alert on global traffic drop and service symptoms, not only component-local checks.

## Sources

- Cloudflare Blog - Cloudflare outage caused by bad software deploy - https://blog.cloudflare.com/cloudflare-outage/
- Cloudflare Blog - Details of the Cloudflare outage on July 2, 2019 - https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Incident Management and Postmortems](kb://06-reference-engineering-observability-sre-incident-management-and-postmortems)
- [Adaptive Concurrency Limits](kb://06-reference-engineering-observability-sre-adaptive-concurrency-limits)
