uses 3.13.7

## Dev

```bash
cd src
cp .env.example .env   # only needed on a fresh clone
docker compose up
```

- App: http://localhost:8000 (Django `runserver`, auto-reloads on code changes)
- Tailwind watch runs in a sidecar container (`assets/css/input.css` -> `workout_log/static/css/output.css`)
- The DB is persisted from the container into `src/data/db.sqlite3`
- Production (gunicorn) variant: `docker compose -f docker-compose.yml up`
