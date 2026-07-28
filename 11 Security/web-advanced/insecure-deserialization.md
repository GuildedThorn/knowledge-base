---
summary: Deserializing attacker-controlled data lets adversaries tamper with object attributes or chain existing "gadget" methods across dependencies into remote code execution, spanning Java, PHP, Python, .NET and Ruby.
status: active
tags: [security, web, insecure-deserialization, appsec]
private: false
---

# Insecure Deserialization

Insecure deserialization occurs when user-controllable data is deserialized by an application, letting attackers manipulate serialized objects and inject malicious data. As OWASP states, it is not possible to securely deserialize untrusted input.

## The vulnerability
Serializers rebuild objects from a byte/text stream, often via reflection that bypasses constructors and validation. Native formats (Java `ObjectInputStream`, PHP `unserialize()`, Python `pickle`, Ruby `Marshal`, .NET `BinaryFormatter`) instantiate arbitrary attacker-chosen types and auto-invoke "magic methods" during reconstruction. The huge dependency surface of modern apps means dangerous method combinations almost always exist. Misplaced trust in post-deserialization validation (too late) and in binary formats being tamper-proof compounds the risk.

## Exploitation techniques
- **Attribute/type tampering:** flip a serialized `isAdmin` boolean, or abuse PHP loose comparison (`0 == "password"`) for auth bypass and privilege escalation.
- **Magic methods as kick-off gadgets:** PHP `__wakeup()`/`__destruct()`, Java `readObject()`, Python `__reduce__()`.
- **Gadget chains:** link existing library methods (a kick-off gadget through to a `Runtime.exec()` sink) for RCE. Pre-built chains ship in **ysoserial** (Java: CommonsCollections1-7, Spring, Groovy, Hibernate, ROME, JRMPClient/URLDNS) and **PHPGGC** (PHP). Apache Commons Collections `InvokerTransformer` is the classic gadget.
- **PHAR deserialization:** the `phar://` wrapper implicitly deserializes manifest metadata during filesystem ops like `file_exists()`.

## Real-world cases (sourced)
- **CVE-2015-4852** — Oracle WebLogic T3 protocol (port 7001) RCE via Apache Commons Collections; FoxGlove Security showed the same class hit WebSphere, JBoss, Jenkins, OpenNMS. Blacklist patches were repeatedly bypassed (CVE-2017-3248, CVE-2018-2628).
- **CVE-2019-18935** — Telerik UI for ASP.NET AJAX (CVSS 9.8, CISA/NSA routinely-exploited). `RadAsyncUpload` insecurely deserializes `rauPostData` via `JavaScriptSerializer`; attacker specifies a `System.Configuration.Install.AssemblyInstaller` gadget to load an uploaded mixed-mode DLL, running code as `w3wp.exe`. Chains with CVE-2017-11317 (hard-coded default key).

## Detection & prevention
Never deserialize untrusted data; prefer pure data formats (JSON/XML with `json_decode`, `safe_load`). If unavoidable: cryptographically sign payloads and reject unsigned; enforce allowlists via `ObjectInputStream.resolveClass()` look-ahead, JEP 290 filters, or custom .NET `SerializationBinder`. Ban `BinaryFormatter`; set Json.NET `TypeNameHandling = None`. Tooling: ysoserial, Serianalyzer (static), SerialKiller/rO0 agents, Burp SuperSerial/JavaSerialKiller. Detect Python pickle by base64 prefix `gASV`.

## Sources
- Insecure deserialization — https://portswigger.net/web-security/deserialization
- Exploiting insecure deserialization — https://portswigger.net/web-security/deserialization/exploiting
- OWASP Deserialization Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html
- ysoserial (Chris Frohoff) — https://github.com/frohoff/ysoserial
- Serialization and deserialization in Java (Snyk) — https://snyk.io/blog/serialization-and-deserialization-in-java/
- CVE-2019-18935 Telerik UI RCE (Bishop Fox) — https://bishopfox.com/blog/cve-2019-18935-remote-code-execution-in-telerik-ui

## Related
- [Web-Advanced — Index](kb://11-security-web-advanced-web-advanced-index)
- [Web App Testing](kb://11-security-playbook-web-app-testing)
- [Payload Cheat Sheets — Index](kb://11-security-payloads-payloads-index)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
