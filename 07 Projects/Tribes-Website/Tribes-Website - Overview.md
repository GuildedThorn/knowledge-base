## Purpose

Document the architecture and status of the `Tribes-Website` project.

## Summary

Despite the name, this is currently a generic, reusable full-stack starter/boilerplate — not yet a Tribes-specific community site. The README frames it explicitly as "a batteries-included starter for building a SPA-backed web app," with a `Notes` CRUD feature as the reference example to copy when adding real resources. It's built as:

- an ASP.NET Core `net10.0` backend
- a React 19 + TypeScript + Vite + Tailwind CSS frontend
- JWT cookie auth plus WebAuthn passkey/security-key login
- MongoDB for persistent data
- SignalR for realtime sync across tabs
- RabbitMQ (optional — lazy/resilient, no broker required for local dev)
- GitHub: [GuildedThorn/Tribes-Website](https://github.com/GuildedThorn/Tribes-Website)

A `wwwroot/tribes-assets` directory exists but is not yet used by any feature — likely staged art for a future Tribes-specific build-out of this template.

## Repo Layout

- `Program.cs`: app wiring — config, auth, CORS, SignalR, middleware, SPA fallback
- `Controllers/`: `AuthController`, `UserController`, `WebAuthnController`, `NotesController`
- `Services/`: `MongoDbService`, `RabbitMqService`, `JwtTokenService`, `RealtimeHub`, `WebAuthnChallengeStore`
- `Models/`: `User`, `WebAuthnCredential`, `Note`
- `Resources/config.example.json`
- `Tests/`: xUnit unit and integration tests, including `WebAuthnChallengeStoreTests.cs` and `JwtTokenServiceTests.cs`
- `frontend/`: React + Vite + Tailwind, builds into `../wwwroot`, includes a headless-browser smoke test (`bun run smoke`)
- `flake.nix`: Nix dev shell plus `packages.default` and `nixosModules.default`
- `Dockerfile`: multi-stage build
- `.github/workflows`: CI

## Major Features

- JWT cookie auth (register/login/logout) plus WebAuthn passkey/security-key login
- example `Notes` resource wired end-to-end (REST + MongoDB + RabbitMQ publish + live SignalR sync across tabs) — the intended pattern to copy for new resources
- single-origin production deploy: frontend built into `wwwroot` and served by the backend, no CORS needed in prod

## Adding a Feature (documented pattern)

model → `GetXCollection()` helper in `MongoDbService` → controller (`[Authorize(Policy="PrivilegedOnly")]`) → API client in `frontend/src/backend/api.ts` → page + route in `AppRoutes.tsx`.

## Runtime Dependencies

- .NET 10 SDK
- Bun
- MongoDB (required)
- RabbitMQ (optional)
- Grafana Loki (optional)

## Notes

- License is MIT with a placeholder copyright holder — this is a template repo, unlike GuildedThorn.com's all-rights-reserved personal license.
- Dev environment seeds from `.env.example` plus a generated JWT key.

## Related

- [[GuildedThorn.com - Overview|GuildedThorn.com]]
- [[07 Projects/SkyDestroyer/SkyDestroyer - Overview|SkyDestroyer - Overview]]
