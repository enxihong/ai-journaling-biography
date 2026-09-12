# Positioning — A Friend, Not an Interview

> **Status:** for team review. This is a **positioning and pitch** document, not
> a scope change. Everything here is either already true of what we're building,
> a cheap prompt-level change, or explicitly parked until after the hackathon —
> see §5.
> **Related:** [`SCOPE.md`](./SCOPE.md) (what we committed to build),
> [`PROJECT.md`](./PROJECT.md) (judging criteria),
> [`BILT_APP_SPEC.md`](./BILT_APP_SPEC.md).

---

## 1. The claim, in one sentence

> Journaling apps already exist and people abandon them, because talking to one
> feels like being interviewed — or watched. Ours talks back like a friend, and
> the diary writes itself afterwards.

This matters for scoring: **Problem & Idea Clarity (20%)** and **Creativity &
Originality (20%)** are 40% of the total, and both are won by how we frame the
product, not by how much we build.

---

## 2. Why the competitors lose users

The problem with existing journaling/biography apps on the Play Store isn't that
they're ugly or slow. It's that using them feels like an interrogation. That
comes from four *structural* properties, not from tone of voice:

1. **Turn asymmetry.** The app asks, you answer, forever. No friendship has that
   shape. That structure *is* an interview, whatever words fill it.
2. **Visible extraction intent.** Every question is instrumental — it's filling
   a schema, and you can feel it. This is the part that reads as surveillance.
3. **The artifact is the stated goal.** "Let's build your biography" turns every
   answer into testimony for a permanent record. People self-censor instantly.
4. **Completionism.** The app chases dates, surnames, exact sequences. Friends
   don't. A friend forgets the date and remembers the feeling.

Naming this clearly is most of the pitch. It's a problem every judge has felt.

---

## 3. The reframe

> **The diary is a byproduct, never the ask.**

The user never journals. The user talks to someone. The entry appears
afterwards, and can be edited or binned.

We are already closer to this than the competition — our core loop is
conversation → entry, not form → record. The work is making sure the
*conversation* doesn't drift back into interview shape.

---

## 4. Mechanics

### 4.1 React, don't ask — *the highest-value change we can make*

Replace follow-up questions with reactions.

```text
Interview:  "How did that make you feel?"
Friend:     "Wait — she said what?"
```

Roughly **one question per three reactions**. Curiosity arrives as interruption,
not as a question queue.

This is a system-prompt change in `backend/llm.py`. It costs minutes and it is
the single thing that makes the live demo *feel* different from every other
journaling app the judges have seen.

### 4.2 Let details drop on purpose

The companion shouldn't chase the year, the surname, or the exact order of
events. Dropping details is what signals nobody is taking notes. Also a prompt
change.

### 4.3 Shared history, not a fabricated life

A companion with invented weekend plans is both obvious and a trust bomb. Don't
build one. The shared substance of the friendship is **the user's own history**:

```text
"You said almost exactly this about your sister in March."
```

That's what makes a friend a friend — they were there. We already have the
pieces for this: pattern detection across entries is exactly this feature seen
from the other side.

### 4.4 The callback

Pattern detection, reframed. Instead of presenting patterns as an analytics
screen, the companion brings something back unprompted:

```text
"A year ago tonight you were terrified about that interview. You got it."
```

Same endpoint, better story. This is the emotional payoff in the pitch.

### 4.5 "Off the record"

The user says *off the record* mid-sentence and that stretch is never stored.

No other feature communicates trust this loudly, and it's the precise inverse of
surveillance. Cheap to implement (a keyword check before the save path), and it
demos in five seconds.

### 4.6 Family tree from stories, not genealogy

No relationship dropdown as the primary path. People get mentioned inside
stories; the tree fills from that; the user confirms with one tap.

The competing family apps make you do data entry about your dead grandmother.
Ours shouldn't. We already support adding a person who will never use the app —
that's the same instinct.

### 4.7 Mood without a mood picker (post-hackathon)

Infer mood from wording, and later from voice prosody; surface it as a gentle
read the user can correct. Five emoji faces is a form.

---

## 5. What this costs us — honest scope fit

`SCOPE.md` is the build target and this document does not override it.

| Idea | Status |
| --- | --- |
| React, don't ask | **Prompt change — do it now.** Minutes, biggest demo impact. |
| Let details drop | **Prompt change — do it now.** |
| Callback framing of patterns | **Free.** Relabel the existing patterns feature in UI + pitch. |
| Family tree from stories | **Mostly already true.** Keep the form as a secondary path. |
| "Off the record" | **Cheap add** if the core loop is done. Skip if not. |
| Payload receipt (§6) | **Rides on the Anymize work** already planned as stretch #1. |
| Voice-first companion | **Post-hackathon.** `SCOPE.md` says voice isn't required for the demo and that stands. |
| Mood inference | **Post-hackathon.** |

### The one real conflict, stated plainly

The full version of this vision is **voice-first** — push-to-talk, the companion
replies in voice, the text box disappears entirely. That is not what we're
building this weekend, and it shouldn't be. ElevenLabs stays where `SCOPE.md`
puts it: narrating the biography chapter, as stretch goal #2.

But it's worth saying in the pitch that this is where the product goes, because
it's the difference between "a journaling app" and "a companion that happens to
keep a diary."

---

## 6. Anymize as the visible differentiator

We're pursuing the **Best use of anymize.ai** track, and `backend/anonymize.py`
is currently a pass-through placeholder waiting on API access.

The positioning idea: make anonymization something the user **sees**, not
backend hygiene.

- Pseudonymize before the model call: `Mum` → `PERSON_1`, `Kreuzberg` → `PLACE_3`.
- Give the user a **receipt**: a screen showing the literal text that left the
  device.

One screen answers the surveillance complaint better than any privacy policy,
and it turns an invisible integration into a visible demo beat — which is
exactly what an award track needs to see. Low extra effort once the API call
itself works.

**Caveat:** once we show a receipt screen, it has to be true — every call, every
retry. If the integration isn't live, we show the placeholder honestly and say
it's a placeholder. `PROJECT.md` is explicit that clarity scores higher than the
illusion of complexity.

---

## 7. Demo and pitch beats

1. **Problem, first 15 seconds.** "Journaling apps interrogate you. People quit."
2. **Talk to it** like a friend. It reacts, it doesn't interview.
3. **Reveal one:** the diary entry it wrote — in the user's own phrasings.
4. **Reveal two:** the callback — something it noticed across entries.
5. **Reveal three:** the anonymized payload that actually left the device.
6. **Close on where it goes:** voice, family, a life story assembled over years.

---

## 8. Risks worth deciding on

**Parasocial dependence.** We're inviting vulnerable disclosure to something that
performs friendship. The companion must never claim exclusivity or feelings it
doesn't have, stays identifiably an AI, and needs a defined path for crisis
content before this is ever public.

**Fabrication.** A friend who misremembers your life is worse than a form that
never knew it. Warm in manner, strict about facts — nothing invented that the
user didn't say. This is also our "Meaningful Use of AI" story: source-grounded
generation, not free-form writing.

**Demo latency.** Breaks the illusion faster than mediocre prose does.
