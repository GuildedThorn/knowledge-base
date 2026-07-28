---
summary: "CI/CD abuse targets workflow tokens, secrets, runners, dependencies, artifact provenance, and deployment permissions."
status: active
tags: [security, cloud, cicd, supply-chain]
private: false
---

# CI/CD Pipeline Abuse

## Purpose

CI/CD abuse targets workflow tokens, secrets, runners, dependencies, artifact provenance, and deployment permissions.

## Key Ideas

- Pipelines often bridge source control, secrets, cloud deploy keys, package registries, and production infrastructure.
- Common risks include over-privileged workflow tokens, untrusted pull-request execution, secret exfiltration, poisoned dependencies, and mutable unsigned artifacts.
- Runner trust boundaries matter: self-hosted runners can become persistence and lateral-movement surfaces.

## Defensive Use

- Use least-privilege job permissions, protected environments, isolated runners, pinned actions/images, secret scanning, branch protection, and signed/provenance-bearing artifacts.
- Review pipelines as production access paths, not just developer automation.

## Sources

- OpenSSF Scorecard - https://scorecard.dev/
- OpenSSF Scorecard GitHub Action - https://github.com/ossf/scorecard-action
- SLSA framework - https://slsa.dev/

## Related

- [Cloud & Container - Index](kb://11-security-cloud-container-cloud-container-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
