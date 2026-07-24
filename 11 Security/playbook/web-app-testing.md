---
summary: Web attack surface cheat sheet — auth, injection, upload, LFI/SSRF/traversal, deserialization.
status: active
tags: [security, playbook, web, appsec]
private: false
---

# Web Application Testing

The largest attack surface on most boxes. Proxy everything through Burp; test each input class methodically.

## Map first

- Spider + note every parameter, form, cookie, and API endpoint.
- Check `robots.txt`, `sitemap.xml`, JS bundles (source maps, hardcoded keys/endpoints), `/api`, `/.git/`.
- Fingerprint the framework — the vuln class usually follows from it (e.g. `X-Powered-By: pdfminer.six` → pickle RCE on Bedsides).

## Injection

- **SQLi**: `' OR 1=1-- -`, then `sqlmap -u '<url>' --batch --dump`. Watch for auth bypass, UNION, blind/time-based.
- **Command injection**: `; id`, `| id`, `$(id)`, `` `id` ``, newline `%0a`. Confirm with OOB DNS/HTTP if blind.
- **SSTI**: `{{7*7}}` / `${7*7}` → 49 means template eval → often RCE (Jinja2, Twig, Freemarker).
- **NoSQL**: `{"$ne": null}`, `[$gt]=`.

## File upload

- Bypass filters: double ext (`.php.jpg`), null byte, case, magic-byte prefix, `.phtml/.phar/.svg`, content-type spoof.
- Find where it lands + how it's served (`/uploads/<name>`) — that's the Bedsides upload-probe step.
- If the server *processes* the file (image/PDF/archive), attack the parser, not just the extension (deserialization, zip-symlink, traversal in names).

## LFI / path traversal / SSRF

- **LFI/traversal**: `../../../../etc/passwd`, `--path-as-is` in curl, PHP wrappers (`php://filter/convert.base64-encode/resource=`), log poisoning → RCE.
- **SSRF**: point the server at `http://127.0.0.1:<internal-port>`, cloud metadata `169.254.169.254`. Reaches services the scan showed as `filtered`.

## Insecure deserialization

High-value, often instant RCE. Language pickles/gadget chains:

- **Python `pickle`**: `__reduce__` → `os.system`. Two chained pickle bugs rooted Bedsides (pdfminer + torch).
- **PHP**: `unserialize()` + POP chain (phpggc).
- **Java**: `ysoserial` gadgets.
- **.NET**: `ysoserial.net`.

## Auth & session

- Default/weak creds, user enumeration via error/timing deltas, JWT `alg:none` / weak secret (`jwt_tool`), IDOR by incrementing IDs, password reset token flaws.

## Related

- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index)
- [Recon & Enumeration](kb://11-security-playbook-recon-enumeration)
- [Reverse Shells & Payloads](kb://11-security-playbook-reverse-shells)
