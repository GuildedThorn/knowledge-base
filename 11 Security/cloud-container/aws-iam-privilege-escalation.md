---
summary: "AWS IAM privilege escalation abuses dangerous permission combinations to create, pass, update, or assume more powerful access."
status: active
tags: [security, cloud, aws, iam]
private: false
---

# AWS IAM Privilege Escalation

## Purpose

AWS IAM privilege escalation abuses dangerous permission combinations to create, pass, update, or assume more powerful access.

## Key Ideas

- Privilege escalation usually comes from combinations: policy versioning, role passing, function/profile creation, instance profile attachment, or trust-policy mistakes.
- `iam:PassRole` is especially sensitive because it lets a principal delegate a role to a service that may then act with that role.
- Effective cloud least privilege must reason about API action combinations, not one permission string at a time.

## Defensive Use

- Continuously analyze IAM for escalation paths, unused permissions, wildcard actions/resources, broad trust policies, and service-role pass paths.
- Use SCPs/permission boundaries to block known dangerous combinations even when local account policies drift.

## Sources

- Rhino Security Labs - AWS IAM Privilege Escalation - https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/
- AWS Security Blog - How to use PassRole - https://aws.amazon.com/blogs/security/how-to-use-the-passrole-permission-with-iam-roles/
- AWS IAM best practices - https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html

## Related

- [Cloud & Container - Index](kb://11-security-cloud-container-cloud-container-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
