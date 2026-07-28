---
summary: "Software supply-chain defense protects source, dependencies, builds, signing, provenance, release, and procurement trust decisions."
status: active
tags: [security, supply-chain, slsa, openssf]
private: false
---

# Software Supply Chain Security

## Purpose

Software supply-chain defense protects source, dependencies, builds, signing, provenance, release, and procurement trust decisions.

## Key Ideas

- Supply-chain compromise can target dependencies, maintainers, CI/CD tokens, build runners, artifact registries, signing keys, or update channels.
- SLSA, OpenSSF Scorecard, SBOMs, and secure-build guidance provide complementary controls rather than one complete solution.
- Consumers need provenance and supplier risk evidence; producers need hardened development and release processes.

## Defensive Use

- Require branch protection, code review, dependency update automation, signed/provenance-bearing builds, secret scanning, and least-privilege CI tokens.
- Review critical dependencies by maintainer health, release process, transitive exposure, and artifact integrity.

## Sources

- SLSA framework - https://slsa.dev/
- OpenSSF Scorecard - https://scorecard.dev/
- NSA/CISA ESF - Managing Open Source Software and SBOMs - https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/3613105/nsa-and-esf-partners-release-recommended-practices-for-managing-open-source-sof/

## Related

- [Crypto & Ransomware - Index](kb://11-security-crypto-ransomware-crypto-ransomware-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
