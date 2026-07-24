---
title: "HTB Bedsides · 06 · Zip-symlink extraction test"
tags: [htb, web, upload, archive]
verdict: dead-end
---

# 06 · Zip symlink → 🔴 dead end (as tried) / rethink archives

## What I did
- No `zip` binary on box; crafted a zip with a symlink entry (`passwd_link -> /etc/passwd`, unix mode `0o120777`) via `nix-shell -p python3`.
- Uploaded `pass.zip`. Response: `File uploaded successfully: pass.zip`.

## Result
- Archive is **stored, not extracted** on the request: `GET /uploads/pass.zip` = 200, but `/uploads/pass/`, `/uploads/passwd_link`, `/uploads/pass/passwd_link` all **404**.
- Also: Python's own `zipfile.extractall` does **not** recreate symlinks (writes target path as plain text), so even if a Python worker extracts it, a *zip* symlink won't give a read primitive.

## Verdict — 🔴 for this exact attempt
The synchronous upload does not extract. Two live possibilities remain:
1. An **async worker** extracts/converts `/uploads/` contents later (cron/queue). If so, a **tar/tar.gz symlink** (tarfile preserves symlinks) or a malicious convertible file could fire out-of-band. → try tar next.
2. The **conversion step** (ImageMagick/Ghostscript/Pillow) on images/PDF is the real bug (e.g. Ghostscript RCE via crafted PDF, CVE-2023-36664).

→ next: characterise conversion output [[htb-bedsides-07-conversion]]
