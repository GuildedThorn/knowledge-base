---
title: "HTB Bedsides · 07 · Traversal + conversion behaviour"
tags: [htb, web, upload, conversion]
verdict: dead-end
---

# 07 · Filename traversal & conversion probing — 🔴 mostly dead

## Filename path traversal — 🔴 dead
- Uploaded with `filename=../trav_9f2a.png`. App takes **basename** → landed at `/uploads/trav_9f2a.png`, not in the parent dir. `/trav_9f2a.png` = 404. Traversal-on-write is sanitized.

## Conversion behaviour — 🔴 no observable output
- Generated valid **BMP, TIFF, PDF** (ImageMagick via `nix-shell -p imagemagick`) and uploaded.
- Polled `/uploads/` for standardized twins (`.png/.jpg/.txt`) over ~48s. **Only the originals appear (200); no converted/extracted output at predictable names.**
- Archives (zip, tar.gz) also never extracted (see [[htb-bedsides-06-zip-symlink]]).

## Interpretation
The advertised "conversion / archive / AI-training" processing is **not triggered synchronously by upload, and not by a fast cron.** Either:
- output names are randomized/hashed (can't poll blindly), or
- processing is gated behind a staff/authenticated action or a slow/again-triggered job, or
- the real bug is reached a different way (the `pdfminer.six` header is a deliberate hint).

## Next moves
- Inspect the **full** upload response body for a convertible input (may embed extracted text / result link) — filtered it out earlier.
- Full 65535-port scan (nmap only did top-1000; :3000 filtered).
- Fuzz research vhost for source/config (`.git`, `app.py`, `index.php`, `robots.txt`).

→ next: [[htb-bedsides-08-deepen]]
