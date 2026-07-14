## Purpose

Document the architecture and deployment shape of the `ThornBot` project.

## Summary

ThornBot is a personal Discord bot for the GuildedThorn.com ecosystem — music playback, a live-radio auto-join integration, and guestbook notifications. Built as:

- a .NET 10 (C#) console app using Discord.Net 3.20.1 (Commands + Interactions) for slash commands
- Victoria (a LavaLink client) for music, spawning its own Lavalink JVM child process on startup
- RabbitMQ.Client for consuming the `guestbook_messages` queue published by GuildedThorn.com
- GitHub: [GuildedThorn/ThornBot](https://github.com/GuildedThorn/ThornBot), MIT licensed

## Repo Layout

- `Program.cs`: entrypoint; `ThornBot.cs`: core bot class
- `Handlers/`: `CommandHandler.cs`, `ComponentHandler.cs`, `EmbedHandler.cs`, `EventsHandler.cs`, `PresenceHandler.cs`, `RadioArchiveAutocompleteHandler.cs`
- `Modules/`: `AudioModule.cs`, `PlayerControlsModule.cs`, `RadioModule.cs`, `UserModule.cs`
- `Services/`: `AudioService.cs`, `GuestBookService.cs`, `LavaLinkService.cs`, `LoggingService.cs`, `RadioService.cs`, `UptimeService.cs`
- `Attributes/`: `RequirePlayerAttribute.cs`, `RequireRadioNotLiveAttribute.cs`
- `Resources/config.json`: discord/radio/lavalink settings
- `application.yml(.example)`: Lavalink's own Spring Boot config (port 2333)
- `dev/up.sh` / `dev/down.sh`: local RabbitMQ container plus dev `.env` generation
- `flake.nix`: Nix dev shell (dotnet SDK 10, jdk21) that also exposes `nixosModules.default` (`services.thornbot`) to run it as a systemd service

## Major Features

- Music: `/play` (YouTube/SoundCloud/direct URL), `/join`, `/leave`, `/skip` (vote-skip requiring >85% of non-bot listeners), `/stop`, `/resume`, `/songrequest`
- Radio: polls GuildedThorn.com's `/api/radio/status` every 5s; on live, auto-joins a dedicated voice channel, plays the stream, posts now-playing updates, and disables music commands in that guild (LavaLink allows one voice connection per guild)
- Guestbook: consumes the RabbitMQ queue from GuildedThorn.com and posts new entries to a configured channel
- `/info` (uptime, guild/user counts, ping, version), `/radio` (status)
- Uptime Kuma push monitoring

## Runtime Dependencies

- .NET 10 SDK
- a JVM for Lavalink, plus a manually-downloaded `Lavalink.jar` and `application.yml`
- RabbitMQ
- config via `Resources/config.json`, overridable with `Section__Key` environment variables

## Deployment

Runs as a systemd service (`services.thornbot`) via its own NixOS module, with options for `package`, `lavalinkPackage`, `javaPackage`, and `environmentFile`. Has crashed in the past — systemd-coredump entries for the `ThornBot` process exist on the main workstation.

## Related

- [[GuildedThorn.com - Overview|GuildedThorn.com]]
- [[GuildedThorn.com - API and Services|GuildedThorn.com - API and Services]]
