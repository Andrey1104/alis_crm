# Generated by Django 5.0.6 on 2024-06-24 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sales", "0009_cart"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="direct",
            field=models.ImageField(default=1, upload_to=""),
        ),
    ]
