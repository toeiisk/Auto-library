# Generated by Django 3.0.5 on 2020-04-10 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0002_auto_20200409_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow_notes',
            name='borrow_user',
        ),
        migrations.RemoveField(
            model_name='calculatefines',
            name='borrow_user',
        ),
        migrations.RemoveField(
            model_name='calculatefines',
            name='librarian_id',
        ),
        migrations.DeleteModel(
            name='Borrow_Book_Info',
        ),
        migrations.DeleteModel(
            name='Borrow_Notes',
        ),
        migrations.DeleteModel(
            name='CalculateFines',
        ),
    ]