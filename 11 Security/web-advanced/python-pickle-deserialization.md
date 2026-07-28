---
summary: "Arbitrary code execution from unpickling untrusted data via the __reduce__ object-reconstruction hook."
status: active
tags: [security, web, pickle, deserialization, python]
private: false
---

# Python Pickle Deserialization

## Purpose

Arbitrary code execution from unpickling untrusted data via the `__reduce__` object-reconstruction hook.

## How It Works

- `pickle.load`/`loads` executes a small stack-based virtual machine (opcodes like `GLOBAL`, `REDUCE`) that can import arbitrary modules and call callables during unpickling.
- A class defining `__reduce__` returns a callable and its arguments; the unpickler invokes that callable, so `(os.system, ("cmd",))` yields command execution.
- Execution happens as objects are reconstructed, before any application code sees the result, so validating the output afterward provides no protection.
- The same risk applies to `pickle`-backed formats and libraries: `shelve`, `joblib`, unsafe PyTorch `torch.load` checkpoints, and some caching layers.

## Security Notes

- Never unpickle data from an untrusted or unauthenticated source; treat pickle strictly as an internal, trusted-boundary format.
- Use safe serialization for external data: JSON for plain data, or schema-typed formats like Protobuf/MessagePack.
- If pickle is unavoidable, subclass `pickle.Unpickler` and override `find_class` to allowlist a minimal set of module/class names, rejecting everything else.
- Add integrity protection (HMAC over the blob with a secret key) so tampered payloads are rejected before `loads` runs.

## Sources

- Python pickle documentation - https://docs.python.org/3/library/pickle.html
- OWASP Deserialization Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
