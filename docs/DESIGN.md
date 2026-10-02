# Design System: NTU GICE Group C

## Overview

**Creative North Star: "The Product Spec Page"**

The page reads like an Apple or Google product specification page: a white ground, grey rounded panels, near-black text, and one link blue. Nothing is decorative. Type is set in whatever system face the reader's device ships (SF and PingFang TC on Apple, Noto Sans TC elsewhere) and is set large, so hierarchy comes from size and weight, not from ornament. The world replaced an earlier engineering computation-pad direction at the user's instruction; none of that world's paper, stamps, or hand-drawn marks carry over.

Density is low and calm. One content column (1040px max, 760px reading measure) holds everything; sections are separated by a single hairline and generous vertical space. Depth is tonal: a grey panel on white, a black ground with a charcoal panel in dark mode. The page has no raster imagery; the only graphics are small stroked SVG glyphs (plus/minus disclosure, external-link arrow, forward arrow) drawn in `currentColor`.

**Key Characteristics:**
- System font stack only; no custom display face.
- Large type: 20px body, 46–84px title, 52–68px stat numerals.
- White/grey tonal panels with 14–18px radii; hairlines instead of shadows.
- One interactive color (link blue); one warning color reserved for deadlines.
- Light and dark themes, following `prefers-color-scheme` and overridable with `data-theme`.

## Colors

A near-achromatic Apple-style neutral set with one blue for everything interactive and one warm warning tone.

