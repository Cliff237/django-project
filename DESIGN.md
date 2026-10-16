---
name: "django-project Design System"
description: "Framework-agnostic design rules for web and mobile app implementation."

# ─── Colors ───────────────────────────────────────────────
colors:
  # Brand
  primary:       "#b83b5e"
  primaryStrong: "#6a2c70"
  primarySoft:   "#f9ed69"
  accent:        "#b83b5e"

  # Surfaces
  surface:       "#fff8bf"
  surfaceMuted:  "#f9ed69"

  # Text & Border
  text:          "#2d1638"
  border:        "#8b315f"

  # Feedback
  success:       "#16A34A"
  warning:       "#D97706"
  danger:        "#DC2626"

# ─── Typography ───────────────────────────────────────────
typography:
  family:        "Georgia, serif"
  displayFamily: "Georgia, serif"
  monoFamily:    "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
  source:        "system font stack"
  weights:       "400, 500, 600, 700"
  defaultWeight: 600
  tone:          "serif"

# Spacing
spacing:
  xs:      4px
  sm:      8px
  md:      12px
  lg:      16px
  xl:      24px
  xxl:     32px
  section: 48px

# Radius
radius:
  sm: 4px
  md: 8px
  lg: 12px

# Motion
motion:
  fast:   120ms
  normal: 180ms
  slow:   260ms
---

# Design System Rules

## Purpose
django-project Design System defines portable, framework-agnostic design rules for web and mobile product interfaces. Use it as the source of truth before changing layouts, components, color, typography, motion, or interaction states.

This file is a portable design skill. Any AI or engineer should be able to read it and improve a web or mobile interface without needing React, Vue, Svelte, Tailwind, native mobile, or any other specific technology.

## Operating Modes

### New Project Mode
- Use these rules to create a coherent first implementation when no existing UI exists.
- Build the information architecture, component system, and responsive behavior from the tokens and rules below.

### Existing Project Refactor Mode
- Treat the existing product as the source of truth for content, routes, behavior, data, and information architecture.
- Improve the visual system by patching styles, tokens, spacing, typography, hierarchy, responsive behavior, and component states.
- Do not regenerate whole pages from scratch when a targeted patch can preserve the current experience.
- Do not replace real content with placeholder, demo, lorem ipsum, or simplified content.
- If a section looks inconsistent with this design system, restyle it first. Do not remove it.
- If removing content, routes, features, media, or data logic seems necessary, stop and ask for approval.

## Preservation Rules For Existing Products
- Preserve all existing headings, paragraphs, labels, buttons, links, images, icons, forms, navigation items, sections, routes, and data-fetching logic unless the user explicitly requests removal.
- Preserve semantic meaning and section order unless the user asks for an information-architecture change.
- Preserve working interactions: forms, menus, language toggles, theme toggles, dialogs, tabs, carousels, and scroll behavior.
- Preserve real brand/product names and domain-specific copy. Design changes must not make the page generic.
- Keep every original section represented after the refactor. A redesigned section is acceptable; a missing section is not.
- Never leave the first viewport empty unless the existing product intentionally has an empty state.

## Safe Refactor Workflow
1. Read the existing UI code before editing. Identify sections, routes, state, data dependencies, and user actions.
2. Inventory current colors, typography, spacing, radius, shadows, and component states.
3. Map old visual values to the tokens in this file one-to-one where possible.
4. Patch section by section. Avoid full-file rewrites when the current structure works.
5. After each section, verify the original content is still present, visible, and reachable.
6. After changing colors, check every affected text/background pair for contrast.
7. Verify desktop and mobile before finishing.

## Visual Direction
- Color direction: Sunset Pop - Bold playful energy.
- Typography direction: Editorial Serif - Premium headings.
- Style direction: 80s - Old-computer collage UI with pixel windows, desktop dialogs, chunky controls, grid paper, and CRT wireframes
- References: Old computer aesthetic, Windows 95 dialog collages, 90s web UI sticker sheets, Retro desktop widgets, CRT sci-fi wireframes.
- Visual style: Sunset Pop color direction, Editorial Serif typography, 80s style.

