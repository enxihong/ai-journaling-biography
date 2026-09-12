# Product Differentiation — A Friend, Not an Interview

> **Status:** design direction, agreed in brainstorm
> **Problem it answers:** competing journaling/biography apps already exist on
> the Play Store. They lose users because they feel like an interrogation.
> **Related:** [`whiteboard-plan.md`](./whiteboard-plan.md) (the flow as first
> drawn), [`ai-journal-flow.mermaid`](./ai-journal-flow.mermaid) (the flow as
> revised by this document),
> [`family_memory_ai_detailed_plan.md`](./family_memory_ai_detailed_plan.md).

---

## 1. Diagnosis — why the competition feels like surveillance

The complaint is not that competing apps are ugly or slow. It is that talking to
them feels like being interviewed, or being watched. That comes from four
structural properties, not from tone of voice:

1. **Turn asymmetry.** The app asks, the user answers, forever. No friendship
   has that shape. That structure *is* an interview, whatever words fill it.
2. **Visible extraction intent.** Every question is instrumental — it is filling
   a schema, and the user can feel it. This is the part that reads as spying.
3. **The artifact is the stated goal.** "Let's build your biography" turns every
   answer into testimony for a permanent record. People self-censor immediately.
4. **Completionism.** The app chases dates, surnames, exact sequences. Friends
   do not. A friend forgets the date and remembers the feeling.

### This is partly in our own plan

The **"enough data?"** gate in the original whiteboard flow is property 4 in
flowchart form: it holds the user in a loop until the system has harvested
enough to satisfy its schema. **We are removing it.** Whatever the user said is
enough. Write it down, however thin.

---

## 2. The reframe

> **The diary is a byproduct, never the ask.**

The user never journals. The user talks to someone. The entry appears
afterwards, unprompted, and can be edited or binned.

Every mechanic below follows from that single move.

---

## 3. Mechanics

### 3.1 Voice notes, not chat

Push-to-talk. The user rambles for 30–60 seconds. The companion replies in
voice. No text field, no suggested prompts, no "How was your day?" empty state.

The voice-note thread shape does more tonal work than any amount of prompt
engineering. A text box with a blinking cursor is a form; a held button is a
conversation.

### 3.2 React, don't ask

Replace follow-up questions with reactions.

```text
Interview:  "How did that make you feel?"
Friend:     "Wait — she said what?"
```

Budget roughly **one question per three reactions**. Curiosity should arrive as
interruption, not as a question queue.

### 3.3 Let details drop on purpose

The companion does not chase the year, the surname, or the exact sequence of
events. Dropping details is what signals that nobody is taking notes. Anything
genuinely needed can be resolved silently later, or never.

### 3.4 Reciprocity through shared history, not a fabricated life

A companion with invented weekend plans is both obvious and a trust bomb. Do not
build one.

Instead, the shared substance of the friendship is **the user's own history**:

```text
"You said almost exactly this about your sister in March."
```

That is what makes a friend a friend — they were there. It is also the one thing
competitors cannot copy without building the same memory layer.

### 3.5 "Off the record"

The user can say *off the record* mid-sentence, and that stretch is never
stored — not as a journal entry, not as a memory, not as a transcript.

No other feature communicates trust this loudly, and it is the precise inverse
of surveillance.

### 3.6 The callback

Weeks or months later, unprompted:

```text
"A year ago tonight you were terrified about that interview. You got it."
```

This is the retention loop and the emotional payoff in a single feature.

### 3.7 Mood without a mood picker

Prosody is already in the audio. Infer mood from voice and words; surface it as a
gentle after-the-fact read the user can correct in one tap.

Five emoji faces is a form. The mood tracker should be invisible.

### 3.8 Family tree from gossip, not genealogy

Never show a relationship dropdown. People get mentioned inside stories; the
tree assembles quietly behind that; the user confirms occasionally with one tap.

The competing family apps make you do data entry about your dead grandmother.
Ours does not.

---

## 4. Anonymization as the visible differentiator

Anonymization is not backend hygiene here. It is a feature the user **sees**.

- Pseudonymize on-device **before** the API call: `Mum` → `PERSON_1`,
  `Kreuzberg` → `PLACE_3`. The mapping stays local.
- Give the user a **receipt**: a screen showing the literal text that left the
  device.

One screen answers the surveillance complaint better than any privacy policy,
and it is the strongest beat in the demo.

### 4.1 Architecture consequence

This forces a real decision about the voice stack:

| | Speech-to-speech (OpenAI Realtime) | STT → redact → LLM → TTS (ElevenLabs) |
| --- | --- | --- |
| Latency | Best, ~500ms | ~1–1.5s |
| Anonymization | Impossible — raw audio leaves the device | Works — redaction happens on the transcript |
| Voice quality / casting | Good | Better, and the voice is ours to choose |
| Interruptibility | Native | Needs building |

**Decision: take the pipeline.** We lose roughly half a second and gain the
entire privacy story, which is the wedge against the competition.

Implementation notes:

- ElevenLabs Scribe for STT, ElevenLabs TTS for output.
- **Interruptibility is not optional.** Being able to talk over the companion
  matters more to the friend illusion than raw latency does.
- Diary generation is a separate, batched, end-of-day job. It is not in the
  latency path.

### 4.2 Voice casting

Do not pick a therapist voice. Calm, low and endlessly patient is the interview
timbre — it is what the competitors sound like. Pick a voice that sounds like it
would laugh at you.

---

## 5. The 90-second demo

1. Talk to it for 60 seconds like a friend. It interrupts, it teases, it calls
   back something from "last week."
2. **Reveal one:** the diary entry it wrote — in the user's own phrasings, not
   the model's.
3. **Reveal two:** the anonymized payload that actually left the device.

Differentiation and privacy in one beat, no slides.

---

## 6. Risks to decide on now

### Parasocial dependence

We are inviting vulnerable disclosure to something that performs friendship.

- The companion must never claim exclusivity, irreplaceability, or feelings it
  does not have.
- It stays identifiably an AI. No pretence otherwise, even in character.
- Crisis content needs a defined path before launch, not after.

### Fabrication

A friend who misremembers your life is worse than a form that never knew it. The
provenance rules in the detailed plan matter **more** under this design, not
less. The companion may be warm; it may not be inventive about facts.

### Latency

Breaks the illusion faster than mediocre writing does. Budget for it before
budgeting for prose quality.

### The anonymization promise

Once we show a receipt screen, it must be true. Every payload, every endpoint,
every retry. A single unredacted call makes the whole positioning a lie.
