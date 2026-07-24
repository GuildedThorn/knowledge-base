---
title: "HTB Bedsides · 03 · Vhost fuzzing"
tags: [htb, recon, fuzzing, vhost]
verdict: could-go-somewhere
---

# 03 · Vhost brute → `research.bedside.htb` — 🟢 could go somewhere

## Environment note
Box is a minimal nix-shell: **no ffuf/gobuster/feroxbuster and no local wordlists.** Worked around it:
- Pulled `subdomains-top1million-5000.txt` from SecLists via `curl` to `/tmp/subs.txt`.
- Parallel sweep with `xargs -P30` + curl, filtering the `301` baseline (unknown vhosts 301-redirect):

```
cat /tmp/subs.txt | xargs -P30 -I{} sh -c 'c=$(curl -s -o /dev/null -w "%{http_code}:%{size_download}" -H "Host: {}.bedside.htb" http://10.129.66.223/); case "$c" in 301:*) ;; *) echo "$c {}";; esac'
```

## Result

- **`research.bedside.htb` → 200 OK, 3152 bytes.** New virtual host, distinct from the static clinic site.
- Small curated AI-app list (ai/chat/ollama/openwebui/...) all 301 — no hit there.

## Verdict — 🟢

`research.bedside.htb` is the live lead. Given the "AI" theme + filtered :3000, this is likely where the app / login / LLM feature lives.

→ next: enumerate research vhost [[htb-bedsides-04-research-vhost]]
