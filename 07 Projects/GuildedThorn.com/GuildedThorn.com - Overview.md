## Purpose

Document the architecture, runtime dependencies, and deployment shape of the `GuildedThorn.com-main` project under `~/Downloads/GuildedThorn.com-main`.

## Summary

GuildedThorn.com is a personal portfolio and platform project built as:

- an ASP.NET Core `net9.0` backend
- a React 19 + TypeScript + Vite frontend
- MongoDB-backed application data
- JWT cookie-based authentication
- SignalR for live chat
- RabbitMQ for guestbook message publishing
- Loki/Serilog for application logging

## Repo Layout

- `Program.cs`: backend entrypoint and service registration
- `Controllers/`: API controllers for auth, blog, chat, gallery, GitHub, guestbook, radio, Spotify, and user data
- `Services/`: MongoDB, RabbitMQ, SignalR hub, and radio/chat helpers
- `Models/`: backend data models and request payload types
- `Resources/config.json`: additional runtime configuration, currently used for Loki URI
- `GuildedThorn.com-Frontend/`: separate Vite frontend application
- `Dockerfile`: multi-stage build for frontend + backend container image
- `flake.nix`: Nix dev shell for .NET, Bun, Node, and supporting tools

## Major Features

- portfolio landing page with personal profile and hardware setup content
- GitHub profile and pinned project data
- Spotify top artists integration
- Twitch stream page
- ThornNet network visualization page
- chat/radio functionality using SignalR
- guestbook system
- blog system with upload flow
- gallery system with image upload flow
- user registration, login, and profile update features
- small browser-side utility pages like pomodoro, regex testing, lorem ipsum, color conversion, and UUID generation

## Runtime Dependencies

- ASP.NET Core 9
- React 19
- Vite
- Bun
- MongoDB
- RabbitMQ
- Loki
- HTTPS for auth cookie flow

## Related

- [[GuildedThorn.com - Backend|GuildedThorn.com - Backend]]
- [[GuildedThorn.com - Frontend|GuildedThorn.com - Frontend]]
- [[GuildedThorn.com - API and Services|GuildedThorn.com - API and Services]]
- [[GuildedThorn.com - Deployment|GuildedThorn.com - Deployment]]
