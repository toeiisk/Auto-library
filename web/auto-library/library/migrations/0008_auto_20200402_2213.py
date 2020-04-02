# Generated by Django 3.0.3 on 2020-04-02 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_borrower_computer_borrower_tutor_room'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tuter_room',
            new_name='Tutor_room',
        ),
        migrations.RenameField(
            model_name='borrower_computer',
            old_name='borrow_user_id',
            new_name='borrow_user',
        ),
        migrations.RenameField(
            model_name='borrower_computer',
            old_name='computer_id',
            new_name='computer',
        ),
        migrations.RenameField(
            model_name='borrower_tutor_room',
            old_name='borrow_user_id',
            new_name='borrow_user',
        ),
        migrations.RenameField(
            model_name='borrower_tutor_room',
            old_name='tutor_room_id',
            new_name='tutor_room',
        ),
    ]