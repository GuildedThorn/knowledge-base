## Purpose

Track the NixVim setup managed by `nixos/users/thorn/programs/nixvim/main.nix`.

## Current State

- NixVim is enabled through Home Manager from `nixos/users/thorn/home.nix`.
- Unfree packages are allowed for the NixVim package set.
- Extra editor/runtime packages include `nixd`, `fzf`, `ripgrep`, `fd`, `alejandra`, `stylua`, and `black`.

## Editor Features

- UI/navigation: `barbar`, `lualine`, `neo-tree`, `web-devicons`, `which-key`, `fzf-lua`, `project-nvim`, and `lastplace`.
- Feedback/diagnostics: `fidget`, `trouble`, and `tiny-inline-diagnostic`.
- Git workflow: `fugitive` and `neogit`.
- Completion/snippets: `blink-cmp`, `blink-cmp-git`, `blink-emoji`, `blink-indent`, `luasnip`, and `lspkind`.
- Language tooling: `treesitter` with all grammars, `treesitter-context`, LSP, Conform formatting, Nix helpers, Dotnet support, and `nix-develop`.
- Quality-of-life plugins: `comment`, `cloak`, `sleuth`, and `neocord`.

## LSP Servers

- `pyright`
- `clangd`
- `lua_ls`
- `nil_ls`
- `nixd`
- `ts_ls`
- `rust_analyzer`
- `typos_lsp`
- `intelephense`

## Formatting

Conform is configured to format on save with LSP fallback and a `500ms` timeout.

- Nix: `nixfmt`
- Lua: `stylua`
- Python: `black`

## Nix-Specific Notes

- `nixd` uses `import <nixpkgs> {}` as its nixpkgs expression.
- `nixd` formatting is configured to call `nixpkgs-fmt`, while the Home Manager package list includes `alejandra` and the shared system packages include `nixfmt`.
- This formatter split should be verified so the intended Nix formatter is clear.

## Secret-Handling Notes

- The Intelephense LSP config contains an inline license key in the source file.
- Treat that value as secret or license material and migrate it out of plain config before publishing or wider sharing.

## Related

- [[01 Maps/Software Map|Software Map]]
- [[02 Systems/NixOS - Home Manager Layout|Home Manager Layout]]
