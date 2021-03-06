from __future__ import annotations

from django.contrib.auth import get_user_model
from django.test import Client
from factory.django import DjangoModelFactory
import pytest
from sesame.utils import get_query_string


class UserFactory(DjangoModelFactory):
    class Meta:
        # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
        model = get_user_model()
        django_get_or_create = ("email",)

    email = "user@example.org"


@pytest.mark.django_db
# pyre-ignore[11]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
def test_login_link_is_not_shown_to_logged_in_users(client: Client) -> None:
    user = UserFactory()
    qs = get_query_string(user)
    client.get(f"/login/magic{qs}")

    response = client.get("/")
    assert b"log in" not in response.content.lower()


# pyre-ignore[11]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
def test_login_link_is_shown_to_guests(client: Client) -> None:
    response = client.get("/")
    assert b"log in" in response.content.lower()
