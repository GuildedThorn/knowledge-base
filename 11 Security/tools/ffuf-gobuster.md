---
summary: ffuf & gobuster — directory, vhost, and parameter fuzzing with filtering.
status: active
tags: [security, tools, fuzzing, web]
private: false
---

# ffuf & gobuster

Content discovery by brute-forcing a wordlist against a `FUZZ` marker. ffuf is the flexible one (any position, filters); gobuster is fast for the common cases.

## ffuf

```bash
# directories
ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt \
     -u http://$IP/FUZZ -e .php,.txt,.html

# vhosts (FUZZ in the Host header) — filter the baseline size
ffuf -w subdomains-top1million-5000.txt -H "Host: FUZZ.$DOMAIN" -u http://$IP -fs 1234

# GET parameter name
ffuf -w burp-parameter-names.txt -u "http://$IP/page?FUZZ=1" -fs 0

# POST body / creds
ffuf -w pass.txt -X POST -d "user=admin&pass=FUZZ" \
     -H "Content-Type: application/x-www-form-urlencoded" -u http://$IP/login -fc 200
```

### Filters / matchers (kill noise)

- `-fs` size · `-fc` status code · `-fw` words · `-fl` lines · `-fr` regex
- matchers mirror them: `-ms -mc -mw -ml -mr`
- `-ac` auto-calibrate (auto-detect the junk baseline) · `-recursion`

## gobuster

```bash
gobuster dir -u http://$IP -w raft-medium-directories.txt -x php,txt -t 50
gobuster vhost -u http://$IP -w subdomains.txt --append-domain
gobuster dns -d $DOMAIN -w subdomains.txt
```

## Related

- [ffuf tool index](kb://11-security-tools-tools-index)
- [Recon & Enumeration](kb://11-security-playbook-recon-enumeration)
- [Web Application Testing](kb://11-security-playbook-web-app-testing)
