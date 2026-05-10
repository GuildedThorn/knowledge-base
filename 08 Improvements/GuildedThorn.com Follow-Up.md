## Purpose

Track concrete technical and documentation follow-up items discovered while reading the `GuildedThorn.com-main` repo.

## Current State

- The project is documented in `07 Projects`.
- The architecture is clear: ASP.NET Core backend, Vite frontend, MongoDB, RabbitMQ, SignalR, Loki, and JWT cookie auth.
- Several implementation and documentation gaps are visible from the repo snapshot.

## Documentation Tasks

- [ ] Add a real environment and secrets note covering JWT, MongoDB, RabbitMQ, Spotify, and Loki config sources
- [ ] Add page-by-page feature notes for portfolio, stream, radio, guestbook, blog, gallery, and tools
- [ ] Document where static files like `Resume.pdf`, images, and gallery uploads are expected to live in deployment
- [ ] Document the expected reverse proxy or TLS termination setup for production

## Backend Follow-Up

- [ ] Verify whether `UserController` should accept `PATCH` only, since the frontend currently uses `POST` for `/api/user/updateData`
- [ ] Verify whether `BlogController.UpdatePost` should require authorization, since `CreatePost` is owner-only but update currently is not marked the same way
- [ ] Replace or harden `AuthController.CheckAuthentication`, which currently checks token expiry by decoding rather than fully validating signature and claims
- [ ] Decide whether `GalleryController` read endpoints should really require auth or whether gallery browsing is intended to be public
- [ ] Finish or remove placeholder code in `RadioController` and `RadioService`
- [ ] Decide whether the `OpenIddict` registration is intentional or just stubbed scaffolding

## Deployment and Build Follow-Up

- [ ] Verify whether building Vite directly into `../wwwroot` is the long-term intended workflow
- [ ] Clean up duplicated or noisy `publish/wwwroot` content declarations in the `.csproj`
- [ ] Record how Docker deployment is actually performed and what environment injection method is used

## Related

- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[GuildedThorn.com - Overview|GuildedThorn.com]]
- [[GuildedThorn.com - API and Services|GuildedThorn.com - API and Services]]
