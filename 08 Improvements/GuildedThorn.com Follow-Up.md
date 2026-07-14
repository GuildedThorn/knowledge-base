## Purpose

Track concrete technical and documentation follow-up items discovered while reading the `GuildedThorn.com` repo, now checked out at `~/Documents/GuildedThorn.com`.

## Current State

- The project is documented in `07 Projects` and is current as of the .NET 10 / WebAuthn / S3 storage / knowledge-base-sync rewrite.
- Several items from the previous pass are now resolved by feature work that landed since: `RadioController`/`RadioService` are fully implemented (no longer placeholders), and gallery uploads now go to S3-compatible storage rather than local `wwwroot` writes.
- Some documentation and hardening gaps are still open.

## Documentation Tasks

- [ ] Add a real environment and secrets note covering JWT, Fido2, MongoDB, S3, RabbitMQ, Spotify, Web Push, and Loki config sources
- [ ] Add page-by-page feature notes for portfolio, stream, radio, guestbook, blog, gallery, donations, and knowledge-base browser
- [ ] Document the knowledge-base sync engine's failure/conflict behavior (what happens if the vault repo has a bad commit, or sync overlaps with a manual trigger)
- [ ] Document the expected reverse proxy or TLS termination setup for production — actual answer is now known and should be written up: the `websites` NixOS host fronts the app with a Cloudflare Tunnel, not a locally-terminated reverse proxy (see [[02 Systems/NixOS - Host websites|Host websites]])

## Backend Follow-Up

- [ ] Verify whether `UserController` should accept `PATCH` only, since the frontend currently uses `POST` for `/api/user/updateData`
- [ ] Verify whether `BlogController.UpdatePost` should require authorization, since `CreatePost` is owner-only but update currently is not marked the same way
- [ ] Replace or harden `AuthController.CheckAuthentication`, which currently checks token expiry by decoding rather than fully validating signature and claims
- [ ] Decide whether `GalleryController` read endpoints should really require auth or whether gallery browsing is intended to be public
- [ ] Decide whether the `OpenIddict` registration (if still present) is intentional or just stubbed scaffolding

## Deployment and Build Follow-Up

- [ ] Verify whether building Vite directly into `../wwwroot` is still the long-term intended workflow now that a NixOS module is the real production deploy path
- [ ] Clean up duplicated or noisy `publish/wwwroot` content declarations in the `.csproj`, if still present after the .NET 10 upgrade

## Related

- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[GuildedThorn.com - Overview|GuildedThorn.com]]
- [[GuildedThorn.com - API and Services|GuildedThorn.com - API and Services]]
- [[02 Systems/NixOS - Host websites|Host websites]]
