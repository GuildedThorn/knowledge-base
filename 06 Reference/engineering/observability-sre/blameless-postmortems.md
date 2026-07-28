---
summary: "SRE practice of writing blame-free incident retrospectives focused on systemic causes and durable remediation over individual fault."
status: active
tags: [reference, engineering, sre, incident, postmortem, culture]
private: false
---

# Blameless Postmortems

## Purpose

SRE practice of writing blame-free incident retrospectives focused on systemic causes and durable remediation over individual fault.

## Blameless Framing

- The premise is that people act rationally given the information, tooling, and incentives they had at the time; failure is a property of the system, not the individual.
- Naming and punishing operators drives incidents underground: engineers hide detail, stop reporting near-misses, and the organization stops learning.
- Blameless does not mean accountability-free; it redirects accountability toward fixing the systems and safeguards that allowed the error.

## Timeline and Analysis

- A postmortem reconstructs a factual timeline: detection, escalation, key actions, and recovery, with timestamps drawn from logs and chat.
- Root-cause analysis looks past the triggering change to contributing factors and missing safeguards, often using techniques like the Five Whys.
- It records impact (users affected, duration, budget spent) and what went well, not only what failed.

## Action Items and Review

- Every postmortem yields concrete, owned, tracked action items with priorities, not vague aspirations.
- Google triggers a postmortem on defined thresholds (user-visible downtime, data loss, on-call escalation) so the process is consistent, not discretionary.
- Postmortems are peer-reviewed and shared widely so lessons propagate beyond the responding team.
- A standard template keeps reports comparable and lowers the friction of writing one.

## Sources

- SRE Book: Postmortem Culture - https://sre.google/sre-book/postmortem-culture/
- Postmortem Template - https://sre.google/sre-book/example-postmortem/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
