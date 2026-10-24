---
name: movie-review-site
description: django-project movie-review site work (Django + 80s retro-design system). Use for ANY task under /home/fabiljayson/Projects/django-project — covers the DESIGN.md source of truth, agent workflow docs and run command.
---

# django-project — Movie Reviews

Small Django site for rating and reviewing movies, styled by the "django-project Design System": 80s retro-desktop aesthetic (chunky OS buttons, window chrome, pixel borders, grid-paper backgrounds, Georgia serif, Sunset Pop palette).

## Run

```bash
cd django-project/MovieReviewProj && python manage.py runserver   # default port 8000 is ours
```

## Non-negotiables

- **`DESIGN.md` is the portable source of truth** for colors, typography, spacing, radius, motion, component states. Any UI change goes through the tokens there — never inline ad-hoc colors/fonts.
- `AGENTS.md` (and `CLAUDE.md`) at the repo root define workflow conventions for this repo — read them before structural changes.
- `ARCHITECTURE.md`, `SECURITY.md`, `CHANGELOG.md` exist: update CHANGELOG for user-visible changes, respect SECURITY.md process.

## State

9 commits, 25 uncommitted files, **no tests**. If continuing: propose pytest coverage before adding features. History context: this project occupies port 8000 (that's why pulsewatch uses 8001).
