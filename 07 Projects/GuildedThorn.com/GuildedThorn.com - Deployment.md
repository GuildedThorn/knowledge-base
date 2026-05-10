## Purpose

Document how GuildedThorn.com is developed, built, and containerized.

## Local Development

The repo includes a Nix dev shell in `flake.nix` with:

- `.NET SDK 9.0`
- `git`
- `nuget`
- `bind`
- `bun`
- `nodejs_24`

The backend project file also declares SPA dev integration:

- SPA root: `GuildedThorn.com-Frontend/`
- SPA proxy URL: `https://localhost:5173`
- SPA launch command: `bun run dev`

## Build Shape

1. The frontend is built with Bun and Vite.
2. Vite outputs the static bundle into the backend `wwwroot`.
3. The backend serves those assets as static files.
4. ASP.NET Core falls back to `index.html` for SPA routing.

## Dockerfile Flow

The Dockerfile uses a multi-stage build:

1. `frontend-builder`
   - based on `oven/bun`
   - installs frontend deps
   - builds the Vite app
2. `build`
   - based on `.NET SDK 9`
   - restores and builds the backend
   - copies frontend build artifacts into `wwwroot`
3. `publish`
   - runs `dotnet publish`
4. `final`
   - based on `mcr.microsoft.com/dotnet/aspnet:9.0`
   - exposes port `8080`
   - runs `dotnet GuildedThorn.com.dll`

## Runtime Expectations

- ASP.NET Core listens on `http://+:8080` in the final container
- HTTPS termination is likely expected upstream if deployed behind a reverse proxy
- the app requires external configuration for JWT, MongoDB, RabbitMQ, Spotify, and Loki

## Related

- [[GuildedThorn.com - Overview|GuildedThorn.com]]
- [[GuildedThorn.com - Backend|GuildedThorn.com - Backend]]
- [[GuildedThorn.com - API and Services|GuildedThorn.com - API and Services]]
