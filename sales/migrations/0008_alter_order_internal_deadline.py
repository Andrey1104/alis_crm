# Generated by Django 5.0.6 on 2024-06-21 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sales", "0007_rename_customer_order_direct_customer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="internal_deadline",
            field=models.DateField(blank=True, null=True),
        ),
    ]