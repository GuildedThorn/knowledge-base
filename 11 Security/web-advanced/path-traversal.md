---
summary: "Escaping the intended directory via dot-dot sequences to read or write arbitrary files on the server."
status: active
tags: [security, web, path-traversal, lfi]
private: false
---

# Path Traversal

## Purpose

Escaping the intended directory via dot-dot sequences to read or write arbitrary files on the server.

## How It Works

- An app builds a filesystem path from user input (filename, template name, download param) and fails to constrain it to a base directory.
- The classic payload uses `../` (or `..\` on Windows) sequences to climb out of the intended folder toward `/etc/passwd`, config files, or source code.
- Also known as directory traversal; when it reads and includes files it overlaps with Local File Inclusion (LFI).
- Beyond reads, writable sinks can enable file overwrite, log poisoning, or dropping web shells.

## Bypasses

- Encoding: `%2e%2e%2f`, double-encoding `%252e`, overlong UTF-8, and mixed separators.
- Absolute paths supplied directly (`/etc/passwd`) when the app only strips `../`.
- Null-byte injection (`%00`) in legacy stacks to truncate an appended extension.
- Nested sequences (`....//`) that survive a naive single-pass strip of `../`.

## Defensive Use

- Avoid passing user input to filesystem APIs; map an allowlisted identifier to a known path instead.
- Canonicalize the resolved path (e.g., `realpath`) and verify it still starts with the intended base directory prefix.
- Reject input containing path separators, `..`, or null bytes after decoding.
- Run the service with least-privilege filesystem permissions and a chroot/container boundary.

## Sources

- PortSwigger Web Security Academy - https://portswigger.net/web-security/file-path-traversal
- OWASP Path Traversal - https://owasp.org/www-community/attacks/Path_Traversal

## Related

- [Web Advanced - Index](kb://11-security-web-advanced-web-advanced-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
