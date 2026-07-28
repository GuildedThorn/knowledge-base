---
summary: "BloodHound models identity relationships as attack paths so defenders can find and remove privilege paths before intrusions abuse them."
status: active
tags: [security, active-directory, bloodhound, identity]
private: false
---

# BloodHound Attack Path Management

## Purpose

BloodHound models identity relationships as attack paths so defenders can find and remove privilege paths before intrusions abuse them.

## Key Ideas

- An attack path is a chain of abusable privileges or behaviors connecting a principal to a privileged asset.
- BloodHound findings use exposure and impact to prioritize choke points rather than enumerating every possible path equally.
- The defender goal is path removal: clean delegation, group membership, local admin, session, ACL, and Tier Zero exposure.

## Defensive Use

- Run regular collection in AD/Entra environments, remediate high-exposure/high-impact choke points, and track exposure trend over time.
- Feed priority findings into ticketing/SIEM workflows so identity risk becomes an operational backlog, not a one-off graph review.

## Sources

- SpecterOps - BloodHound Attack Paths - https://bloodhound.specterops.io/analyze-data/findings/attack-paths
- SpecterOps - BloodHound Glossary - https://bloodhound.specterops.io/resources/glossary/overview
- SpecterOps - What is Attack Path Management? - https://specterops.io/what-is-attack-path-management/

## Related

- [C2 & Post-Ex - Index](kb://11-security-c2-postex-c2-postex-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
