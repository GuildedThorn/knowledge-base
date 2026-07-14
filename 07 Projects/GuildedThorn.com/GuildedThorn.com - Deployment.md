## Purpose

Document how GuildedThorn.com is developed, built, containerized, and actually deployed in production.

## Local Development

The repo includes a Nix dev shell in `flake.nix` (now `.NET SDK 10.0`) with `git`, `nuget`, `bind`, `bun`, `nodejs_24`.

`dev/up.sh` / `dev/down.sh` spin up `mongo:8` and `rabbitmq:4-management` containers, generate a dev `.env`, and `dev/seed.js` seeds an `owner` test user plus sample data — this local dev workflow did not exist in the previous version of this note.

The backend project file also declares SPA dev integration:

- SPA root: `GuildedThorn.com-Frontend/`
- SPA proxy URL: `https://localhost:5173`
- SPA launch command: `bun run dev`

## Build Shape

1. The frontend is built with Bun and Vite.
2. Vite outputs the static bundle into the backend `wwwroot`.
3. The backend serves those assets as static files.
4. ASP.NET Core falls back to `index.html` for SPA routing.

## Testing

`Tests/` now holds xUnit unit tests plus Testcontainers-based integration tests (auto-skip when Docker isn't available); the frontend has Vitest + Testing Library. CI builds and tests both halves.

## Dockerfile Flow

Multi-stage build (now on **.NET 10**, not 9):

1. `frontend-builder` (`oven/bun`) — installs frontend deps, builds the Vite app
2. `build` (`mcr.microsoft.com/dotnet/sdk:10.0`) — restores/builds the backend, copies frontend build artifacts into `wwwroot`
3. `publish` — runs `dotnet publish`
4. `final` (`mcr.microsoft.com/dotnet/aspnet:10.0`) — exposes port `8080`, runs `dotnet GuildedThorn.com.dll`

## Actual Production Deployment: NixOS, Not Just Docker

This note previously only covered the Docker build; the real production path is a NixOS module. The flake exposes `nixosModules.default`, providing `services.guildedthorn` (`DynamicUser`, a `StateDirectory` for persistent gallery/upload state). This module is consumed as the `guildedthorn-com` flake input in the `ThornixOS` repo and deployed to the `websites` NixOS host — see [[02 Systems/NixOS - Host websites|Host websites]].

Shipping a new version in production is a flake-lock bump in `ThornixOS`, not a manual container push:

```sh
nix flake update guildedthorn-com
git commit flake.lock -m "chore: bump guildedthorn-com"
git push   # comin on the websites host picks it up within ~a minute
```

Only `guildedthorn.service` restarts; Owncast and RabbitMQ on that host are untouched. See [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]] for the general `comin` GitOps flow.

## Runtime Expectations

- ASP.NET Core listens on `http://+:8080` in both the container and the NixOS service
- the `websites` host fronts the app with a Cloudflare Tunnel (outbound-only; only SSH is exposed on the public interface otherwise) rather than a locally-terminated reverse proxy
- the app requires external configuration for JWT, Fido2, MongoDB, RabbitMQ, Spotify, Web Push, and Loki, provided via a sops-managed environment file on the `websites` host

## Related

- [[GuildedThorn.com - Overview|GuildedThorn.com]]
- [[GuildedThorn.com - Backend|GuildedThorn.com - Backend]]
- [[GuildedThorn.com - API and Services|GuildedThorn.com - API and Services]]
- [[02 Systems/NixOS - Host websites|Host websites]]
