---
summary: Burp Suite — intercepting proxy workflow, Repeater/Intruder/Decoder, useful extensions.
status: active
tags: [security, tools, burp, web]
private: false
---

# Burp Suite

The intercepting proxy for web testing. Everything web-facing should route through it so you can inspect and replay requests.

## Setup

- Browser → proxy `127.0.0.1:8080`; install Burp CA cert (`http://burp` → CA cert) to intercept HTTPS.
- Set **Target → Scope** to the host, then "show only in-scope" to keep Proxy history clean.

## Core tools

- **Proxy / Intercept** — pause, edit, forward requests live. Toggle intercept off + use history for passive mapping.
- **Repeater** (`Ctrl-R` to send from anywhere) — hand-tune a single request; the workhorse for manual injection/LFI/auth testing.
- **Intruder** — fuzz positions. Attack types: **Sniper** (one list, one position), **Cluster bomb** (multi-position combos, e.g. user×pass). Filter by status/length in results.
- **Decoder / Inspector** — URL/base64/hex encode-decode, hashes.
- **Comparer** — diff two responses (spot auth-bypass / user-enum deltas).
- **Sequencer** — token randomness analysis.

## Common flow

1. Browse the app with intercept off → passively populate history + sitemap.
2. Right-click an interesting request → **Send to Repeater**, probe by hand.
3. Found a parameter worth brute-forcing → **Send to Intruder**, set positions, load payloads, filter results.
4. Community edition: Intruder is throttled — for speed, hand off to `ffuf` with the same request.

## Extensions (BApp Store)

- **Logger++**, **Autorize** (authz/IDOR testing), **JWT Editor**, **Param Miner** (hidden params), **Turbo Intruder** (fast, scripted).

## Related

- [Burp tool index](kb://11-security-tools-tools-index)
- [Web Application Testing](kb://11-security-playbook-web-app-testing)
