---
summary: "Exploiting native Java object deserialization with gadget chains to achieve remote code execution."
status: active
tags: [security, web, deserialization, gadget-chain, rce]
private: false
---

# Java Insecure Deserialization

## Purpose

Exploiting native Java object deserialization with gadget chains to achieve remote code execution.

## How It Works

- `ObjectInputStream.readObject()` reconstructs arbitrary object graphs from a serialized byte stream, invoking class logic before the application inspects the result.
- Any class on the classpath implementing `Serializable` is a candidate; the deserializer resolves types purely from the stream's declared class names.
- A gadget chain stitches together the magic methods (`readObject`, `readResolve`, `finalize`, or proxy `invoke`) of benign library classes so that reconstruction ends in a dangerous call such as `Runtime.exec` or reflection.
- The magic bytes `AC ED 00 05` (or base64 `rO0`) signal a Java serialized stream and are a useful hunt indicator in traffic.

## Engineering Notes

- `ysoserial` generates ready-made payloads for chains in common libraries (Commons Collections, Spring, Groovy, JRMP), turning an exposed sink into RCE.
- Primary defenses: avoid native serialization for untrusted input; use a look-ahead `ObjectInputStream` that rejects unknown classes before instantiation.
- Enforce a strict allowlist via `ObjectInputFilter` (JEP 290) rather than a blocklist, which chain authors routinely bypass.
- Prefer data-only formats (JSON, Protobuf) with schema validation; keep gadget libraries patched and off the classpath where possible.

## Sources

- OWASP Deserialization Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html
- ysoserial - https://github.com/frohoff/ysoserial
- PortSwigger Web Security Academy - https://portswigger.net/web-security/deserialization

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
