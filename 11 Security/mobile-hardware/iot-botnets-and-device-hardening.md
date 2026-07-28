---
summary: "IoT botnets exploit weak device management, default credentials, exposed services, and unpatchable embedded fleets."
status: active
tags: [security, hardware, iot, botnet]
private: false
---

# IoT Botnets and Device Hardening

## Purpose

IoT botnets exploit weak device management, default credentials, exposed services, and unpatchable embedded fleets.

## Key Ideas

- Mirai proved that simple credential scanning can compromise enough embedded devices to create major DDoS capacity.
- IoT risk is operational: unknown inventory, abandoned firmware, shared credentials, exposed management ports, and weak monitoring.
- Many devices lack endpoint agents, so network-layer control and procurement standards matter more.

## Defensive Use

- Inventory devices, isolate IoT networks, remove default credentials, block inbound management, restrict outbound scanning, and retire unsupported firmware.
- Require update commitments, unique credentials, and secure defaults when buying new devices.

## Sources

- USENIX - Understanding the Mirai Botnet - https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-antonakakis.pdf
- Cloudflare - Mirai retrospective - https://blog.cloudflare.com/inside-mirai-the-infamous-iot-botnet-a-retrospective-analysis/
- NISTIR 8259 - Foundational Cybersecurity Activities for IoT Device Manufacturers - https://csrc.nist.gov/pubs/ir/8259/final

## Related

- [Mobile & Hardware - Index](kb://11-security-mobile-hardware-mobile-hardware-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
