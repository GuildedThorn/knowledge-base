---
summary: "IETF standard defining the syslog message format with severity, facility, structured data, and transport for event logging."
status: active
tags: [reference, engineering, sre, logging, rfc, protocol]
private: false
---

# Syslog Protocol (RFC 5424)

## Purpose

IETF standard defining the syslog message format with severity, facility, structured data, and transport for event logging.

## Message Format

- Each message begins with a PRI value: `PRI = facility * 8 + severity`, wrapped in angle brackets, e.g. `<34>`.
- Severity ranges 0 (Emergency) to 7 (Debug); facility ranges 0-23 (kernel, mail, auth, local0-7, etc.).
- The header also carries VERSION, an RFC 3339 TIMESTAMP, HOSTNAME, APP-NAME, PROCID, and MSGID fields.
- STRUCTURED-DATA provides machine-parseable key/value elements (SD-ID plus SD-PARAM pairs), replacing the ad-hoc free text of legacy BSD syslog (RFC 3164).

## Transport

- RFC 5426 defines syslog over UDP (best-effort, lossy, no delivery guarantee).
- RFC 6587 defines syslog over TCP with octet-counting or non-transparent framing for reliable delivery.
- RFC 5425 defines syslog over TLS, adding transport encryption and mutual authentication for sensitive log streams.
- The MSG portion is recommended to be UTF-8 with a byte-order-mark to signal encoding.

## Sources

- RFC 5424 The Syslog Protocol - https://www.rfc-editor.org/rfc/rfc5424
- RFC 5425 Syslog over TLS - https://www.rfc-editor.org/rfc/rfc5425

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
