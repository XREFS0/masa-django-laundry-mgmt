"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lsmsApp", "0005_laundry_products_price_laundryproducts_laundryitems"),
    ]

    operations = [
        migrations.AlterField(
            model_name="laundry",
            name="status",
            field=models.CharField(
                choices=[("0", "Pending"), ("1", "In-progress"), ("2", "Done"), ("3", "Picked Up")],
                default=0,
                max_length=2,
            ),
        ),
    ]
