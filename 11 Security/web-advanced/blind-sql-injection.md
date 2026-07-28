---
summary: "SQL injection recovered without visible output using boolean-conditional, error-based, and time-delay inference channels."
status: active
tags: [security, web, sqli, inference, time-based]
private: false
---

# Blind SQL Injection

## Purpose

SQL injection recovered without visible output using boolean-conditional, error-based, and time-delay inference channels.

## Inference Channels

- Blind SQLi arises when a query is injectable but neither results nor errors are returned to the response, so data is inferred one bit at a time.
- Boolean-based: inject a condition and observe a binary difference in the application response (e.g. content present vs absent) to test each hypothesis true/false.
- Error-based: force a conditional database error (division by zero, CAST failure) that changes the response when a tested condition is true.
- Time-based: pair a condition with a delay primitive so a slow response signals true, used when responses are otherwise identical.

## Automating Extraction

- Character-by-character extraction uses SUBSTRING plus comparison/ASCII, resolved via binary search to reduce request count.
- Delay primitives differ by engine: MySQL `SLEEP()`/`BENCHMARK()`, PostgreSQL `pg_sleep()`, MSSQL `WAITFOR DELAY`, Oracle heavy queries or `dbms_pipe.receive_message`.
- Tools like sqlmap automate detection, technique selection, and multi-threaded extraction across these channels.

## Out-of-Band (DNS) Channels

- When in-band inference is too slow or blocked, OOB exfiltration triggers a DNS or HTTP callback carrying extracted data to an attacker-controlled server.
- Examples: MSSQL via UNC path lookups, Oracle via `UTL_HTTP`/`UTL_INADDR`, resolving to a monitored DNS zone.
- OOB works even when the injection point is fully asynchronous, since data leaves via a separate network path.

## Sources

- PortSwigger Web Security Academy - https://portswigger.net/web-security/sql-injection/blind
- OWASP Blind SQL Injection - https://owasp.org/www-community/attacks/Blind_SQL_Injection

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
