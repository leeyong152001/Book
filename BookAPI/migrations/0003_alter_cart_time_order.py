# Generated by Django 5.0 on 2023-12-31 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookAPI', '0002_comment_rate_alter_cart_time_order_delete_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='time_order',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 31, 15, 1, 0, 42675)),
        ),
    ]