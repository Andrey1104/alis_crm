# Generated by Django 5.0.6 on 2024-06-24 07:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="tag",
            field=models.ManyToManyField(
                null=True, related_name="tag_messages", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]