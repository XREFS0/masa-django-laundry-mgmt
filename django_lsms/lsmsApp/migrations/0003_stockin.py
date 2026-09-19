"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("lsmsApp", "0002_products"),
    ]

    operations = [
        migrations.CreateModel(
            name="StockIn",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("quantity", models.FloatField(default=0)),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                ("date_created", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="lsmsApp.products"),
                ),
            ],
            options={
                "verbose_name_plural": "List of Stock-In",
            },
        ),
    ]
