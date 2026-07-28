---
summary: "UEFI bootkits persist below the operating system by modifying boot components, weakening trust in startup and endpoint remediation."
status: active
tags: [security, hardware, uefi, bootkit]
private: false
---

# UEFI Bootkits and Secure Boot

## Purpose

UEFI bootkits persist below the operating system by modifying boot components, weakening trust in startup and endpoint remediation.

## Key Ideas

- Bootkits run before or during OS startup, allowing stealthy persistence and potential disabling of OS security mechanisms.
- BlackLotus demonstrated practical UEFI Secure Boot bypass conditions using vulnerable signed boot components that were not fully revoked.
- Secure Boot is a policy and key-management system; default-on is not the same as correctly managed.

## Defensive Use

- Verify Secure Boot state, db/dbx contents, boot order, EFI System Partition contents, and firmware updates during high-confidence incident response.
- Follow NSA guidance for Secure Boot configuration and recovery instead of disabling Secure Boot for compatibility.

## Sources

- NSA - Guidance for Managing UEFI Secure Boot - https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4356302/nsa-releases-unified-extensible-firmware-interface-secure-boot-guidance/
- MITRE ATT&CK - Bootkit T1542.003 - https://attack.mitre.org/techniques/T1542/003/
- ESET - BlackLotus UEFI bootkit analysis - https://www.eset.com/uk/about/newsroom/press-releases/eset-research-analyses-blacklotus-a-uefi-bootkit-that-can-bypass-uefi-secure-boot-on-fully-patched-systems0/

## Related

- [Mobile & Hardware - Index](kb://11-security-mobile-hardware-mobile-hardware-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
