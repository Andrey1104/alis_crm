# Generated by Django 5.0.6 on 2024-06-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description_cs",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="description_de",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="description_en",
            field=models.TextField(blank=True, null=True),
        ),
    ]
