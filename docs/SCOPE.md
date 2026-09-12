# Scope Decision — Option B

We're building **Option B**: Journal + a simple Family Tree (no full sharing/permissions system).
The full vision lives in `docs/family_memory_ai_detailed_plan.md` — that document is a
long-term product spec, not our build target. We treat it as a reference to extend into
*if* time allows, not the plan itself.

## What we committed to build (Option B)

1. Journal conversation (chat with AI) → structured journal entry
2. Pattern detection across multiple journal entries
3. Simple family tree: create a person, link a memory to them
4. Biography chapter generated from journal entries + patterns
5. Sharing/audience-selection: UI only, no real permissions backend

## Status

- [x] Backend scaffold (FastAPI + SQLite)
- [x] Frontend scaffold (plain HTML/JS, one page)
- [x] `/api/chat` — tested working with real OpenAI key
- [x] `/api/persons`, `/api/persons/{id}/memories` — tested working
- [ ] `/api/journal` (save) — built, not yet tested with real key
- [ ] `/api/patterns` — built, not yet tested with real key
- [ ] `/api/biography` — built, not yet tested with real key
- [ ] Anymize AI integration — waiting on API key/docs
- [ ] ElevenLabs "listen to your biography chapter" — snippet provided, not wired in yet
- [ ] Bilt mobile frontend — teammate has a build, integration effort not yet assessed

## Stretch goals, in priority order (only after Option B core loop fully works)

1. Anymize AI privacy layer (real award track, low effort once we have API access)
2. ElevenLabs narration of the biography chapter (demo wow-factor, ~30–45 min)
3. Bilt mobile frontend integration (unknown effort — depends on how the teammate's
   Bilt export talks to a backend; assess before committing time)
4. Anything further from `family_memory_ai_detailed_plan.md` (sharing permissions,
   claimed/unclaimed profile transitions, family perspective model, etc.) — realistically
   **unlikely** to be reached given the time budget. Do not start these unless 1–3 are
   done and there is still meaningful time left.

## Explicitly not doing

- Real authentication/login (faked/skipped for demo)
- Deployment — running locally for the demo, no hosting
- Dementia/legacy mode as a built feature — stays a **pitch narrative** only
- Google Cloud / Vertex / Gemini — using OpenAI instead
- HeyGen — not in current scope
