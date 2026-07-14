## Purpose

Document the architecture, runtime dependencies, and deployment shape of the `GuildedThorn.com` project, now checked out at `~/Documents/GuildedThorn.com` (moved from `~/Downloads/GuildedThorn.com-main`).

## Summary

GuildedThorn.com is a personal portfolio and platform project built as:

- an ASP.NET Core **`net10.0`** backend (upgraded from net9.0)
- a React 19 + TypeScript + Vite 6 + Tailwind CSS 4 + React Router 7 frontend
- MongoDB-backed application data, now with S3-compatible object storage (SeaweedFS) for gallery images and radio recordings
- JWT cookie-based authentication, now with WebAuthn/FIDO2 passkey and security-key login as well
- SignalR for live chat and radio now-playing updates
- RabbitMQ for guestbook message publishing
- Web Push (VAPID) notifications
- Loki/Serilog for application logging
- GitHub: [GuildedThorn/GuildedThorn.com](https://github.com/GuildedThorn/GuildedThorn.com)

## Repo Layout

- `Program.cs`: backend entrypoint and service registration
- `Controllers/`: API controllers for auth, WebAuthn, blog, chat, contact, donations, gallery, GitHub, guestbook, knowledge base, push notifications, radio, sitemap, Spotify, stream schedule, and user data
- `Services/`: MongoDB, RabbitMQ, SignalR hub(s), chat moderation, donations, gallery/S3 storage, knowledge-base sync engine, push notifications, radio, and WebAuthn challenge storage
- `Models/`: backend data models and request payload types
- `Resources/config.json`: additional runtime configuration
- `GuildedThorn.com-Frontend/`: separate Vite frontend application
- `Tests/`: xUnit unit tests plus Testcontainers integration tests (auto-skip without Docker)
- `dev/up.sh` / `dev/down.sh` / `dev/seed.js`: local dev environment — spins up Mongo + RabbitMQ containers and seeds test data
- `Dockerfile`: multi-stage build for frontend + backend container image
- `flake.nix`: Nix dev shell, and also exposes a `nixosModules.default` providing `services.guildedthorn` — this is how the site is actually deployed in [[02 Systems/NixOS - Host websites|the `websites` NixOS host]]

## Major Features

- portfolio landing page with personal profile and hardware setup content
- GitHub profile and pinned project data
- Spotify top artists integration
- Twitch stream page and a stream schedule feature
- ThornNet network visualization page
- chat/radio functionality using SignalR, with a full Icecast-relay radio implementation (archive/replay of past broadcasts, recording)
- guestbook system with chat moderation (bans, anti-raid, slow mode)
- blog system with upload flow
- gallery system backed by S3-compatible object storage
- contact form and a donations feature
- **knowledge-base sync**: mirrors this very Obsidian vault (`GuildedThorn/knowledge-base`) into MongoDB as browsable public notes — parses frontmatter, `[[wikilinks]]`, and `![[image embeds]]`, polls the repo every 5 minutes by default
- WebAuthn/FIDO2 passwordless login and optional security-key 2FA on top of password auth
- Web Push (VAPID) browser notifications
- user registration, login, and profile update features
- small browser-side utility pages like pomodoro, regex testing, lorem ipsum, color conversion, and UUID generation

## Runtime Dependencies

- ASP.NET Core 10 SDK
- React 19 / Vite 6 / Bun
- MongoDB
- S3-compatible object storage (SeaweedFS in production)
- RabbitMQ
- Loki
- HTTPS for auth cookie flow
- Web Push / VAPID keys, WebAuthn relying-party config

## Related

- [[GuildedThorn.com - Backend|GuildedThorn.com - Backend]]
- [[GuildedThorn.com - Frontend|GuildedThorn.com - Frontend]]
- [[GuildedThorn.com - API and Services|GuildedThorn.com - API and Services]]
- [[GuildedThorn.com - Deployment|GuildedThorn.com - Deployment]]
- [[02 Systems/NixOS - Host websites|Host websites]]
