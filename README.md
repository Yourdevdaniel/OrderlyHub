# OrderlyHub

> 🚧 **Work in progress.** Authentication is implemented; the store and order modules are next.

A multi-store order management platform: sellers run one or more stores, list products,
and manage orders from a single dashboard. I'm building it from scratch to practice the
full cycle of a real product, from data modeling to deployment.

## Stack

- **Backend:** Django, Django REST Framework, Simple JWT
- **Frontend:** React, TypeScript, Vite
- **Database:** SQLite in development, PostgreSQL planned for production

## Status

| Module | Status |
|---|---|
| Custom user model (unique email, phone, email verification flag) | ✅ Done |
| Register / login with JWT access + refresh | ✅ Done |
| Refresh token via httpOnly cookie | ✅ Done |
| Email verification tokens | 🔨 In progress |
| Social login (Google, GitHub) | 🔨 In progress |
| Stores, sellers and products | ⏳ Planned |
| Orders | ⏳ Planned |
| Frontend | ⏳ Planned |
| Tests and CI | ⏳ Planned |
| Deploy | ⏳ Planned |

## Data model

The entity diagram is in [`docs/diagram.pdf`](docs/diagram.pdf).

## Running locally

```bash
# backend
cd backend
python -m venv .venv
.venv\Scripts\activate        # Windows  (Linux/macOS: source .venv/bin/activate)
pip install django djangorestframework djangorestframework-simplejwt
python manage.py migrate
python manage.py runserver

# frontend
cd frontend
npm install
npm run dev
```
