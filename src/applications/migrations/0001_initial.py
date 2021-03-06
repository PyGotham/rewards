# Generated by Django 3.0.5 on 2020-05-04 04:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True  # type: ignore

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Application",
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
                ("background", models.TextField(verbose_name="applicant background")),
                (
                    "reason_to_attend",
                    models.TextField(
                        verbose_name="reason the applicant wishes to attend"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("pending", "Pending")],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "applicant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
