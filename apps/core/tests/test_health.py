from unittest.mock import patch

import environ
import pytest
from django.db import DatabaseError
from rest_framework.test import APIClient

from config.settings import prod


@pytest.mark.django_db
def test_health_check_success():
    client = APIClient()

    response = client.get("/api/health/")

    assert response.status_code == 200
    assert response.data == {
        "status": "ok",
        "database": "ok",
    }


def test_health_check_database_failure():
    client = APIClient()

    with patch(
        "apps.core.views.connection.cursor",
        side_effect=DatabaseError("Database unavailable"),
    ):
        response = client.get("/api/health/")

    assert response.status_code == 503
    assert response.data == {
        "status": "error",
        "database": "unreachable",
    }


def test_production_debug_is_disabled():
    assert prod.DEBUG is False


def test_missing_secret_key_raises_error(monkeypatch):
    monkeypatch.delenv("SECRET_KEY", raising=False)

    env = environ.Env()

    with pytest.raises(environ.ImproperlyConfigured):
        env("SECRET_KEY")
