# Django REST Framework Starter Template

A reusable backend starter template built with Django REST Framework, PostgreSQL, Docker Compose, pytest, and Ruff.

## Tech Stack

- Python 3.14
- Django 6.1
- Django REST Framework
- PostgreSQL 17
- Docker Compose
- pytest and pytest-django
- Ruff
- django-environ

## Project Setup

### 1. Clone the repository

```bash
git clone &lt;https://github.com/Manish511T/DRF-Template.git&gt;
cd drf-template
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements/dev.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and configure your local values.

### 5. Start PostgreSQL

```bash
docker compose up -d
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Health endpoint:

`http://127.0.0.1:8000/api/health/`

## Testing

Run tests:

```bash
pytest -v
```

## Code Quality

Check code:

```bash
ruff check .
```

Format code:

```bash
ruff format .
```

## Environment

Development settings: `config.settings.dev`

Production settings: `config.settings.prod`

Never commit your `.env` file or production secrets.

## License

MIT