# django-project

[![CI](https://github.com/fabiljayson/django-project/actions/workflows/ci.yml/badge.svg)](https://github.com/fabiljayson/django-project/actions/workflows/ci.yml)

A Django movie-review web application styled with the **django-project Design System** (`DESIGN.md`) — an 80s retro-desktop aesthetic (chunky OS buttons, window chrome, pixel borders, grid-paper backgrounds, Georgia serif typography, Sunset Pop color palette).

## What it is

`django-project` is a small Django site for rating and reviewing movies. It is intentionally framework-agnostic in its design tokens: `DESIGN.md` is the portable source of truth for colors, typography, spacing, radius, motion, and component states, usable across React, Vue, Svelte, plain HTML/CSS, or native mobile.

## Project structure

```
django-project/
├── DESIGN.md              # Portable design system (tokens + 80s rules)
├── AGENTS.md              # Agent/CLI workflow conventions
├── CLAUDE.md              # Claude-specific workflow notes
├── README.md              # This file
├── LICENSE                # MIT License
├── ARCHITECTURE.md        # System architecture
├── SECURITY.md            # Security policy
├── CHANGELOG.md           # Release history
├── .gitignore             # Git ignore rules
├── skills-lock.json       # Skill lockfile
├── MovieReviewProj/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── MovieReviewProj/   # Django project config (settings, urls, wsgi, asgi)
│   ├── mainApp/           # Home page (hero + features)
│   ├── movies/            # Movies catalog (stub)
│   ├── reviews/           # Reviews (stub)
│   ├── accounts/          # User accounts (stub)
│   ├── watchList/         # Watch list (stub)
│   ├── static/
│   │   ├── css/style.css  # DESIGN.md token implementation (80s components)
│   │   ├── images/        # Background images
│   │   └── fotawesome/    # Font Awesome icons
│   └── templates/
│       ├── base.html      # Shared shell: toolbar nav + window-styled footer
│       ├── mainApp/main.html
│       ├── movies/movies.html
│       ├── review/review.html
│       ├── watchList/watchList.html
│       └── account/account.html
```

## Routes

| Path | View | Description |
|------|------|-------------|
| `/` | `mainApp.HomePageView` | Home: hero + feature windows |
| `/movies/` | `movies.MoviesPageView` | Movies catalog |
| `/movies/reviews` | `reviews.MoviesReviewsPageView` | Reviews |
| `/accounts/` | `accounts.AccountPageView` | Account |
| `/watchList/` | `watchList.WatchListPageView` | Watch list |
| `/admin/` | Django admin | Admin interface |

## Design system

`DESIGN.md` defines:
- **Colors**: primary `#b83b5e`, primary-strong `#6a2c70`, primary-soft `#f9ed69`, surface `#fff8bf`, text `#2d1638`, border `#8b315f`, plus success/warning/danger
- **Typography**: Georgia serif (body/display), ui-monospace stack, weights 400/500/600/700
- **Spacing**: 4/8/12/16/24/32/48px
- **Radius**: 4/8/12px
- **Motion**: 120/180/260ms
- **Style**: 80s retro desktop — window chrome, pixel borders, chunky buttons, grid-paper backgrounds

`static/css/style.css` is the CSS implementation of these tokens.

## Getting started

### Requirements
- Python 3.11+
- `uv` (recommended) or `pip`

### Install

```bash
cd MovieReviewProj
uv venv
source .venv/bin/activate
uv pip install django
```

### Run

```bash
cd MovieReviewProj
source .venv/bin/activate
python manage.py runserver
```

Open http://127.0.0.1:8000/

### Django checks

```bash
python manage.py check
```

## Conventions

- Follow `AGENTS.md` (npm for package scripts where applicable, comment style, boundaries).
- Read `DESIGN.md` before changing UI, layout, component styling, or interaction behavior.
- Preserve all existing content, copy, routes, and behavior when applying the design system.
- Never commit secrets or keys; `SECRET_KEY` in `settings.py` is development-only.

## Contributing

See `DESIGN.md` AI Implementation Checklist and the Safe Refactor Workflow before changing UI. Open an issue or pull request on GitHub.

## License

MIT License — see `LICENSE`.
