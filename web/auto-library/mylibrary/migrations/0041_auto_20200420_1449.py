# Generated by Django 3.0.5 on 2020-04-20 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0040_remove_idcard_img_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower_computer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 14, 49, 43, 590830)),
        ),
    ]