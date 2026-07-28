---
summary: "Cloud metadata abuse turns SSRF or local code execution into access to instance metadata, temporary credentials, and cloud identity context."
status: active
tags: [security, cloud, aws, metadata]
private: false
---

# Cloud IMDS and Metadata Abuse

## Purpose

Cloud metadata abuse turns SSRF or local code execution into access to instance metadata, temporary credentials, and cloud identity context.

## Key Ideas

- AWS IMDS exposes instance metadata and role credentials from a link-local endpoint inside the instance.
- IMDSv2 adds session-oriented token requirements to reduce SSRF/open-proxy paths against metadata.
- The risk is privilege amplification: an app bug can become cloud API access if the instance role is too broad.

## Defensive Use

- Require IMDSv2, set hop limits deliberately, block unnecessary metadata access from containers, and least-privilege instance roles.
- Monitor CloudTrail for unexpected role credential use, unusual regions/services, and API calls inconsistent with the workload.

## Sources

- AWS EC2 - Use the Instance Metadata Service - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html
- AWS Security Blog - IMDSv2 defense in depth - https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/
- AWS - Configure instance metadata options - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html

## Related

- [Cloud & Container - Index](kb://11-security-cloud-container-cloud-container-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
