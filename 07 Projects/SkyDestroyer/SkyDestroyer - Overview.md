## Purpose

Document the architecture, runtime dependencies, and deployment shape of the `SkyDestroyer` project.

## Summary

SkyDestroyer is a custom rewrite of AADS (Aerial Assault Dedicated Server) and TAAML (Tribes Aerial Assault Master List) project built as:

- an ASP.NET Core `net9.0` backend
- Loki/Serilog for application logging

## Repo Layout

- `Program.cs`: backend entrypoint for SkyDestroyer.cs
![[Pasted image 20260428181729.png]]
- `SkyDestroyer.cs`: Initialized Server, runs a server scheduler on a dedicated tickrate, sets server options via options in constants, requests data from master list service
![[Pasted image 20260428181804.png]]
- `Utils\Client.cs`: Sets Client Data and Maps out Client/Server Packets
![[Pasted image 20260428181836.png|697]]
## Major Features

- threaded and async runtime
- much cleaner netcode over the existing server software

## Runtime Dependencies

- ASP.NET Core 9
- RabbitMQ
- Loki

## Related

