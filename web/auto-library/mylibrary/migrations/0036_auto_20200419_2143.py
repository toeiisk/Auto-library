# Generated by Django 3.0.5 on 2020-04-19 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0035_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='idcard',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
    ]
