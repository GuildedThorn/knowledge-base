## Purpose

Describe the ASP.NET Core backend structure for GuildedThorn.com.

## Stack

- `ASP.NET Core` on **`net10.0`** (upgraded from net9.0)
- JWT bearer authentication with cookie token transport, plus WebAuthn/FIDO2 (Fido2NetLib) for passkey/security-key login
- MongoDB for persistent application data
- S3-compatible object storage (SeaweedFS) for gallery images and radio recordings, proxied through the app rather than served directly
- SignalR for live chat and radio now-playing updates
- RabbitMQ for guestbook message publishing
- Web Push (VAPID) for browser notifications
- Serilog with console and Grafana Loki sinks
- Swagger in development

## Entry Point

`Program.cs` sets up:

- `.env` loading through `DotNetEnv`
- config loading from `Resources/config.json` and environment variables
- Serilog logging
- JWT signing/validation and WebAuthn relying-party config
- CORS policy named `AllowFrontend`
- controllers, Swagger, SignalR, and custom services
- static file serving plus SPA fallback to `index.html`

## Data Stores

MongoDB collections/models now include: `Users`, `Messages`, `GuestBookMessages`, `BlogPosts`, `Gallery`, `ChatBan`, `ContactMessage`, `Donation`, `DonationSettings`, `Github`, `KnowledgeBaseNote`, `KnowledgeBaseSyncState`, `PushSubscriptionDoc`, `RadioRecording`, `Spotify`, `StreamEvent`, `UserStats`, `WebAuthnCredential` — a large expansion from the original five-collection set.

Other backend integrations:

- RabbitMQ queue: `guestbook_messages`
- Loki log sink URI from configuration
- S3-compatible bucket for gallery/radio-recording storage

## Authentication Model

- login validates credentials against MongoDB; passwords stored as BCrypt hashes
- JWT tokens issued by the backend, stored as an `HttpOnly`, `Secure`, `SameSite=Strict` cookie named `token`; bearer auth also reads the token from the cookie in `OnMessageReceived`
- WebAuthn (`WebAuthnController` + `WebAuthnChallengeStore` + `WebAuthnCredential` model) adds passwordless passkey login and optional security-key 2FA
- authorization uses both roles and a `PrivilegedOnly` policy

## Key Controllers

- `AuthController`: register, login, logout, auth check, current-user lookup
- `WebAuthnController`: passkey/security-key registration and assertion flows
- `BlogController`: list, fetch, create, and update blog posts
- `GalleryController`: paginated image metadata, upload, delete — now via `GalleryStorage`/`S3StorageService` instead of writing to `wwwroot`
- `GithubController`: GitHub profile data and pinned project data proxy endpoints
- `GuestBookController`: one message per authenticated user and RabbitMQ publish on create
- `SpotifyController`: Spotify OAuth callback plus top-artist fetch
- `UserController`: current user data and profile update
- `ChatController`: message broadcast, now backed by `ChatModerationService` (bans, anti-raid, slow mode)
- `ContactController`: contact form submissions
- `DonationsController`: donation intake and settings
- `KnowledgeBaseController`: paginated/searchable/tag-filterable public read endpoint over the synced vault notes, plus an owner-only manual sync trigger
- `PushController`: Web Push (VAPID) subscription management
- `SitemapController`: sitemap generation
- `StreamScheduleController`: stream schedule data
- `RadioController`: now fully implemented — Icecast relay, SignalR now-playing, archive/replay of past broadcasts, recording (previously a placeholder)

## Knowledge-Base Sync

`KnowledgeBaseSyncEngine` uses LibGit2Sharp to mirror the public `GuildedThorn/knowledge-base` Obsidian vault into MongoDB: it parses Obsidian frontmatter, `[[wikilinks]]`, and `![[image embeds]]`, resolves images from `91 Images/`, and explicitly skips vault scaffolding folders. `KnowledgeBaseSyncService` polls the repo every 5 minutes by default (`KnowledgeBase:PollIntervalMinutes`).

## Notes

- SignalR hub authorization is enforced on `ChatHub`; `RadioHub` also exists for now-playing updates.
- `ChatService` creates a TTL index to expire chat messages after 30 days.
- Repo's own `CLAUDE.md` is stale (says net9, calls RadioService a stub) — trust `README.md` over `CLAUDE.md`.

## Related

- [[GuildedThorn.com - Overview|GuildedThorn.com]]
- [[GuildedThorn.com - API and Services|GuildedThorn.com - API and Services]]
- [[GuildedThorn.com - Deployment|GuildedThorn.com - Deployment]]
