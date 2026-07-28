---
summary: "Mirai showed how default credentials and unmanaged IoT fleets can scale into internet-impacting DDoS botnets."
status: active
tags: [security, threat-intel, iot, ddos]
private: false
---

# Mirai Botnet

## Purpose

Mirai showed how default credentials and unmanaged IoT fleets can scale into internet-impacting DDoS botnets.

## Key Ideas

- Mirai scanned for exposed embedded devices with weak/default credentials, then used compromised devices for large DDoS campaigns.
- The USENIX retrospective measured rapid growth, variant competition, and the fragile operational model of consumer/embedded IoT.
- The lesson is structural: even simple malware becomes systemic when device owners cannot patch, monitor, or rotate credentials at scale.

## Defensive Use

- Inventory embedded devices, remove default credentials, block inbound management from the internet, and segment IoT from critical networks.
- Track outbound scanning and DDoS command patterns from network devices that should never initiate broad internet scans.

## Sources

- Understanding the Mirai Botnet - USENIX Security 2017 - https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-antonakakis.pdf
- Elie Bursztein - Understanding the Mirai Botnet - https://elie.net/publication/understanding-the-mirai-botnet
- Cloudflare - Inside the infamous Mirai IoT Botnet - https://blog.cloudflare.com/inside-mirai-the-infamous-iot-botnet-a-retrospective-analysis/

## Related

- [Threat Intel - Index](kb://11-security-threat-intel-threat-intel-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
