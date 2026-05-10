## Purpose

Describe the ASP.NET Core backend structure for GuildedThorn.com.

## Stack

- `ASP.NET Core` on `net9.0`
- JWT bearer authentication with cookie token transport
- MongoDB for persistent application data
- SignalR for live chat
- RabbitMQ for guestbook message publishing
- Serilog with console and Grafana Loki sinks
- Swagger in development

## Entry Point

`Program.cs` sets up:

- `.env` loading through `DotNetEnv`
- config loading from `Resources/config.json` and environment variables
- Serilog logging
- JWT signing and validation
- CORS policy named `AllowFrontend`
- controllers, Swagger, SignalR, and custom services
- static file serving plus SPA fallback to `index.html`

## Data Stores

MongoDB collections exposed by `MongoDbService`:

- `Users`
- `Messages`
- `GuestBookMessages`
- `BlogPosts`
- `GalleryImages`

Other backend integrations:

- RabbitMQ queue: `guestbook_messages`
- Loki log sink URI from configuration

￼￼Purpose

Track plugins, sync decisions, workflow habits, and vault conventions.

￼￼￼Related

- ￼￼￼￼￼￼Software Map￼￼
- ￼￼￼￼￼￼Setup Note Template￼￼
## Authentication Model

- login validates credentials against MongoDB
- passwords are stored as BCrypt hashes
- JWT tokens are issued by the backend
- the JWT is stored as an `HttpOnly`, `Secure`, `SameSite=Strict` cookie named `token`
- bearer auth also reads the token from the cookie in `OnMessageReceived`
- authorization uses both roles and a `PrivilegedOnly` policy

## Key Controllers

- `AuthController`: register, login, logout, auth check, current-user lookup
- `BlogController`: list, fetch, create, and update blog posts
- `GalleryController`: paginated image metadata, upload, delete, file write to `wwwroot/images/gallery`
- `GithubController`: GitHub profile data and pinned project data proxy endpoints
- `GuestBookController`: one message per authenticated user and RabbitMQ publish on create
- `SpotifyController`: Spotify OAuth callback plus top-artist fetch
- `UserController`: current user data and profile update
- `ChatController`: simple controller-side message broadcast

## Notes

- SignalR hub authorization is enforced on `ChatHub`.
- `ChatService` creates a TTL index to expire chat messages after 30 days.
- `RadioController` and `RadioService` are currently mostly placeholders.

## Related

- [[GuildedThorn.com - Overview|GuildedThorn.com]]
- [[GuildedThorn.com - API and Services|GuildedThorn.com - API and Services]]
- [[GuildedThorn.com - Deployment|GuildedThorn.com - Deployment]]
