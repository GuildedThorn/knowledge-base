---
summary: "Suricata is a high-performance network IDS/IPS whose signature language inspects traffic for known malicious patterns."
status: active
tags: [security, dfir, suricata, ids, network]
private: false
---

# Suricata IDS/IPS Rules

## Purpose

Suricata is a high-performance network IDS/IPS whose signature language inspects traffic for known malicious patterns.

## Rule Anatomy

- A rule has three parts: an action, a header, and options in parentheses.
- Actions are `pass`, `drop`, `reject`, and `alert`; `drop`/`reject` require inline IPS mode.
- The header specifies protocol, source/destination IP and port, and a direction operator (`->` or `<>`).
- Every rule needs a unique `sid` and a `msg`; `rev` tracks revisions and `classtype` groups by threat class.

## Payload and Flow Keywords

- `content` matches byte or ASCII patterns; modifiers like `nocase`, `offset`, `depth`, `distance`, and `within` constrain where.
- Sticky buffers (`http.uri`, `http.host`, `dns.query`, `tls.sni`, `file.data`) scope matching to parsed protocol fields.
- `flow` (e.g. `established,to_server`) and `flowbits` add stateful and cross-rule logic; `pcre` allows regular expressions.
- `threshold`/`detection_filter` rate-limit noisy signatures.

## Protocol Parsing and Output

- Multi-threaded engine performs application-layer parsing for HTTP, TLS, DNS, SMB, and more, enabling protocol-aware detection.
- EVE JSON is the primary output: alert, flow, http, dns, tls, and fileinfo events for SIEM ingestion.
- Can extract files and compute hashes; integrates with rule feeds like Emerging Threats and Talos.

## Sources

- Suricata - https://suricata.io/
- Suricata Documentation - https://docs.suricata.io/

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
