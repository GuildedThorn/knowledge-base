---
summary: "Feature flags decouple deployment from release, enabling gradual rollout, experiments, kill switches, and operational control."
status: active
tags: [reference, engineering, architecture, feature-flags]
private: false
---

# Feature Flags and Progressive Delivery

## Purpose

Feature flags decouple deployment from release, enabling gradual rollout, experiments, kill switches, and operational control.

## Core Model

- Flags can be release, experiment, ops, permission, or migration flags.
- Progressive delivery rolls changes through cohorts while observing health.
- Long-lived flags become branching logic debt and must be retired.

## Engineering Notes

- Name flags with owner, purpose, creation date, and removal condition.
- Keep flag evaluation fast, observable, and safe under config-service failure.
- Do not use flags as a substitute for schema/backward compatibility.

## Sources

- Martin Fowler - Feature Toggles - https://martinfowler.com/articles/feature-toggles.html
- OpenFeature specification - https://openfeature.dev/specification/
- LaunchDarkly - Progressive delivery - https://launchdarkly.com/blog/what-is-progressive-delivery/

## Related

- [Software Architecture - Index](kb://06-reference-engineering-software-architecture-software-architecture-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
