# Changelog

All notable changes to `django-project` are documented in this file.

## [Unreleased]

### Added
- `README.md`, `LICENSE`, `ARCHITECTURE.md`, `SECURITY.md`, `CHANGELOG.md`
- `.gitignore` (Python, Django, uv/venv, static/media)

### Changed
- Expanded `README.md` from a single-line title to project overview, structure, routes, design system, getting started, and conventions

## [0.2.0] - 2026-10-16 — Apply DESIGN.md design system

### Added
- `templates/base.html` — shared shell: sticky 80s toolbar nav, window-styled footer, `{% block content %}`
- `static/css/style.css` — full rewrite implementing `DESIGN.md` tokens (colors, Georgia serif, 4–48px spacing, 4–12px radius, 120–260ms motion) and 80s components (window cards, title-bar chrome, chunky OS buttons with default/hover/active/focus-visible/disabled states, `::selection` rule, reduced-motion support, grid-paper background)

### Changed
- `templates/mainApp/main.html` — extends `base.html`; hero preserves original "Rate Movies. Share Truth." copy; feature cards restyled as window cards
- `templates/movies/movies.html`, `templates/review/review.html`, `templates/watchList/watchList.html`, `templates/account/account.html` — extend `base.html`; original stub content preserved inside window cards

### Fixed
- Removed legacy dark-theme values (black backgrounds, Segoe UI, gradients, glass cards) and broken relative CSS paths on sub-routes

## [0.1.0] - 2026-10-16 — Landing page

### Added
- Initial Django project scaffold: `MovieReviewProj` project + `mainApp`, `movies`, `reviews`, `accounts`, `watchList` apps
- Root URLConf including all apps at `''`
- `mainApp` home page with hero, features grid, footer
- Stub pages for movies, reviews, account, watch list
- `static/css/style.css` (original dark modern style)
- `DESIGN.md`, `AGENTS.md`, `CLAUDE.md`
