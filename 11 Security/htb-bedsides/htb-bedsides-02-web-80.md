---
title: "HTB Bedsides · 02 · Web root (port 80)"
tags: [htb, web, recon]
verdict: rabbit-hole
---

# 02 · Homepage `http://bedside.htb/` — 🐇 rabbit hole (but thematic clue)

Curl with `--resolve bedside.htb:80:10.129.66.223` (host file is read-only on this NixOS box; `--resolve`/`-H Host:` used throughout).

## Result

- **200 OK**, Apache 2.4.68. Single-page static "Bedside Clinic" cardiology marketing site.
- Only in-page anchor links: `#about #treatments #ai #contact`. **No real routes, no forms, no JS app.**
- Contact: `contact@bedside.htb`.
- **Heavy "AI" theming** — whole section on "Artificial Intelligence in Heart Care", predictive modelling, chatbots-adjacent language.

## Verdict — 🐇 / clue

The page body itself is a dead end (static HTML, nothing to attack). **But** the AI theme + the **filtered port 3000** strongly suggests an AI/LLM web app (Open-WebUI / Ollama / LibreChat / Gitea are common on :3000). That's the real target.

→ next: fuzz vhosts + dirs [[htb-bedsides-03-fuzzing]]; keep port 3000 parked as 🟢 [[htb-bedsides-01-nmap]].
