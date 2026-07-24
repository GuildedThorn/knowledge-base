---
title: "HTB Bedsides · 04 · research.bedside.htb upload portal"
tags: [htb, web, upload, pdfminer]
verdict: could-go-somewhere
---

# 04 · `research.bedside.htb` — file-upload portal — 🟢 HOT

## Findings
- Title: **Bedside Research Portal**. Response header **`X-Powered-By: pdfminer.six`** → Python backend using pdfminer.six for PDF text extraction.
- POST multipart form, field **`uploadFile`**, no auth.
- Accepted formats: **jpeg, jpg, png, bmp, tiff, dcm, pdf**.
- Notice: *"Collections can be uploaded as **archives**."*
- Notice: *"Certain file formats may be **converted to standardized formats** before being used for AI training."*

## Candidate attack surfaces (ranked)
1. 🟢 **Archive upload → zip-slip / symlink read.** "Archives" extracted server-side; a symlink or `../` path inside a zip could read arbitrary files (SSH keys, app source, /etc/passwd) or write outside the upload dir.
2. 🟢 **Image conversion RCE/SSRF.** "converted to standardized formats" = ImageMagick/Pillow. tiff/dcm/svg conversion → ImageTragick-style or malicious-file parsing.
3. 🟢 **DICOM (.dcm) parsing** — niche parser, possible bugs.
4. 🟡 **pdfminer.six parsing** — extracts text from uploaded PDF and (likely) returns it. Check version for CVEs; also a channel to read what the server does with our file.

## Verdict — 🟢 primary path
This portal is the foothold vector. Next: observe how an upload responds (does it echo extracted text? a saved path?), then test archive/symlink and image-conversion angles.

→ next: [[htb-bedsides-05-upload-probe]]
