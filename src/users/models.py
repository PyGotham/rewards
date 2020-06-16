from __future__ import annotations

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.postgres.fields import CIEmailField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# pyre-ignore[11]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
class User(AbstractBaseUser):
    # pyre-ignore[28]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    email = CIEmailField(_("email address"), unique=True)
    # Blank passwords are allowed since we only allow applicants to use
    # magic links to log in.
    password = models.CharField(_("password"), max_length=128, blank=True)
    # pyre-ignore[6]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(_("user can access the admin"), default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        # pyre-ignore[16]: This is fixed by https://github.com/facebook/pyre-check/pull/256.
        username, domain = self.email.split("@", 1)

        # Hide the characters in the username other than the first one.
        return f"{username[0]}{'*' * (len(username) - 1)}@{domain}"
