---
summary: "Packers compress, encrypt, or virtualize malware code so static analysis sees a wrapper before the real payload is reconstructed."
status: active
tags: [security, reversing, packer, malware-analysis]
private: false
---

# Packers and Unpacking

## Purpose

Packers compress, encrypt, or virtualize malware code so static analysis sees a wrapper before the real payload is reconstructed.

## Key Ideas

- Packing changes file entropy, section names, imports, entry-point behavior, and memory layout.
- Common unpacking strategy: identify the wrapper, let it reconstruct the payload in memory, dump, then repair enough metadata for analysis.
- Some protectors use virtualization, anti-debugging, and staged decryption to keep useful code out of the original file.

## Defensive Use

- Detect both the packer and the unpacked payload when possible; packer-only signatures tend to be broad and noisy.
- Prefer behavior and memory indicators for packed threats because disk bytes can be regenerated frequently.

## Sources

- Practical Malware Analysis - packers and unpacking - https://nostarch.com/malware
- MITRE ATT&CK - Software Packing T1027.002 - https://attack.mitre.org/techniques/T1027/002/
- YARA documentation - https://yara.readthedocs.io/en/latest/

## Related

- [Reversing - Index](kb://11-security-reversing-reversing-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
