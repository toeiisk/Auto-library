# Generated by Django 3.0.5 on 2020-04-15 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0025_auto_20200415_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculatefines',
            name='chrage',
        ),
    ]