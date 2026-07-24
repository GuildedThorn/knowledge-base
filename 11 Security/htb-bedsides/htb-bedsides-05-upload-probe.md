---
title: "HTB Bedsides · 05 · Upload behaviour + /uploads/ path"
tags: [htb, web, upload]
verdict: could-go-somewhere
---

# 05 · Upload behaviour — 🟢 could go somewhere

## Tests
- Uploaded a crafted PDF (`uploadFile=@test.pdf`, multipart POST to `/`).
- Response: **`File uploaded successfully: test.pdf`** (original filename echoed; no extracted text returned inline).

## Where files land
- Dir fuzz on research vhost → **`/uploads/`** (403, listing blocked) and `/javascript` (alias).
- **`GET /uploads/test.pdf` → 200.** Uploaded files are served back by their original name, even though directory listing is forbidden.

## Why this matters
Files are both **written server-side and retrievable by name**. So any server-side processing that produces or references a file we can name becomes readable. This turns the "archive" + "conversion" features into a file-read primitive:
- Zip containing a **symlink** → if extracted preserving the link, `GET /uploads/<linkname>` may serve the link target (e.g. `/etc/passwd`, SSH keys, app source).
- Zip-slip `../` → write outside /uploads.

## Verdict — 🟢
Test symlink-in-zip extraction next.

→ next: [[htb-bedsides-06-zip-symlink]]
