from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Tutor_room(models.Model):
    AVAILABLE = 'AVAILABLE'
    UNAVAILABLE = 'UNAVAILABLE'
    STATUS = [
        (AVAILABLE, 'AVAILABLE'),
        (UNAVAILABLE, 'UNAVAILABLE')
    ]

    name_room = models.CharField(max_length=250, default='SOME STRING')
    img_tutor = models.ImageField(upload_to='static/static_dirs/images/tutor/')
    status_room = models.CharField(max_length=12, choices=STATUS, default=AVAILABLE)
    def __str__(self):
        return '(%s) %s' %(self.id, self.name_room) 

class Computer(models.Model):
    AVAILABLE = 'AVAILABLE'
    UNAVAILABLE = 'UNAVAILABLE'
    STATUS = [
        (AVAILABLE, 'AVAILABLE'),
        (UNAVAILABLE, 'UNAVAILABLE')
    ]

    name_com = models.CharField(max_length=250, default='SOME STRING')
    img_com = models.ImageField(upload_to='static/static_dirs/images/computer/')
    status_com = models.CharField(max_length=12, choices=STATUS, default=AVAILABLE)
    def __str__(self):
        return '(%s) %s %s' %(self.id, self.name_com, self.status_com) 

class Publisher(models.Model):
    name = models.CharField(max_length=250, default='SOME STRING')
    address = models.CharField(max_length=250, default='SOME STRING')
    def __str__(self):
        return '(%s) %s' %(self.id, self.name) 

class All_type(models.Model):
    all_type_name = models.CharField(max_length=250)
    def __str__(self):
        return '(%s) %s' %(self.id, self.all_type_name)

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
        return '(%s) %s' %(self.id, self.name_book)

class Borrow_Notes(models.Model):
    book_isbn = models.ForeignKey(Book_info, on_delete=models.PROTECT)
    date = models.DateTimeField()
    return_date = models.DateTimeField()
    charg = models.IntegerField(default='1')
    borrow_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '(%s)' %(self.id)

class CalculateFines(models.Model):
    date = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_user = models.ForeignKey(Borrow_Notes, on_delete=models.CASCADE)

class Borrower_Tutor_Room(models.Model):
    borrow_user = models.ForeignKey(User, on_delete=models.CASCADE)
    tutor_room = models.ForeignKey(Tutor_room, on_delete=models.CASCADE)
    date = models.DateTimeField()

class Borrower_Computer(models.Model):
    borrow_user = models.ForeignKey(User, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    date = models.DateTimeField()

class Borrow_Book_Info(models.Model):
    borrow_user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_info_id_book = models.ForeignKey(Book_info, on_delete=models.CASCADE)

class Idcard(models.Model):
    user_idcard = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    idcard = models.CharField(max_length=250)
    # def __str__(self):
    #     return '(%s) %s' %(self.user_idcard.first_name) ทำหน่อยๆ