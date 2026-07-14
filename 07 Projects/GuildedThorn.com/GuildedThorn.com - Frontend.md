## Purpose

Describe the React/Vite frontend for GuildedThorn.com.

## Stack

- React `19`
- TypeScript
- Vite `6`
- Tailwind CSS `4`
- React Router `7`
- SignalR client
- `@xyflow/react` for network diagrams

## Build and Output

- frontend source lives in `GuildedThorn.com-Frontend/`
- Vite builds into the backend `../wwwroot` directory
- aliases are defined for `components`, `routes`, `styles`, `assets`, `backend`, `layouts`, `pages`, and `lib`

## Route Structure

Public routes:

- `/`
- `/login`
- `/register`
- `/contact`
- `/net`
- `/stream`
- `/tools/pomodoro`
- `/tools/regex`
- `/tools/loremipsum`
- `/tools/colorconverter`
- `/tools/uuidgenerator`

Protected routes:

- `/settings`
- `/guestbook`
- `/radio`
- `/blog/upload`
- `/blog/pages`
- `/gallery/upload`
- `/gallery/images`

## Major Frontend Features

- portfolio landing page with personal and hardware content
- GitHub stats and pinned projects
- Spotify top artists section
- Twitch embed page
- ThornNet diagram with saved node positions in local storage
- guestbook UI
- login/register flows, plus WebAuthn passkey/security-key registration and login
- blog and gallery upload interfaces
- knowledge-base browser reading the synced vault notes from the backend
- utility tools implemented fully in the browser

## API Consumption

The frontend fetch layer calls the endpoints documented in [[GuildedThorn.com - API and Services|API and Services]], including the newer WebAuthn, knowledge base, push, contact, donations, and stream-schedule routes.

## Notes

- auth flows rely on backend-set cookies and use `credentials: "include"` in relevant fetch calls
- the radio page creates a SignalR connection and polls Icecast metadata
- several UI components and pages are custom rather than scaffold defaults

## Related

- [[GuildedThorn.com - Overview|GuildedThorn.com]]
- [[GuildedThorn.com - API and Services|GuildedThorn.com - API and Services]]
