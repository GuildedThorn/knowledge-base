---
summary: "Schema evolution coordinates application deployments, data backfills, compatibility, and rollback paths."
status: active
tags: [reference, engineering, databases, migrations]
private: false
---

# Schema Migrations and Evolution

## Purpose

Schema evolution coordinates application deployments, data backfills, compatibility, and rollback paths.

## Core Model

- Expand/contract migration sequences keep old and new app versions compatible during rolling deploys.
- Backfills can be operationally expensive and should be resumable, throttled, and observable.
- Rollback means code/data compatibility, not just reverting a migration file.

## Engineering Notes

- Prefer additive changes first, deploy code that writes both/read new, backfill, then remove old paths later.
- Make destructive migrations manual or staged behind checks.
- Record migration ownership, expected runtime, lock behavior, and rollback plan.

## Sources

- PostgreSQL - ALTER TABLE - https://www.postgresql.org/docs/current/sql-altertable.html
- Prisma - Data migrations - https://www.prisma.io/docs/guides/data-migration
- Martin Fowler - Evolutionary Database Design - https://martinfowler.com/articles/evodb.html

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