## Style System: 80s
Use 80s to create nostalgic old-computer interfaces: floating desktop windows, pixel borders, chunky buttons, modal dialogs, file icons, loading bars, equalizers, fake OS toolbars, sticker-like cursors, grid-paper backdrops, and optional CRT wireframe panels. It works best for retro portfolios, music pages, zines, playful product launches, game communities, creator sites, sticker/collage pages, and interactive experiments. The mood can lean monochrome navy, teal Windows 95, colorful 90s UI, or amber CRT, but it should feel like a working retro desktop rather than generic synthwave.

### Layout Rules
- use a desktop collage layout: overlapping windows, modal boxes, tool panels, sticker icons, loading widgets, and cursor affordances.
- use grid-paper, checkerboard, teal desktop, or black CRT backgrounds depending on the product mood.
- use window chrome as structure: title bars, close/minimize buttons, resize handles, menu strips, scrollbars, and segmented controls.
- compose hero sections like a retro computer screen or sticker sheet with one dominant message and several supporting UI fragments.
- allow deliberate overlap and duplicated window stacks, but keep primary copy and CTAs unobstructed.
- use monochrome navy/white, teal/gray/blue, colorful 90s primary colors, or amber CRT as coherent modes; avoid mixing every mode in one section.
- use pixel, bitmap, monospace, or chunky display type for labels and headings; keep longer copy in readable sans or mono.
- mobile layout should collapse windows into stacked cards while preserving title bars, pixel borders, and button treatment.

### Component Patterns
- buttons should look like old OS controls: rectangular, beveled or thick-bordered, with clear pressed, focus, and disabled states.
- window cards should include a title bar, border, close/minimize icons, and optional resize handles or shadow offset.
- modals and alerts should use strong iconography: warning triangles, red X, checkboxes, hearts, speech bubbles, or pointer hands.
- forms should use square inputs, pixel borders, short labels, password dots, reset/cancel pairs, and visible focus rectangles.
- progress bars and loading states should use segmented fills, block meters, equalizer sliders, or tiny status text.
- icons should reference folders, files, clocks, cursors, media controls, hearts, chat bubbles, stickers, globes, and system tools.
- navigation can be a fake desktop menu, toolbar row, tab strip, or stack of draggable windows.
- CRT panels can use thin amber line art, scanlines, technical diagrams, loading meters, and wireframe objects.

### Existing Project Refactor Rules
- inventory the existing interface first: navigation, hero, content sections, CTAs, forms, and footer.
- preserve all content and apply the 80s/90s desktop aesthetic through windows, toolbars, pixel borders, icons, and control styling.
- do not remove real content to make room for decorative retro elements.
- patch backgrounds, colors, borders, title bars, buttons, forms, and icon treatments section by section.
- if a section has complex visuals, frame them as app windows, image editors, old media players, file cards, or CRT panels.
- when adding retro references, make them functional or contextual: alerts, loading, file previews, toolbar controls, or media widgets.
- if the product is corporate or formal, use restrained window chrome and grid-paper framing instead of chaotic sticker collage.
- preserve semantic structure and accessibility even when visuals imitate old desktop software.

### Spacing Rules
- use pixel-grid spacing: 4px, 8px, 12px, 16px, 24px, 32px, 48px.
- section padding should be 40px to 72px on desktop, 24px to 40px on mobile.
- window content padding should be compact: 12px to 24px, with tighter spacing in title bars and toolbars.
- keep gutters consistent, but allow intentional overlap between decorative windows when readability is protected.
- leave enough clearance around offset shadows, resize handles, and stacked windows so edges remain visible.
- use grid backgrounds, dividers, and window frames to create groups instead of modern whitespace-only layouts.
- keep content containers within 1120px to 1360px unless the section is intentionally full-screen desktop collage.

### Visual Hierarchy Rules
- use window size, title-bar color, border weight, and cursor placement to establish priority.
- primary CTAs should look like active OS buttons or highlighted dialog actions, not soft modern pills.
- use one dominant mode per section: monochrome navy, teal desktop, colorful primary UI, or amber CRT.
- body text must remain readable; reserve pixel fonts for short labels, buttons, badges, and headings.
- use hard edges, block fills, checker/grid fields, and offset window stacks instead of soft gradients and glows.
- use CRT glow, scanlines, or wireframes only in the amber sci-fi mode and keep them behind readable content.
- decorative cursors, stickers, and icons should guide attention toward actions, not randomly fill empty space.

