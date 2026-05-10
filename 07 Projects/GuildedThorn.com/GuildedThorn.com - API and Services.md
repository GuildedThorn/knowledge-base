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

## External Service Dependencies

- GitHub API for profile data
- `pinned.berrysauce.dev` for pinned repository data
- Spotify Accounts and Web API
- Twitch embed script on the stream page
- Icecast status JSON for radio metadata
- MongoDB for persistent storage
- RabbitMQ for guestbook event publishing
- Grafana Loki for logs

## Required Configuration Areas

The code expects configuration for:

- `Jwt:Key`
- `Jwt:Issuer`
- `Jwt:Audience`
- `MongoDB:ConnectionString`
- `MongoDB:DatabaseName`
- `RabbitMQ:HostName`
- `RabbitMQ:Username`
- `RabbitMQ:Password`
- `Spotify:ClientId`
- `Spotify:ClientSecret`
- `Spotify:RedirectUri`
- `Loki:Uri`

## Operational Notes

- `Resources/config.json` currently only shows a Loki URI.
- Additional secrets and connection strings are expected from environment variables or other runtime config injection.
- Gallery uploads write files into `wwwroot/images/gallery`.

## Related

- [[GuildedThorn.com - Overview|GuildedThorn.com]]
- [[GuildedThorn.com - Backend|GuildedThorn.com - Backend]]
- [[GuildedThorn.com - Deployment|GuildedThorn.com - Deployment]]
