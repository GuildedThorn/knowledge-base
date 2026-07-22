## Purpose

Document how the `ThornixOS` repo is structured so it is easier to find shared modules, per-host config, and secrets.

## Scope

This note reflects the repo at `~/Documents/ThornixOS` (GitHub: `GuildedThorn/ThornixOS`). This replaces the old `/run/media/thorn/NIX_CONFIG/nix-config` layout entirely — that Makefile/lock-file scheme is gone.

## Identity

ThornixOS is the name of the repo itself, not a distinct OS distribution — per its own README: "my nix config, dont mind the name, a friend thought it was funny."

## Layout

The flake uses [flake-parts](https://github.com/hercules-ci/flake-parts) + [import-tree](https://github.com/vic/import-tree) (the "dendritic" pattern):

- `flake.nix` holds only inputs; `outputs = import-tree ./modules`.
- Every `.nix` file under `modules/` is auto-imported as a flake-parts module. Nothing is wired up by path — each file contributes either a named piece (`config.nixos.modules.<name>`) or a whole host (`flake.nixosConfigurations.<name>`).
- `modules/computers/<host>.nix`: one file per host, composes named modules plus that host's `hosts/<host>/` files into a `nixosConfigurations.<host>`.
- `modules/core/`: base config, the `thorn-core` bundle, and module-plumbing files (`base.nix`, `files.nix`, `home-manager-modules.nix`, `nixos-modules.nix`, `thorn-core.nix`).
- `modules/desktop/`, `modules/graphics/`, `modules/processor/`, `modules/services/`, `modules/apps/`, `modules/users/`, `modules/home-manager/`: reusable named modules (see [[02 Systems/NixOS - Shared Modules|Shared Modules]]).
- `hosts/<host>/`: per-host data — `hardware-configuration.nix`, `disko.nix` where used, `networking.nix`, `home.nix` where a host has a Home Manager overlay, and `secrets.nix` + `secrets.yaml` (sops) where a host has secrets.
- `certs/`: checked-in (non-secret) certificates — `ThornCloud_CA.crt` (internal CA) and `proxmox.guildedthorn.arpa.crt`.
- `programs/`: standalone application source/config trees rather than Home Manager modules — now only `clonehero/clonehero.nix` (packaging/config). The `ags/` and `eww/` widget trees were deleted along with their unused `astal`/`ags` flake inputs.
- `.sops.yaml`: sops recipient/creation-rule declarations (see [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]).
- `.github/workflows/ci.yml`: runs `nix flake check` and dry-run-builds every host's toplevel on push/PR.

## How Composition Works

1. `flake.nix` inputs feed `import-tree ./modules`, which auto-registers every module file.
2. `modules/computers/<host>.nix` lists the named modules that host wants (e.g. `config.nixos.modules.desktop-hyprland`, `config.nixos.modules.services-ssh`) plus its `hosts/<host>/` data files.
3. Deployment is not path-based rebuild-and-copy — see [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]] for the `comin` GitOps flow that replaced it.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Flake Structure|Flake Structure]]
- [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
