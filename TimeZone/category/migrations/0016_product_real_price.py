# Generated by Django 4.2.4 on 2023-12-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0015_remove_offer_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='real_price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
