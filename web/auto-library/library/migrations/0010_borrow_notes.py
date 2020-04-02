# Generated by Django 3.0.3 on 2020-04-02 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0009_delete_borrow_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow_Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_borrowed', models.IntegerField()),
                ('status_book', models.CharField(max_length=250)),
                ('return_date', models.DateField()),
                ('date', models.DateField()),
                ('borrow_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]