---
summary: Record how ThornixOS hosts get built and deployed now that the repo has moved to GitOps.
status: active
tags: [systems, host]
---

## Purpose

Record how ThornixOS hosts get built and deployed now that the repo has moved to GitOps.

## Deployment Model: comin

Every host runs [comin](https://github.com/nlewo/comin), watching the `ThornixOS` repo's `main` branch. There is no push-based deploy step and no SSH-from-CI:

1. A change is committed and pushed to `main`.
2. Each host's `comin` agent pulls the new commit.
3. `comin` builds that host's own `nixosConfigurations.<hostname>` and switches to it if the build succeeds.
4. Activation is diff-based — a commit that doesn't touch a given host's closure is a no-op for it, and a failed build leaves the previous generation running.

This replaces the old `bin/rebuild-deploy` + `current-user.lock`/`current-host.lock` + top-level `Makefile` (`make import`/`check`/`backup`/`revert`/`install`) workflow entirely. That tooling no longer exists in the repo.

## Bootstrapping a New Host

A host only needs one manual rebuild, to get `comin` itself running:

```sh
nixos-rebuild switch --flake github:GuildedThorn/ThornixOS#<host>
```

After that, `comin` owns the host and future changes ship by pushing to `main`.

## Deploying a GuildedThorn.com Update

Because the site enters the flake as the `guildedthorn-com` input, shipping a new site build is a lock-file bump, not a host change:

```sh
nix flake update guildedthorn-com
git commit flake.lock -m "chore: bump guildedthorn-com"
git push   # comin on `websites` picks it up within about a minute
```

Only `guildedthorn.service` restarts on the `websites` host; other services there are untouched.

## CI

`.github/workflows/ci.yml` runs `nix flake check` and dry-run-builds every host's toplevel on each push/PR — this is the pre-merge safety net now that there's no local `make check` drift comparison.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Repository Layout|Repository Layout]]
- [[02 Systems/NixOS - Flake Structure|Flake Structure]]
- [[GuildedThorn.com - Deployment|GuildedThorn.com - Deployment]]
