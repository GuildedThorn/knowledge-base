## Purpose

Document the architecture and purpose of the `CI4k` project.

## Summary

CI4k ("Caught in 4K Rich Presence" / CI4kRPC) is a configurable, time/calendar-based Discord Rich Presence tray app — built to stop people DMing the user while at work by automatically showing an accurate status. Built as:

- Java 21, Maven-built, packaged into a single shaded/fat jar (`maven-shade-plugin`, main class `com.guildedthorn.ci4k.CI4k`)
- a system tray app (falls back to a plain window if no tray support)
- GitHub: [GuildedThorn/CI4k](https://github.com/GuildedThorn/CI4k)

## Stack

- `io.github.CDAGaming:DiscordIPC` for Discord Rich Presence
- `gson` for JSON config
- `biweekly` for iCalendar parsing/recurrence expansion
- `flatlaf` for the Swing look-and-feel
- `slf4j` for logging
- auto-detects and matches the system theme via Stylix (`/etc/stylix/palette.json`) or by parsing GTK's `gtk.css` base16 vars, falling back to a plain light theme
- also ships a Nix flake (`nix run .` / `nix build .`) that sets `_JAVA_AWT_WM_NONREPARENTING=1` to avoid a blank AWT window on tiling Wayland compositors like Hyprland/sway

## Repo Layout

- `src/main/java/com/guildedthorn/ci4k/`
  - `CI4k.java`: entrypoint
  - `core/`: `AppConfig.java`, `CalendarConfig.java`, `CalendarEvent.java`, `ConfigStore.java`, `DiscordPresenceService.java`, `GoogleCalendarService.java`, `PresenceData.java`, `PresenceResolver.java`
  - `theme/`: `StylixTheme.java`, `ThemePalette.java`
  - `ui/`: `Ci4kIcons.java`, `MainWindow.java`, `TrayController.java`
- `src/main/resources/config.json` and `src/main/resources/icons/*.png` (bundled icon set)
- `assets/icons/`: matching SVG source set (home, work, sleep, programming, studying, gaming, exercise, watching, meeting, coffee, app logo)
- top-level `config.json`: runtime config, must live in the app's working directory
- `pom.xml`, `dependency-reduced-pom.xml`, `flake.nix`/`flake.lock`, `.github/workflows/build.yml`

## Major Features

- GUI dashboard: General tab (Discord Client ID, default state/details/images), Schedule tab (per-day-of-week table editor for timed presence entries), Calendar tab (optional calendar integration)
- Calendar integration via any ICS-serving calendar (Google Calendar's secret iCal URL, Outlook, Nextcloud, etc.) — no OAuth or cloud project needed
- Live calendar events override the weekly schedule with templated fields (`{summary}`, `{location}`, `{description}`), re-sync every 5 minutes, handle recurrence/cancellations, ignore all-day/"Free" events, and show a Discord "time left" countdown
- Config is fully GUI-editable and round-trips to the same `config.json` an advanced user could hand-edit

## Runtime Dependencies

- Java 21 JVM (bundled via the shaded jar) or the Nix package
- `config.json` present in the working directory
- Rich Presence art assets uploaded separately as named art assets in the Discord Developer Portal (512x512+), referenced by key in config

## Notes

- Personal desktop tray app, not a deployed service — no systemd unit.

## Related

- [[GuildedThorn.com - Overview|GuildedThorn.com]]
