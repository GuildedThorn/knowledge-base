## Purpose

Track plugins, sync decisions, workflow habits, and vault conventions for this knowledge base itself.

## Current State

- Home Manager side is minimal: `modules/home-manager/obsidian.nix` just sets `programs.obsidian.enable = true` on all four desktop hosts (`nixos`, `scout`, `mac`, `proxmox-guest`) — no vault path or plugin list is declared in Nix. Vault-level config (`.obsidian/`) is managed inside the vault itself, not through Home Manager.
- Core plugins enabled include Graph view, Backlink, Outgoing Link, Bookmarks, Daily Notes, Templates, Canvas, Bases, Outline, and **Sync** (Obsidian's official paid sync service) — no community plugins are installed as of this pass.
- This vault is also mirrored into [[GuildedThorn.com - Overview|GuildedThorn.com]] via its knowledge-base sync engine, which parses this vault's frontmatter/wikilinks/image-embeds directly — see [[GuildedThorn.com - Backend|GuildedThorn.com - Backend]].

## Related

- [[01 Maps/Software Map|Software Map]]
- [[90 Templates/Setup Note Template|Setup Note Template]]
- [[GuildedThorn.com - Overview|GuildedThorn.com]]
