from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Tutor_room(models.Model):
    name_room = models.CharField(max_length=250, default='SOME STRING')
    status_room = models.CharField(max_length=250)

class Computer(models.Model):
    name_com = models.CharField(max_length=250, default='SOME STRING')
    status_com = models.CharField(max_length=250)

class Publisher(models.Model):
    name = models.CharField(max_length=250, default='SOME STRING')
    address = models.CharField(max_length=250, default='SOME STRING')

class All_type(models.Model):
    all_type_name = models.CharField(max_length=250)
    def __str__(self):
        return self.all_type_name
class Book_type(models.Model):
    type_book = models.CharField(max_length=250, default='SOME STRING', editable=True)
    all_type_id =  models.ForeignKey(All_type, on_delete=models.PROTECT)
    def __str__(self):
        return self.type_book 

class Book_info(models.Model):
    isbn = models.CharField(max_length=250, default='SOME STRING')
    img_book = models.ImageField(upload_to='static/static_dirs/images/')
    book_type_id = models.ForeignKey(Book_type, on_delete=models.PROTECT)
    name_book = models.CharField(max_length=250)
    amount_book = models.IntegerField()
    location_book = models.CharField(max_length=250)
    descri_book = models.CharField(max_length=250)
    published_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    def __str__(self):
        return self.name_book

class Borrow_Notes(models.Model):
    book_isbn = models.CharField(max_length=250, default='SOME STRING')
    date = models.DateField(auto_now=True)
    return_date = models.DateTimeField(default=datetime.now()+timedelta(days=7))
    borrow_user = models.ForeignKey(User, on_delete=models.CASCADE)

class CalculateFines(models.Model):
    date = models.DateField(auto_now=True)
    chrage = models.IntegerField()
    librarian_id = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_user = models.ForeignKey(Borrow_Notes, on_delete=models.CASCADE)

class Borrower_Tutor_Room(models.Model):
    borrow_user = models.ForeignKey(User, on_delete=models.CASCADE)
    tutor_room = models.ForeignKey(Tutor_room, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField()

class Borrower_Computer(models.Model):
    borrow_user = models.ForeignKey(User, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

class Borrow_Book_Info(models.Model):
    borrow_user = models.ForeignKey(Borrow_Notes, on_delete=models.CASCADE)
    book_info_id_book = models.ForeignKey(Book_info, on_delete=models.CASCADE)