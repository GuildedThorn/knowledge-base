---
summary: "Executing arbitrary shell commands by injecting into OS calls, including blind and out-of-band variants."
status: active
tags: [security, web, shell, rce]
private: false
---

# OS Command Injection

## Purpose

Executing arbitrary shell commands by injecting into OS calls, including blind and out-of-band variants.

## How It Works

- Occurs when user input is passed to a shell-invoking API (`system`, `popen`, `exec`, backticks, `Runtime.exec`) without sanitization.
- Shell metacharacters chain or terminate the intended command: `;`, `&`, `&&`, `|`, `||`, newline, and command substitution `` `...` `` or `$(...)`.
- Injected input inherits the privileges of the running process, so success can mean full host compromise.

## Detection

- Direct injection returns command output inline; test with `whoami`, `id`, or arithmetic echoes.
- Blind injection yields no output: infer success via time delays (`ping -c 10 127.0.0.1`, `sleep 10`) or conditional errors.
- Out-of-band (OOB) confirmation triggers DNS or HTTP callbacks to an attacker-controlled host (e.g. `nslookup`, `curl` to a Burp Collaborator domain) when in-band channels are closed.

## Defensive Use

- Avoid shelling out entirely; use language-native APIs and libraries instead of constructing command strings.
- If a call is unavoidable, pass arguments as an array/argv vector so no shell parses them, and never concatenate user input.
- Apply strict input allowlisting (expected characters/values only) and run the process with least privilege.

## Sources

- PortSwigger Web Security Academy - https://portswigger.net/web-security/os-command-injection
- OWASP Command Injection - https://owasp.org/www-community/attacks/Command_Injection

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
