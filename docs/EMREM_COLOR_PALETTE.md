# EmRem Color Palette

A simple brand color system for the EmRem app, based on the current logo.

## Core Brand Colors

| Role | Color | Hex | Use |
|---|---|---|---|
| Primary Purple | 🟣 | `#6117B4` | Main buttons, active navigation, timeline accents, headings, key UI elements |
| Mustard Gold | 🟡 | `#FDC000` | Achievements, milestones, celebrations, badges, highlight states |
| Bright Pink | 🩷 | `#FB2480` | People, relationships, meaningful memories, heart icon, small emotional accents |
| Warm Cream | 🤍 | `#FFF9F2` | Main app background |
| Soft Lavender | 💜 | `#EEE4FB` | Purple-tinted cards, selected states, AI response backgrounds |
| Soft Yellow | 🌼 | `#FFF3C4` | Achievement cards and milestone backgrounds |
| Soft Pink | 🌸 | `#FFE2EE` | People / relationship cards and emotional memory backgrounds |
| Deep Ink | ◼️ | `#24162F` | Main body text and high-contrast text |
| Muted Grey | ◻️ | `#756D7B` | Dates, captions, secondary labels, helper text |
| White | ⚪ | `#FFFFFF` | Cards, modals, clean contrast surfaces |

## Brand Meaning

Use the three main colors consistently:

- **Purple = My Story / Memories**
- **Yellow = Growth / Achievements**
- **Pink = People / Relationships**

This gives the color system meaning instead of using colors only for decoration.

## Recommended UI Balance

Keep the interface calm and premium by using the bright brand colors selectively.

- **60%** Warm Cream / White
- **25%** Purple
- **10%** Mustard Gold
- **5%** Bright Pink

Avoid using purple, yellow, and pink equally across the whole screen.

## Suggested Component Usage

### Primary Button

- Background: `#6117B4`
- Text: `#FFFFFF`

Example:
**Tell a Memory**

### Secondary Button

- Background: `#FFFFFF` or `#FFF9F2`
- Border: `#6117B4`
- Text: `#6117B4`

Example:
**Add Photo**

### Achievement / Milestone

- Background: `#FFF3C4`
- Accent/Icon: `#FDC000`
- Text: `#24162F`

### People / Relationship Card

- Background: `#FFE2EE`
- Accent/Icon: `#FB2480`
- Text: `#24162F`

### AI / Selected State

- Background: `#EEE4FB`
- Accent: `#6117B4`
- Text: `#24162F`

### General Cards

- Background: `#FFFFFF`
- Text: `#24162F`
- Secondary text: `#756D7B`

## Timeline Color Logic

Use the timeline colors consistently so users can understand the type of memory at a glance.

- 🟣 Purple = General memory / life event
- 🟡 Yellow = Achievement / milestone / growth
- 🩷 Pink = Person / relationship / emotional memory

## Accessibility Notes

- Do **not** use mustard yellow (`#FDC000`) as normal text on white.
- Use `#24162F` for readable text on yellow or light backgrounds.
- Use white text on primary purple buttons.
- Keep body text dark enough for strong contrast.
- Use pink and yellow mainly as accents, icons, tags, and backgrounds.

## Brand Line

> **Purple tells the story. Yellow celebrates the journey. Pink remembers the people.**

## CSS Variables

```css
:root {
  --emrem-purple: #6117B4;
  --emrem-gold: #FDC000;
  --emrem-pink: #FB2480;

  --emrem-cream: #FFF9F2;
  --emrem-lavender: #EEE4FB;
  --emrem-soft-yellow: #FFF3C4;
  --emrem-soft-pink: #FFE2EE;

  --emrem-ink: #24162F;
  --emrem-muted: #756D7B;
  --emrem-white: #FFFFFF;
}
```

## Quick Bilt Guidance

When building EmRem in Bilt:

- Use **Warm Cream** as the main background.
- Use **Primary Purple** for main actions and navigation.
- Use **Mustard Gold** for achievements and milestones.
- Use **Bright Pink** for people and relationship-related memories.
- Keep cards mostly white with soft lavender, yellow, or pink backgrounds only where they communicate meaning.
- Keep text minimal and use **Deep Ink** for readability.
- Avoid overly colorful screens; the brand should feel warm, modern, emotional, and polished.
