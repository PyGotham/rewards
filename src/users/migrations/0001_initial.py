# Generated by Django 3.0.5 on 2020-04-23 16:36

import django.contrib.postgres.fields.citext
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True  # type: ignore

    dependencies = []

    operations = [
        migrations.RunSQL(
            "CREATE EXTENSION IF NOT EXISTS citext", reverse_sql=migrations.RunSQL.noop
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        blank=True, max_length=128, verbose_name="password"
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    django.contrib.postgres.fields.citext.CIEmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
