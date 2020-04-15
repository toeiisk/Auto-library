from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import *

# Register your models here.
admin.site.register(Permission)
admin.site.register(Tutor_room)
admin.site.register(Computer)
admin.site.register(Publisher)
admin.site.register(Book_info)
admin.site.register(Borrow_Notes)
admin.site.register(Borrower_Computer)
admin.site.register(Borrower_Tutor_Room)
admin.site.register(CalculateFines)
admin.site.register(Borrow_Book_Info)
admin.site.register(All_type)
admin.site.register(Book_type)
admin.site.register(Idcard)
