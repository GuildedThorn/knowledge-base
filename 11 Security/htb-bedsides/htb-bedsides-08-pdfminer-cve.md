---
title: "HTB Bedsides · 08 · Foothold vuln = CVE-2025-64512 (pdfminer.six pickle RCE)"
tags: [htb, exploit, pdfminer, cve, rce]
verdict: could-go-somewhere
---

# 08 · Intended foothold identified — 🟢 THE PATH

## What
**CVE-2025-64512 / GHSA-wf5f-4jwr-ppcp** — Arbitrary Code Execution in **pdfminer.six** via crafted PDF.
- pdfminer's `CMapDB` loads CMap resources by name using **Python `pickle`** (cached `.pickle.gz`).
- A **path-traversal in the CMap name** makes it load an attacker-controlled `*.pickle.gz` from an arbitrary path.
- Malicious pickle `__reduce__` → **RCE as the PDF-processing user** when the PDF is parsed.
- (CVE-2025-70559 is the follow-up for the incomplete patch.)

## Why it fits Bedsides perfectly
- Response header **`X-Powered-By: pdfminer.six`** — deliberate hint.
- Upload allow-list includes **`gz`** and **`pdf`** — we upload the compressed pickle *and* the trigger PDF.
- Files are stored at a known path (**`/uploads/<name>`**) → we control the pickle's on-disk location for the CMap traversal to reach.
- Everything routes through :80 (full 65535 scan = 22/80 open, 3000 filtered).

## Box shape (from public writeups, medium)
Double insecure-deserialization chain: pdfminer pickle RCE → shell in a **processing container**; a second deserialization bug on another service → **root on the host**. Port 3000 (filtered) is likely the second-stage service reachable post-foothold.

## Plan
1. Pull exact PoC (CMap traversal string + PDF structure) from advisory.
2. Build malicious `payload.pickle.gz` (`__reduce__` → reverse shell to our tun0).
3. Upload pickle.gz, then upload crafted PDF referencing it via CMap traversal.
4. Catch shell; then pivot to :3000 for root.

→ next: [[htb-bedsides-09-exploit-build]]

## Sources
- https://github.com/advisories/GHSA-wf5f-4jwr-ppcp
- https://www.sentinelone.com/vulnerability-database/cve-2025-64512/
