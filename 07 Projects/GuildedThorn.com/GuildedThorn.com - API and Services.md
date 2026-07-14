## Purpose

Provide a compact API and integration reference for GuildedThorn.com.

## HTTP API Surface

### Auth

- `GET /api/auth/me`
- `GET /api/auth/check`
- `POST /api/auth/login`
- `POST /api/auth/register`
- `POST /api/auth/logout`
- `GET /api/auth/user/{id}`

### WebAuthn

- passkey/security-key registration and assertion endpoints on `WebAuthnController` (challenge issued via `WebAuthnChallengeStore`)

### Blog

- `GET /api/blog/getPosts?page=&pageSize=`
- `GET /api/blog/{id}`
- `POST /api/blog`
- `PUT /api/blog/{id}`

### Gallery

- `GET /api/gallery/getImages?page=&pageSize=`
- `GET /api/gallery/{id}`
- `POST /api/gallery`
- `DELETE /api/gallery/{id}`

### GitHub

- `GET /api/Github/getInfo`
- `GET /api/Github/getProjects`

### Guestbook

- `POST /api/GuestBook/message`
- `GET /api/GuestBook/getGuestBookMessages?page=&pageSize=`

### Spotify

- `GET /api/spotify/login`
- `GET /api/spotify/callback`
- `GET /api/spotify/top-artists`

### User

- `GET /api/User/me`
- `PATCH /api/User/updateData`

### Chat

- `POST /api/Chat/send`
- SignalR hub: `/chathub`

### Radio

- Icecast relay/status and archive endpoints on `RadioController`
- SignalR hub for now-playing updates

### Knowledge Base

- paginated/searchable/tag-filterable public notes endpoint on `KnowledgeBaseController`
- owner-only manual sync trigger

### Contact, Donations, Push, Sitemap, Stream Schedule

- form/data endpoints on `ContactController`, `DonationsController`, `PushController`, `SitemapController`, `StreamScheduleController`

## External Service Dependencies

- GitHub API for profile data
- `pinned.berrysauce.dev` for pinned repository data
- Spotify Accounts and Web API
- Twitch embed script on the stream page
- Icecast status JSON for radio metadata
- MongoDB for persistent storage
- S3-compatible object storage (SeaweedFS) for gallery images and radio recordings
- RabbitMQ for guestbook event publishing
- Grafana Loki for logs
- Web Push (VAPID) for browser notifications
- the public `GuildedThorn/knowledge-base` git repo, mirrored via LibGit2Sharp

## Required Configuration Areas

The code expects configuration for:

- `Jwt:Key`, `Jwt:Issuer`, `Jwt:Audience`
- `Fido2:ServerDomain`, `Fido2:Origins`
- `MongoDB:ConnectionString`, `MongoDB:DatabaseName`
- `RabbitMQ:HostName`, `RabbitMQ:Username`, `RabbitMQ:Password`
- `Spotify:ClientId`, `Spotify:ClientSecret`, `Spotify:RedirectUri`
- `WebPush:PublicKey`, `WebPush:PrivateKey`, `WebPush:Subject`
- `KnowledgeBase:PollIntervalMinutes`
- `Loki:Uri`

## Operational Notes

- `Resources/config.json` holds non-secret runtime config; secrets/connection strings come from environment variables (production) or `dev/up.sh`-generated `.env` (local dev).
- Gallery uploads and radio recordings are written to S3-compatible storage, not local `wwwroot`.

## Related

- [[GuildedThorn.com - Overview|GuildedThorn.com]]
- [[GuildedThorn.com - Backend|GuildedThorn.com - Backend]]
- [[GuildedThorn.com - Deployment|GuildedThorn.com - Deployment]]
