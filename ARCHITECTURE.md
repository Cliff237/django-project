# Architecture

## Overview

`django-project` is a Django web application for movie reviews styled with the django-project Design System (`DESIGN.md`), an 80s retro-desktop visual system. The project follows Django's standard "project + apps" layout: one Django project (`MovieReviewProj`) containing several small Django apps.

## Directory ownership

```
MovieReviewProj/                 # Django project root (manage.py lives here)
├── manage.py                    # Django CLI entry point
├── db.sqlite3                   # Default SQLite database (dev)
├── MovieReviewProj/             # Project package: settings, urls, wsgi, asgi
│   ├── settings.py              # Django settings (DEBUG=True, SQLite, static dirs)
│   ├── urls.py                  # Root URLConf: includes all app URLs at root ''
│   ├── wsgi.py / asgi.py        # WSGI/ASGI application entry points
│   └── templates/base.html      # Shared shell: toolbar nav + window-styled footer
├── static/                      # Collected static assets
│   ├── css/style.css            # DESIGN.md token implementation (80s components)
│   ├── images/                  # Background images (bodybg.jpg)
│   └── fotawesome/              # Font Awesome icon font
├── templates/                   # (DIRS template dir; unused, APP_DIRS used instead)
├── mainApp/                     # Home page
│   ├── views.py                 # HomePageView (TemplateView -> mainApp/main.html)
│   ├── urls.py                  # '' -> home
│   └── templates/mainApp/main.html
├── movies/                      # Movies catalog (stub)
│   ├── views.py                 # MoviesPageView (TemplateView -> movies/movies.html)
│   ├── urls.py                  # 'movies/' -> movie
│   └── templates/movies/movies.html
├── reviews/                     # Reviews (stub)
│   ├── views.py                 # MoviesReviewsPageView (TemplateView -> review/review.html)
│   ├── urls.py                  # 'movies/reviews' -> reviews
│   └── templates/review/review.html
├── accounts/                    # User accounts (stub)
│   ├── views.py                 # AccountPageView (TemplateView -> account/account.html)
│   ├── urls.py                  # 'accounts/' -> account
│   └── templates/account/account.html
└── watchList/                   # Watch list (stub)
    ├── views.py                 # WatchListPageView (TemplateView -> watchList/watchList.html)
    ├── urls.py                  # 'watchList/' -> watchList
    └── templates/watchList/watchList.html
```

## Tech stack

- **Framework**: Django 5.2 (project settings header references Django 6.0.3 template; installed version is 5.2.18)
- **Database**: SQLite (`db.sqlite3`) — default, dev-appropriate; swap `DATABASES` ENGINE/NAME for production (PostgreSQL recommended)
- **Templates**: Django Template Language (`django.template.backends.django.DjangoTemplates`), `APP_DIRS: True` plus `DIRS` pointing at `MovieReviewProj/templates`
- **Static files**: `STATIC_URL = 'static/'`, `STATICFILES_DIRS` = `MovieReviewProj/static`
- **Auth**: `django.contrib.auth` installed, password validators enabled
- **Middleware**: Security, sessions, CSRF, auth, messages, clickjacking (Django defaults)
- **Styling**: Single CSS file implementing `DESIGN.md` tokens; Font Awesome for icons

## URL routing

All apps are included at root path `''` in `MovieReviewProj/urls.py`, so each app's `urls.py` defines full paths (e.g. `movies/` in `movies/urls.py` becomes `/movies/`). There are no `app_name` namespaces defined yet — add them when reversing URLs in templates.

## Request flow

1. Browser requests a path.
2. Django root `URLConf` matches against included app patterns in order: `mainApp`, `movies`, `reviews`, `accounts`, `watchList`.
3. Matched `TemplateView` renders the corresponding template.
4. Templates extend `base.html`, which loads `static/css/style.css` and renders the 80s toolbar nav + window-styled footer.
5. `style.css` applies `DESIGN.md` tokens (colors, Georgia serif, 4/8/12/16/24/32/48px spacing, 4/8/12px radius, 120/180/260ms motion, chunky OS button states, window chrome).

## Data layer

No models are defined yet across any app (`models.py` files are empty stubs). The site is currently static template views only. To add data (movies, reviews, watch lists, user profiles):
1. Define models in the relevant app's `models.py`.
2. Run `python manage.py makemigrations` and `python manage.py migrate`.
3. Register models in `admin.py` for the Django admin.
4. Switch views from `TemplateView` to `ListView`/`DetailView`/`CreateView` as needed.

## Design system boundary

`DESIGN.md` is framework-agnostic and portable. `static/css/style.css` is the Django-specific mapping of its tokens. UI changes must consult `DESIGN.md` first (tokens before raw hex values; preserve content; check contrast; mobile-first).

## Extension points

- Add `app_name` to each app's `urls.py` and use namespaced `{% url %}` tags.
- Add models + migrations for persistent data.
- Replace stub `TemplateView`s with form-handling views (reviews submit, watch list toggle).
- Wire `accounts` to `django.contrib.auth.views` (login/logout/password reset).
- Add `MEDIA_URL`/`MEDIA_ROOT` for user-uploaded images (movie posters).
