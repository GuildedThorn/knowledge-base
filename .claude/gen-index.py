#!/usr/bin/env python3
"""Regenerate INDEX.md and .claude/index.json — a compact catalog of the vault
for an LLM to read *first* (know the whole map in ~1 file), then read_note only
what it needs.

Fields per note: slug (the read_note id), title, folder, status, tags, and a
one-line summary. All are taken from YAML frontmatter when present
(summary/status/tags/title/private) and otherwise derived — so the catalog is
useful today with zero frontmatter and gets sharper as frontmatter is added.

Slug matches vr-brain's VaultParser.Slugify exactly:
    lowercase(relpath without .md), [^a-z0-9]+ -> '-', trimmed.

Run manually (`python3 .claude/gen-index.py`) or let the git pre-commit hook
run it on every commit.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
# Folders that are not knowledge notes — kept out of the catalog.
SKIP_DIRS = {".git", ".obsidian", ".claude", "91 Images", "Postcards"}
INDEX_MD = VAULT / "INDEX.md"
INDEX_JSON = VAULT / ".claude" / "index.json"

FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def slugify(rel_no_ext: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", rel_no_ext.lower()).strip("-") or "note"


def parse_frontmatter(text: str):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm, body = {}, text[m.end():]
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip().lower()] = v.strip().strip("\"'")
    return fm, body


def clean(s: str) -> str:
    s = re.sub(r"\[\[[^\]|]*\|([^\]]+)\]\]", r"\1", s)   # [[a|b]] -> b
    s = re.sub(r"\[\[([^\]]+)\]\]", r"\1", s)            # [[a]]   -> a
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)       # [t](u)  -> t
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)             # **b**   -> b
    s = re.sub(r"[>#*_]+", "", s)                        # stray md marks
    return re.sub(r"\s+", " ", s).strip()


def derive_summary(body: str) -> str:
    lines = body.splitlines()
    # Prefer the first prose line after a "## Purpose"/"## Summary" heading.
    for i, ln in enumerate(lines):
        if re.match(r"^#{1,6}\s+(purpose|summary)\b", ln.strip(), re.I):
            for nxt in lines[i + 1:]:
                if nxt.strip():
                    s = clean(nxt)
                    if s:
                        return first_sentence(s)
            break
    # Otherwise first non-heading, non-callout, non-list content line.
    for ln in lines:
        t = ln.strip()
        if not t or t.startswith(("#", ">", "|", "-", "*", "`")):
            continue
        s = clean(t)
        if s:
            return first_sentence(s)
    return ""


def first_sentence(s: str, limit: int = 160) -> str:
    m = re.search(r"(.+?[.!?])(\s|$)", s)
    out = m.group(1) if m and len(m.group(1)) <= limit else s
    return (out[: limit - 1] + "…") if len(out) > limit else out


def derive_status(folder: str, body: str) -> str:
    head = body[:400].lower()
    if folder == "99 Archive":
        return "archived"
    if "superseded" in head or "[!warning] archived" in head:
        return "superseded"
    if folder == "00 Inbox":
        return "inbox"
    if folder == "90 Templates":
        return "template"
    if folder == "Briefings":
        return "log"
    if folder == "08 Improvements" or re.search(r"^\s*-\s*\[ \]", body, re.M):
        return "in-progress"
    return "active"


def top_folder_tag(folder: str) -> str:
    # "05 Network" -> "network"; "07 Projects/vr-brain" -> "projects".
    seg = folder.split("/")[0]
    return re.sub(r"^\d+\s*", "", seg).strip().lower().replace(" ", "-") or "root"


def main() -> int:
    notes = []
    for path in sorted(VAULT.rglob("*.md")):
        rel = path.relative_to(VAULT).as_posix()
        if rel == "INDEX.md" or any(rel.startswith(d + "/") or rel == d for d in SKIP_DIRS):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)
        folder = rel.split("/")[0] if "/" in rel else "(root)"
        tags = [t.strip().strip("[]\"'") for t in fm.get("tags", "").split(",") if t.strip()]
        if not tags:
            tags = [top_folder_tag(folder)]
        notes.append({
            "slug": slugify(rel[:-3]),
            "title": fm.get("title") or path.stem,
            "path": rel,
            "folder": folder,
            "status": fm.get("status") or derive_status(folder, body),
            "tags": tags,
            "summary": fm.get("summary") or derive_summary(body),
        })

    notes.sort(key=lambda n: (n["folder"], n["title"].lower()))
    INDEX_JSON.write_text(json.dumps(notes, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # ---- INDEX.md ----------------------------------------------------------
    from collections import Counter, defaultdict
    by_status = Counter(n["status"] for n in notes)
    by_folder = defaultdict(list)
    for n in notes:
        by_folder[n["folder"]].append(n)

    out = []
    out.append("<!-- AUTO-GENERATED by .claude/gen-index.py — DO NOT EDIT BY HAND. -->")
    out.append("<!-- Regenerated on every commit (git pre-commit hook). -->\n")
    out.append("# Vault Index\n")
    out.append("A one-file catalog of every note. **Read this first** to see the whole "
               "vault, then `read_note` the `slug` of only what you need — no folder scans.\n")
    out.append(f"- **{len(notes)} notes** · "
               + " · ".join(f"{k}: {v}" for k, v in sorted(by_status.items())))
    out.append("- Status: `active` (current) · `in-progress` (open work) · `log` · "
               "`inbox` · `template` · `superseded`/`archived` (history — usually skip).\n")

    for folder in sorted(by_folder):
        out.append(f"## {folder}\n")
        for n in by_folder[folder]:
            tag = f" _#{n['tags'][0]}_" if n["tags"] else ""
            summ = f" — {n['summary']}" if n["summary"] else ""
            out.append(f"- `{n['slug']}` · **{n['title']}** · {n['status']}{tag}{summ}")
        out.append("")

    INDEX_MD.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"gen-index: {len(notes)} notes -> INDEX.md + .claude/index.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
