---
summary: "Encoding command-and-control traffic inside DNS queries and responses to exfiltrate data and evade egress filtering."
status: active
tags: [security, techniques, dns, c2, exfiltration]
private: false
---

# DNS Tunneling C2

## Purpose

Encoding command-and-control traffic inside DNS queries and responses to exfiltrate data and evade egress filtering.

## How It Works

- The client encodes outbound data into subdomain labels (e.g. `<base32-chunk>.tunnel.attacker.com`) of queries for an attacker-controlled zone.
- The attacker runs the authoritative resolver for that domain, so recursive resolvers relay the query to it, bypassing direct egress rules.
- Responses carry tasking back in TXT, CNAME, NULL, or A/AAAA records, encoding bytes the client decodes.
- Label length (63 bytes) and total name length (255 bytes) cap per-query throughput, making the channel slow but resilient.

## Engineering Notes

- Tools like iodine build a full IP-over-DNS tunnel; others (dnscat2) provide an encrypted C2 session channel.
- TXT records maximize per-response capacity; NULL/CNAME variants trade compatibility for bandwidth.
- Maps to MITRE ATT&CK T1071.004 (Application Layer Protocol: DNS).

## Defensive Use

- Baseline query volume and detect high request rates to a single domain and unusually long or high-entropy subdomain labels.
- Flag excessive TXT/NULL queries and clients that bypass internal resolvers to talk DNS directly outbound.
- Force all DNS through logging resolvers and apply DGA/tunneling analytics on the query stream.

## Sources

- MITRE ATT&CK T1071.004 - https://attack.mitre.org/techniques/T1071/004/
- iodine - https://github.com/yarrick/iodine

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
