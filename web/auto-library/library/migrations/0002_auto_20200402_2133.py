# Generated by Django 3.0.3 on 2020-04-02 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='name_com',
            field=models.CharField(default='SOME STRING', max_length=250),
        ),
        migrations.AddField(
            model_name='tuter_room',
            name='name_room',
            field=models.CharField(default='SOME STRING', max_length=250),
        ),
    ]