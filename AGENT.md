## Purpose

Short operating contract for generating and updating notes in this vault.

## Priority

1. be correct
2. use few tokens
3. search narrowly
4. avoid duplicates
5. place notes in the right folder

## Search Rules

- check the relevant map note first
- use `rg --files` before broad reads
- read only the closest matching notes
- read config or project files only when they directly support the requested note
- do not scan unrelated folders

## Source Order

1. current user message
2. inbox note content
3. existing vault notes
4. directly related config or project files
5. map notes for linking and placement

## Folder Rules

- `00 Inbox`: raw capture only
- `02 Systems`: OS, config, auth, secrets, deploy flow
- `03 Devices`: hardware and host-specific notes
- `04 Software`: app-specific notes
- `05 Network`: firewall, DNS, routing, VPN, SSH, serial, recovery
- `06 Reference`: standards, commands, templates, cheatsheets
- `07 Projects`: project architecture, API, deployment, runtime
- `08 Improvements`: unresolved work and cleanup

## Note Rules

- one topic per note
- update existing notes before creating new ones
- do not invent facts
- separate current state from planned work
- add only useful sections
- link to the right map note when relevant

## Standard Sections

### Device

- `## Purpose`
- `## Identity`
- `## Hardware Specs`
- `## System Notes` or `## NixOS-Specific Notes`
- `## Related`

### System or Network

- `## Purpose`
- `## Current State`
- `## Tasks`, `## Workflow`, or `## Operations` as needed
- `## Related`

### Project

- `## Purpose`
- `## Summary`
- `## Architecture`, `## Stack`, `## API`, or `## Deployment`
- `## Related`

### Improvement

- `## Purpose`
- `## Current State`
- `## Tasks`
- `## Related`

## Inbox Handling

- extract the real topic
- remove chatter and duplicates
- split multi-topic notes when needed
- move stable knowledge out of inbox
- move unresolved work into `08 Improvements`

## Do Not

- create duplicate notes
- leave fake placeholder links
- restate large amounts of user text without value
- add long explanations when direct note content is enough

## Related

- [[06 Reference/Codex Generation Standard|Codex Generation Standard]]
- [[00 Inbox/Inbox Processing|Inbox Processing]]
