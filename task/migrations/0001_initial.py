# Generated by Django 5.0.6 on 2024-06-24 06:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("NON_URGENT", "Non-urgent"),
                            ("LOW", "Low"),
                            ("MEDIUM", "Medium"),
                            ("HIGH", "High"),
                            ("URGENT", "Urgent"),
                        ],
                        default="HIGH",
                        max_length=15,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("ASSIGNED", "Assigned"),
                            ("SUBMITTED", "Submitted"),
                            ("IN_PROCESS", "In Process"),
                            ("DONE", "Done"),
                        ],
                        default="ASSIGNED",
                        max_length=15,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deadline", models.DateField(blank=True, null=True)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks_creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "executor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks_executor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]