# Mobile App Spec — for Bilt

A plain-English description of the app to build with Bilt. This describes what the app
does and why, not how it's wired up technically — Bilt works best from a description
like this.

## What this app is

A journaling app that turns everyday conversation into lasting memories. You talk about
your life the way you'd talk to a friend, and the app turns that into a diary entry. Over
time, it notices patterns in what you've shared — recurring themes, people who matter to
you, things you keep coming back to. You can also build a simple family tree and turn your
memories into a biography chapter.

## Use cases

### 1. Capture a memory by talking, not typing forms
**As someone who wants to preserve a memory**, I open the app, and it feels like texting a
thoughtful friend. I say what's on my mind — "Today I visited my grandpa and he told me
about fishing when he was young" — and the app asks one gentle follow-up question at a
time to help me remember more, instead of handing me a blank form to fill in.

*Why it matters:* People don't journal because blank pages are intimidating. Conversation
isn't.

### 2. Turn a conversation into a diary entry I can keep
**As a user who just finished talking**, I tap one button and my conversation becomes a
proper, readable diary entry with a title — something I could show someone, not just a
raw chat log.

*Why it matters:* This is the moment where "talking" becomes "something real that's mine."

### 3. Discover patterns about myself I hadn't noticed
**As someone who's saved a few entries over time**, I tap "find my patterns" and the app
shows me things I keep circling back to — people, feelings, recurring topics — based on
what I've actually written, not generic personality-quiz answers.

*Why it matters:* This is the emotional payoff of journaling long-term — understanding
yourself better, made visible instead of buried in old notebooks.

### 4. Build a simple family tree and attach memories to people
**As someone documenting my family**, I add people I want to remember — starting with
just a name and how they're related to me — and attach memories to them as I think of
them. The person doesn't need to be a user of the app themselves; I can add my
grandfather even if he'll never open a phone.

*Why it matters:* Most memories about family members are about people who aren't going
to type them in themselves.

### 5. Turn my memories into a biography chapter
**As someone with a handful of saved entries**, I tap "write my biography" and get back
a warm, narrative chapter woven from what I've actually shared — not a robotic summary,
and nothing invented that I didn't actually say.

*Why it matters:* This is the "wow" moment — years of scattered memories becoming
something that reads like a real story about a real life.

## Tone and feel

Warm, personal, unhurried. This is not a productivity app — it should feel more like a
keepsake than a task tracker. Avoid corporate/dashboard-style UI; lean toward something
that feels like a diary or a photo album.

## Screens, roughly

1. **Talk / Journal** — a conversation view where you talk to the AI and save what comes
   out of it as an entry
2. **My Journal** — a list of saved entries you can look back through
3. **Patterns** — a simple screen showing what the app has noticed about you over time
4. **Family Tree** — people you've added, with the memories attached to each
5. **My Biography** — the generated chapter(s), readable like a short story

## What's not needed yet

- No login/account system for the hackathon demo
- No sharing with other people yet — everything is private to the one user for now
- No voice input required (typing is fine for the demo)

## Notes

This describes the product on its own terms — it doesn't assume any particular backend
or data setup. Build it as a complete, self-contained experience (AI conversation,
storage, pattern detection, biography generation all included) rather than assuming it
needs to plug into another team member's work.
