---
summary: Desynchronizing how chained HTTP servers parse request boundaries so an attacker-controlled prefix is smuggled onto the next user's request, enabling credential capture, cache poisoning, and control bypass.
status: active
tags: [security, web, http-request-smuggling, appsec]
private: false
---

# HTTP Request Smuggling

Request smuggling interferes with how a site processes a sequence of HTTP requests received from one or more users. When a front-end and back-end disagree about where one request ends and the next begins, an attacker can inject a hidden request that gets prepended to a victim's traffic.

## The vulnerability
HTTP/1.1 offers two ways to declare message length: `Content-Length` and `Transfer-Encoding: chunked`. When a front-end (proxy, load balancer, WAF, CDN) and back-end interpret these differently — or handle duplicate/obfuscated headers inconsistently — request boundaries become ambiguous (CWE-444, "Inconsistent Interpretation of HTTP Requests"). The first documented treatment is Watchfire's 2005 paper by Linhart, Klein, Heled, and Orrin, describing cache poisoning, firewall/WAF bypass, and request/credential hijacking.

## Exploitation techniques
Classic HTTP/1 desyncs (James Kettle, "HTTP Desync Attacks: Request Smuggling Reborn", 2019):
- **CL.TE** — front-end honors `Content-Length`, back-end honors `Transfer-Encoding`.
- **TE.CL** — the reverse.
- **TE.TE** — both support `Transfer-Encoding`, but one is tricked via obfuscation (`Transfer-Encoding: xchunked`, trailing space, odd casing).

Detection is timeout-based: a malformed request makes a vulnerable back-end hang while synced servers respond normally. HTTP/2 downgrading ("HTTP/2: The Sequel is Always Worse", 2021) adds **H2.CL** and **H2.TE** desyncs plus request tunnelling and response splitting. **CL.0** and **client-side desync (CSD)** ("Browser-Powered Desync Attacks", 2022) extend attacks to single-server sites, using spec-compliant requests, pause-based desync (Apache, Varnish), and abuse of first-request routing/validation.

## Real-world cases (sourced)
From Kettle's research: **PayPal** login-page JS hijack ($18,900 then $20,000); **Trello** and **New Relic** admin/API access via HackerOne; **Netflix** H2.CL via Netty ($20,000); **AWS ALB** H2.TE ($7,000+$10,000); **Atlassian Jira** request splitting ($15,000); **Amazon.com** client-side desync capturing auth tokens; **Akamai/Capital One**, **Cisco ASA WebVPN**, and **Pulse Secure VPN**. Apache mod_proxy request-line injection is CVE-2021-33193.

## Detection & prevention
Prefer HTTP/2 end-to-end (its length framing is unambiguous); avoid downgrading to HTTP/1 back-ends. Normalize ambiguous requests and reject-and-close rather than forward. Never assume a request has no body, strictly validate against the spec, and reject conflicting/duplicate `Content-Length`/`Transfer-Encoding`. Avoid custom HTTP servers. Burp Suite's HTTP Request Smuggler automates discovery.

## Sources
- HTTP Desync Attacks: Request Smuggling Reborn (Kettle, 2019) — https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn
- HTTP/2: The Sequel is Always Worse (Kettle, 2021) — https://portswigger.net/research/http2
- Browser-Powered Desync Attacks (Kettle, 2022) — https://portswigger.net/research/browser-powered-desync-attacks
- Web Security Academy: HTTP request smuggling — https://portswigger.net/web-security/request-smuggling
- HTTP Request Smuggling (Watchfire, 2005) — https://www.cgisecurity.com/lib/HTTP-Request-Smuggling.pdf
- CWE-444: Inconsistent Interpretation of HTTP Requests — https://cwe.mitre.org/data/definitions/444.html

## Related
- [Web-Advanced — Index](kb://11-security-web-advanced-web-advanced-index)
- [Web App Testing](kb://11-security-playbook-web-app-testing)
- [Payload Cheat Sheets — Index](kb://11-security-payloads-payloads-index)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
