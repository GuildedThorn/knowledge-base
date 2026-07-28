---
summary: "ASP.NET Core request handling is a middleware pipeline ending in endpoints; Minimal APIs expose compact route definitions over the same hosting model."
status: active
tags: [reference, engineering, dotnet, aspnet]
private: false
---

# ASP.NET Core Middleware and Minimal APIs

## Purpose

ASP.NET Core request handling is a middleware pipeline ending in endpoints; Minimal APIs expose compact route definitions over the same hosting model.

## Core Model

- Middleware runs in registration order and can short-circuit or call the next delegate.
- Endpoint routing maps requests to route handlers, controllers, SignalR hubs, gRPC services, or Razor pages.
- Dependency injection, configuration, logging, options, and hosting are first-class framework primitives.

## Engineering Notes

- Place authentication before authorization, exception handling early, and static/compression/caching middleware deliberately.
- Use Minimal APIs for small HTTP surfaces and controllers when conventions, filters, or large REST surfaces justify them.
- Treat model binding, validation, auth, rate limits, and OpenAPI metadata as part of the endpoint contract.

## Sources

- Microsoft - ASP.NET Core fundamentals - https://learn.microsoft.com/en-us/aspnet/core/fundamentals/
- Microsoft - ASP.NET Core middleware - https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/
- Microsoft - Minimal APIs overview - https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/overview

## Related

- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
