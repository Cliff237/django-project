# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| current `main` | Yes |

## Reporting a vulnerability

Security issues should be reported privately, not as public GitHub issues. Contact the repository owner via GitHub or open a draft security advisory on GitHub (`Security` tab → "Report a vulnerability").

Include:
- Steps to reproduce
- Affected routes or components
- Suggested fix (if any)

## Known security considerations (development state)

This project is in early development. The following are known and must be addressed before any production deployment:

### `SECRET_KEY`
`MovieReviewProj/settings.py` contains a hardcoded `SECRET_KEY` marked `django-insecure-...`. This is a development-only value.
- **Fix**: Load `SECRET_KEY` from an environment variable (`DJANGO_SECRET_KEY`) with a fallback only for local dev. Never commit production keys.

### `DEBUG = True`
`DEBUG` is `True` in `settings.py`, which exposes detailed error pages (including tracebacks and request data) to end users.
- **Fix**: Set `DEBUG = False` in production, ideally via `DJANGO_DEBUG` env var.

### `ALLOWED_HOSTS = []`
With `DEBUG = True`, Django accepts any host. In production this enables host-header attacks.
- **Fix**: Set `ALLOWED_HOSTS` to the exact domain(s) the app serves, via env var.

### Database
The app uses SQLite (`db.sqlite3`), which is file-based and unsuitable for concurrent production traffic.
- **Fix**: Switch to PostgreSQL (or another production RDBMS) in `DATABASES`, configured via env vars.

### Static files in production
`STATICFILES_DIRS` points at a local `static/` directory and `STATIC_URL = 'static/'`. This works for `runserver` but not for production serving.
- **Fix**: Use `whitenoise` or a dedicated static file server/CDN; run `python manage.py collectstatic`.

### CSRF / sessions / clickjacking
Django's default middleware is enabled (`CsrfViewMiddleware`, `SessionMiddleware`, `XFrameOptionsMiddleware`, `SecurityMiddleware`). Cookie settings (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, `SECURE_SSL_REDIRECT`) are not configured for HTTPS.
- **Fix**: Enable secure cookie flags and HTTPS redirect behind a TLS termination proxy.

### Dependencies
Only Django and its standard transitive deps (`asgiref`, `sqlparse`) are used. Font Awesome is vendored under `static/fotawesome/`.
- **Fix**: Keep dependencies updated; audit with `pip-audit` or `uv` equivalent before releases.

### Authentication
`django.contrib.auth` and password validators are installed, but `accounts/` is currently a stub with no login/signup flow. No user registration, password reset, or permission checks exist yet.
- **Fix**: Wire `accounts` to `django.contrib.auth.views` before exposing user data.

## Secure defaults that ARE in place

- CSRF protection middleware enabled
- X-Content-Type-Options / X-Frame-Options via `SecurityMiddleware`
- Password validators (similarity, min length, common password, numeric)
- `USE_TZ = True` for timezone-safe datetimes

## Maintenance

Review this file before tagging any release. Rotate `SECRET_KEY` immediately if a leaked value is suspected.
