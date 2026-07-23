#!/usr/bin/env python3
"""One-time backfill: prepend `summary`/`status`/`tags` frontmatter to every
vault note that doesn't already have a frontmatter block. Idempotent — notes
that already start with `---` are left untouched, so it's safe to re-run.

summary  <- first `## Purpose`/`## Summary` line (cleaned), else first prose line
status   <- judged from folder + markers (active/in-progress/archived/…)
tags     <- folder facet (+ host/project facet where obvious)
"""
from __future__ import annotations
import re, sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".obsidian", ".claude", "91 Images", "Postcards"}


def slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "note"


def clean(s: str) -> str:
    s = re.sub(r"\[\[[^\]|]*\|([^\]]+)\]\]", r"\1", s)
    s = re.sub(r"\[\[([^\]]+)\]\]", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"[>#*_]+", "", s)
    return re.sub(r"\s+", " ", s).strip()


def first_sentence(s: str, limit: int = 160) -> str:
    m = re.search(r"(.+?[.!?])(\s|$)", s)
    out = m.group(1) if m and len(m.group(1)) <= limit else s
    return (out[: limit - 1] + "…") if len(out) > limit else out


def derive_summary(body: str) -> str:
    lines = body.splitlines()
    for i, ln in enumerate(lines):
        if re.match(r"^#{1,6}\s+(purpose|summary)\b", ln.strip(), re.I):
            for nxt in lines[i + 1:]:
                if nxt.strip():
                    s = clean(nxt)
                    if s:
                        return first_sentence(s)
            break
    for ln in lines:
        t = ln.strip()
        if not t or t.startswith(("#", ">", "|", "-", "*", "`")):
            continue
        s = clean(t)
        if s:
            return first_sentence(s)
    return ""


def derive_status(folder: str, title: str, body: str) -> str:
    head = body[:400].lower()
    if "superseded" in head or "[!warning] archived" in head:
        return "superseded"
    if folder == "99 Archive":
        return "archived"
    if folder == "00 Inbox":
        return "inbox"
    if folder == "90 Templates":
        return "template"
    if folder == "Briefings" or title.lower().endswith("log"):
        return "log"
    if folder == "08 Improvements":
        return "in-progress"
    return "active"


def derive_tags(rel: str, folder: str, title: str) -> list[str]:
    low = title.lower()
    if folder == "02 Systems":
        return ["systems", "host"] if "host" in low else ["systems"]
    if folder.startswith("07 Projects") and "/" in rel:
        return ["projects", slugify(rel.split("/")[1])]
    facet = {
        "01 Maps": "maps", "03 Devices": "devices", "04 Software": "software",
        "05 Network": "network", "06 Reference": "reference",
        "08 Improvements": "improvements", "09 Observability": "observability",
        "10 Hobbies": "hobbies", "90 Templates": "templates",
        "99 Archive": "archive", "00 Inbox": "inbox", "Briefings": "briefing",
    }.get(folder, "root")
    return [facet]


def yaml_summary(s: str) -> str:
    # Quote if it contains YAML-significant characters.
    return f'"{s}"' if re.search(r'[:#\[\]{}",]', s) else s


def main() -> int:
    changed = skipped = 0
    for path in sorted(VAULT.rglob("*.md")):
        rel = path.relative_to(VAULT).as_posix()
        if rel == "INDEX.md" or any(rel == d or rel.startswith(d + "/") for d in SKIP_DIRS):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if text.lstrip().startswith("---"):
            skipped += 1
            continue
        folder = rel.split("/")[0] if "/" in rel else "(root)"
        summary = derive_summary(text)
        status = derive_status(folder, path.stem, text)
        tags = derive_tags(rel, folder, path.stem)
        fm = "---\n"
        if summary:
            fm += f"summary: {yaml_summary(summary)}\n"
        fm += f"status: {status}\n"
        fm += f"tags: [{', '.join(tags)}]\n"
        fm += "---\n\n"
        path.write_text(fm + text.lstrip("\n"), encoding="utf-8")
        changed += 1
    print(f"add-frontmatter: {changed} notes updated, {skipped} already had frontmatter")
    return 0


if __name__ == "__main__":
    sys.exit(main())
