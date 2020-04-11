from django.db import models
from django.contrib.auth.models import User

class Tutor_room(models.Model):
    name_room = models.CharField(max_length=250, default='SOME STRING')
    status_room = models.CharField(max_length=250)

class Computer(models.Model):
    name_com = models.CharField(max_length=250, default='SOME STRING')
    status_com = models.CharField(max_length=250)

class Publisher(models.Model):
    name = models.CharField(max_length=250, default='SOME STRING')
    address = models.CharField(max_length=250, default='SOME STRING')

class Book_info(models.Model):
    img_book = models.ImageField(upload_to='static/static_dirs/images/')
    type_book = models.CharField(max_length=250)
    name_book = models.CharField(max_length=250)
    amount_book = models.IntegerField()
    location_book = models.CharField(max_length=250)
    descri_book = models.CharField(max_length=250)
    published_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)


class Borrow_Notes(models.Model):
    number_borrowed = models.IntegerField()
    status_book = models.CharField(max_length=250)
    return_date = models.DateField()
    date = models.DateField()
    borrow_user = models.ForeignKey(User, on_delete=models.CASCADE)

class CalculateFines(models.Model):
    date = models.DateField()
    chrage = models.IntegerField()
    librarian_id = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_user = models.ForeignKey(Borrow_Notes, on_delete=models.CASCADE)

class Borrower_Tutor_Room(models.Model):
    borrow_user = models.ForeignKey(User, on_delete=models.CASCADE)
    tutor_room = models.ForeignKey(Tutor_room, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

class Borrower_Computer(models.Model):
    borrow_user = models.ForeignKey(User, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

class Borrow_Book_Info(models.Model):
    borrow_user = models.ForeignKey(Borrow_Notes, on_delete=models.CASCADE)
    book_info_id_book = models.ForeignKey(Book_info, on_delete=models.CASCADE)