### Style Anti-patterns
- default to synthwave sunsets, neon gradients, or chrome text unless the reference specifically calls for it.
- add overly soft rounded cards, glassmorphism, neumorphism, or minimalist SaaS styling.
- let overlapping windows, stickers, or cursors cover actual content or CTAs.
- use tiny pixel text for paragraphs or accessibility-critical labels.
- mix too many nostalgia modes in one section without a clear hierarchy.
- sacrifice keyboard focus, semantic controls, or responsive behavior for fake OS visuals.

### Style Checklist
- the page feels like an old-computer UI or retro desktop collage, not generic synthwave.
- color contrast is strong and readable on all windows, dialogs, and panels.
- CTAs look like clickable OS controls with clear default, hover, active, focus, and disabled states.
- title bars, window borders, file icons, dialogs, sliders, loading bars, or media controls are used meaningfully.
- the selected nostalgia mode is coherent: monochrome, teal desktop, colorful 90s UI, or amber CRT.
- content is preserved and readable despite overlap, pixel styling, and decorative UI fragments.
- the result is playful, nostalgic, and usable rather than a random sticker sheet.

## Design Tokens
Use semantic tokens first. Raw values from frontmatter are source values, not permission to scatter hex codes or one-off sizes through implementation.

### Color
- Primary action color: #b83b5e.
- Strong primary: #6a2c70. Use for high-emphasis text, selected state, or strong borders.
- Soft primary: #f9ed69. Use for subtle surfaces, selected backgrounds, or calm highlights.
- Surface: #fff8bf.
- Muted surface: #f9ed69.
- Text: #2d1638.
- Border: #8b315f.
- Success, warning, and danger are semantic states. Pair them with labels, icons, or position; never rely on color alone.
- When moving from a dark theme to a light or warm theme, update inherited light text classes such as white, muted-white, or low-opacity foregrounds.
- Do not apply one warm/cream/brown palette across the entire page without contrast, hierarchy, and content anchors.

### Text Selection
- Use this style-specific `::selection` treatment for 80s. It should follow the selected color tokens and stay readable.
```css
/* 80s selection: chunky old-computer highlight. */
::selection {
  background-color: #6a2c70;
  color: #fff8bf;
  text-shadow: 2px 2px 0 #b83b5e;
}
```
- If the selected color changes, keep the same style behavior but re-check text/background contrast.

### Contrast And Visibility Gate
- Every visible text node must remain readable after color changes.
- Check hero text, navigation, buttons, card titles, form labels, helper text, icons, borders, and disabled states against their actual backgrounds.
- If legacy classes or CSS keep text white on a light surface, replace them with semantic foreground tokens.
- If content appears missing after a restyle, inspect contrast and visibility before deleting or rebuilding the section.
- Do not finish with invisible text, hidden CTAs, empty hero areas, or decorative backgrounds replacing product content.

### Typography
- Primary family: Georgia, serif.
- Display family: Georgia, serif.
- Monospace family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace.
- Allowed weights: 400, 500, 600, 700.
- Default UI weight: 600.
- Keep heading levels semantic. Visual size must follow layout importance, not HTML heading number.
- Keep letter spacing at 0 by default. Use uppercase labels sparingly and only for short metadata.

### Spacing And Radius
- Spacing scale: 4/8/12/16/24/32/48.
- Prefer spacing and grouping over extra borders.
- Use 4px radius for compact controls, 8px for standard cards/inputs, and 12px only for larger feature surfaces.
- Do not invent new spacing values unless the layout cannot be solved with the scale.

## Layout Rules
- Start mobile-first. The smallest useful viewport defines the base layout.
- Use content-driven breakpoints. Do not scale type directly with viewport width.
- Keep navigation, primary actions, and form completion paths easy to reach on touch devices.
- Prefer a clear grid, predictable alignment, and stable dimensions for controls, cards, tabs, and repeated items.
- Empty, loading, and error states must preserve layout stability and explain the next action.

