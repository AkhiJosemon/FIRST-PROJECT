# Generated by Django 4.2.4 on 2023-12-02 04:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0032_alter_coupon_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='expiry_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 12, 1, 4, 33, 15, 627396, tzinfo=datetime.timezone.utc)),
        ),
    ]