### Primary
- **Link Blue** (light #0066CC, dark #2997FF): every link, the primary pill button, the quiet button's text, the open Q&A number, hover on Q&A questions and cross-links, timeline dots, and the focus ring (at 60% via `color-mix`). It is the only color that signals "you can act here".

### Secondary
- **Deadline Rust** (light #B64400, dark amber #FF9F0A): the registration-close date in the hero panel, days-left counts,. Nowhere else.

### Neutral
- **Ground** (white #FFFFFF / black #000000): page and sticky-bar background; also the selected segment's fill.
- **Panel Grey** (#F5F5F7 / #1C1C1E): every panel, card, tag chip, pill track, and quiet button.
- **Ink** (#1D1D1F / #F5F5F7): headings and body text.
- **Secondary Ink** (#6E6E73 / #A1A1A6): summaries, captions, table headers, tags, question numbers at rest, list markers.
- **Hairline** (#D2D2D7 / #3A3A3C): 1px row dividers, section tops, bar underline.

### Named Rules
**The One Blue Rule.** Blue means interactive. Never use it for emphasis, decoration, or headings that are not links.

**The Warning Is Rare Rule.** Rust/amber appears only on dates and countdowns. If it is not about time or absence, it is not rust.

## Typography

**Display Font:** system UI (-apple-system / SF Pro, with PingFang TC, then Noto Sans TC, Microsoft JhengHei, Roboto, Segoe UI, Arial)
**Body Font:** same stack
**Label/Mono Font:** none distinct; numerals use `tabular-nums`

**Character:** One family, the device's own. Noto Sans TC (400/500/600/700) is loaded from Google Fonts only as the non-Apple fallback for Traditional Chinese.

### Hierarchy
- **Display** (700, clamp(46px, 7.4vw, 84px), 1.1): the page title only; `word-break: keep-all` with a `<wbr>` at the natural CJK break.
- **Headline** (700, clamp(34px, 4.4vw, 52px), 1.15): section headings.
- **Stat** (600, clamp(52px, 5.6vw, 68px), 1, -0.02em, tabular): the big numbers in rule and admission cards, with a 20px unit beside them.
- **Lead** (500, clamp(24px, 2.7vw, 30px), 1.6): section opening statements, 760px measure.
- **Title** (600, 21–28px): card headings, Q&A questions, professor names, preparation rows.
- **Body** (400, 20px, 1.7; 19px under 760px): running text. Q&A answers run clamp(19px, 2vw, 21px) at 1.85 line-height in Chinese, 1.7 in English.
- **Secondary** (400, 17px, 1.6–1.65): descriptions under titles, table cells, notes, in Secondary Ink.
- **Label** (500, 14–15px): table headers, segment and language buttons (15–16px).

### Named Rules
**The Size Not Style Rule.** Hierarchy comes from size and weight (400/500/600/700). No italics (`em` and `i` are reset to normal), no uppercase, no letter-spaced labels.

**The Nothing Under 14px Rule.** The smallest shipped text is 14px (tags); body never drops below 19px.

## Layout

A single centered column: max 1040px with a fluid gutter of clamp(20px, 5vw, 48px); prose and headers cap at a 760px measure. Sections stack with clamp(48px, 7vw, 88px) vertical padding and a hairline top border. Card grids use a uniform 12px gap: rules and admission stats in 3 columns (2 at ≤980px, 1 at ≤760px), base courses in 4 (2 at ≤980px), course map 1fr/1fr/1.6fr. List-style content (research areas, dates, Q&A, cross-links) is hairline-separated rows with 20–24px vertical padding and a fixed left column (240px areas, 56px Q&A number, 190px dates). The sticky top bar is 60px tall; under 760px the section tabs wrap to a second, horizontally scrollable row.

## Elevation & Depth

Flat. Depth is tonal: grey panels on the ground, hairlines between rows. The single shadow is a soft lift on the selected segment of a pill control (`0 1px 3px rgba(0,0,0,.12)`), echoing the platform's native segmented control.

### Named Rules
**The Tone Not Shadow Rule.** Separate things with Panel Grey or a 1px Hairline. Shadows appear only on a selected segment.

## Shapes

Soft, consistent rounding. Tags 6px; small panels (deadline, task) 14px; cards 16px; the sources band 18px; every button, pill track, and segment fully rounded (999px). Focus ring corners 4px. Glyphs are 2px stroked line icons with round caps; timeline markers are 10px circles, filled for required and ring-only for optional.

## Components

### Buttons
- **Shape:** full pill (999px).
- **Primary ("open source"):** Link Blue fill, white 17px/500 text, 12px 20px padding, 12px external-link arrow; hover brightens 8%.
- **Quiet (expand/collapse all):** Panel Grey fill, Link Blue 16px/500 text, 10px 18px padding, 40px min height; hover darkens 3%.
- **Focus:** 3px Link Blue ring at 60%, 2px offset.

### Segmented Control
Language toggle (中文/EN) and map switcher: Panel Grey pill track with 3–4px padding; segments are text in Secondary Ink; the pressed segment gets a Ground fill, Ink text, and the soft lift shadow. State is exposed with `aria-pressed`.

### Cards / Containers
- **Corner Style:** 16px (14px for the small deadline/task panels, 18px for the sources band).
- **Background:** Panel Grey.
- **Shadow Strategy:** none (see Elevation).
- **Border:** none.
- **Internal Padding:** 22–26px (20px on mobile).

### Navigation
Sticky bar on the Ground color with a hairline underline. Brand at 19px/600 on the left; section tabs at 17px in Secondary Ink, current tab in Ink at 600 with a 2px Ink underline; language pill on the right.

### Disclosure Rows (Q&A and preparation)
Native `details` rows between hairlines. Summary grid: 56px tabular question number (30px/600, Secondary Ink, turns Link Blue when open), the question at Title size, and a 24px plus/minus glyph whose vertical stroke rotates away over 0.25s. Answers are indented to the question text and capped at the reading measure.

### Stat Card
Panel Grey card with a Stat-size tabular numeral and a 20px unit, a 21px/600 title, and 16.5–17px Secondary Ink explanation.

## Do's and Don'ts

### Do:
- **Do** use the system font stack as shipped, with Noto Sans TC as the only loaded web font.
- **Do** keep body text at 20px (19px on mobile) and let size, not decoration, carry hierarchy.
- **Do** group content on Panel Grey (#F5F5F7 / #1C1C1E) cards with 14–18px radii and a 12px grid gap.
- **Do** separate list rows with a single 1px Hairline.
- **Do** define every new color for both light and dark themes.
- **Do** use `tabular-nums` for all numbers, dates, and course codes.

### Don't:
- **Don't** introduce a custom or decorative display face.
- **Don't** bring back the engineering-pad vocabulary: paper textures, stamps, hand-drawn marks, margin annotations.
- **Don't** use Link Blue for anything that is not interactive, or rust/amber for anything that is not a deadline.
- **Don't** add drop shadows to cards; the only shadow is the selected segment's lift.
- **Don't** put small uppercase or letter-spaced labels above headings.