## Component Rules
- Every interactive component must define default, hover, active, focus-visible, disabled, loading, success, and error behavior when those states apply.
- Buttons must communicate hierarchy through role: primary, secondary, tertiary, destructive, or icon-only.
- Forms must keep labels visible, helper text close to the field, and errors specific enough to fix.
- Cards must represent repeated items or contained tools. Do not nest cards inside other cards.
- Modals and popovers must include focus management, escape behavior, and clear dismissal affordances.

## Interaction And Motion
- Motion must clarify state change, not decorate the screen.
- Transitions should usually stay between 120ms and 260ms.
- Provide reduced-motion behavior for animations, parallax, shimmer, and auto-moving content.
- Pointer hover cannot be the only way to reveal important controls because touch devices do not have hover.

## Accessibility Requirements
WCAG 2.2 AA, keyboard-first interactions, visible focus states, semantic HTML before ARIA, reduced-motion support, accessible target sizes.

- Text and meaningful non-text UI must meet WCAG 2.2 AA contrast.
- Keyboard users must be able to reach, understand, and operate every interactive control.
- Focus indicators must be visible, high-contrast, and not hidden by overflow or animation.
- Semantic HTML or native platform semantics come before ARIA patches.
- Touch targets should be at least 24px by WCAG 2.2 AA and should reach 44px when layout allows.

## Content Tone
Clear, concise, implementation-focused, low-jargon, and helpful without being decorative.

- Use direct labels for actions.
- Avoid vague UI copy like "Submit" when the action can be named.
- Keep empty states useful: state what happened, why it matters, and what the user can do next.

## Rules: Do
- use semantic tokens before raw values in components.
- preserve existing content, copy, media, routes, and behavior when applying this system to an existing project.
- preserve hierarchy with spacing, contrast, typography, and component state.
- define default, hover, active, focus-visible, disabled, loading, success, and error states.
- design mobile-first, then enhance for tablet and desktop density.
- keep implementation guidance portable across React, Vue, Svelte, plain HTML/CSS, and mobile UI stacks.
- use old-computer window chrome, pixel borders, title bars, file icons, and chunky buttons.
- use grid-paper, teal desktop, monochrome navy, or amber CRT backgrounds as coherent visual modes.
- make CTAs feel like clickable OS controls with visible pressed and focus states.
- use loading bars, media controls, sliders, equalizers, dialog boxes, and file cards as meaningful UI patterns.
- preserve readability with high contrast and avoid using bitmap fonts for long paragraphs.
- keep the retro desktop language consistent across sections.

## Rules: Don't
- use low-contrast text, hidden focus indicators, or color-only state communication.
- delete or replace existing product content unless the user explicitly asks for content removal.
- introduce one-off spacing, typography, or radius values outside the token system.
- mix unrelated visual metaphors in the same screen.
- depend on framework-specific component names in design rules.
- add decorative motion without reduced-motion fallbacks.
- default to synthwave sunsets, neon gradients, or chrome text unless the reference specifically calls for it.
- add overly soft rounded cards, glassmorphism, neumorphism, or minimalist SaaS styling.
- let overlapping windows, stickers, or cursors cover actual content or CTAs.
- use tiny pixel text for paragraphs or accessibility-critical labels.
- mix too many nostalgia modes in one section without a clear hierarchy.
- sacrifice keyboard focus, semantic controls, or responsive behavior for fake OS visuals.

## AI Implementation Checklist
- Read this file before changing UI, layout, component styling, or interaction behavior.
- Identify the target surface: mobile app, mobile web, desktop web, dashboard, landing page, form flow, or content-heavy view.
- Map the design tokens to the project technology without changing the design intent.
- Reuse existing project components when they can satisfy these rules.
- If the current UI conflicts with this file, explain the conflict and choose the more accessible, consistent option.
- Confirm all original navigation items, hero content, CTAs, media, sections, and forms still exist unless removal was requested.
- Confirm no text became invisible from background, opacity, blend-mode, or inherited color changes.
- Confirm the first viewport contains meaningful product content, not just a background treatment.
- Verify keyboard navigation, focus-visible styling, responsive behavior, text overflow, loading state, and error state before finishing.
