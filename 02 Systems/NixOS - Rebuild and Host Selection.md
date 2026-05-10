## Purpose

Record how this repo selects a user/host combination and how it is deployed to `/etc/nixos`.

## Host Selection Model

- `nixos/flake.nix` reads `current-user.lock` for the active primary user and throws if it is missing.
- It reads `current-host.lock` for a single selected host when present.
- If `current-host.lock` does not exist, it builds configs for every host directory under that user.
- The resulting flake output name is the host name, for example `.#scout` or `.#mitm`.

## Primary Workflow

The repo contains `bin/rebuild-deploy`:

```bash
bin/rebuild-deploy <user> <host>
```

That script:

1. Writes the selected user into `/etc/nixos/current-user.lock`.
2. Writes the selected host into `/etc/nixos/current-host.lock`.
3. Changes into `/etc/nixos`.
4. Runs `sudo nixos-rebuild switch --flake /etc/nixos --upgrade`.

## Makefile Workflow

The top-level `Makefile` handles repo-to-system sync:

- `make import` copies the live `/etc/nixos` tree into the local `nixos/` directory.
- `make check` shows drift between local files and `/etc/nixos`.
- `make backup` copies `/etc/nixos` into `/etc/nixos.backups/<timestamp>`.
- `make backups` lists available backups.
- `make revert` restores a backup into `/etc/nixos`.
- `make install` interactively copies changed files into `/etc/nixos`, optionally creating a backup first.

## Operational Notes

- `programs.nh` is enabled in the shared base config and points to `/etc/nixos` as the flake path.
- The local repo and the live `/etc/nixos` tree are separate until `make install` or another copy step is run.
- The rebuild script assumes the flake is already present at `/etc/nixos`.
- Because `current-host.lock` is written into `/etc/nixos`, the flake can resolve the selected host without an explicit `.#<host>` suffix.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Repository Layout|Repository Layout]]
