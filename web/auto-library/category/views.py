from django.shortcuts import render
from mylibrary.models import *
import datetime
import pytz

def search_book(request):
    context = {}
    search = request.GET.get('search', '') # get ค่าที่มาจาก search
    context['search'] = search #กำหนดค่าให้
    context['book'] = Book_info.objects.filter(name_book__icontains=search)
    #เอาค่า search มาเทียบกับ name ของ Restaurnt เพื่อนำมาแสดง
    return render(request, 'category/index.html', context=context)

def math(request):
    allbook = Book_info.objects.all()
    publisher = Publisher.objects.all()
    booktype = Book_type.objects.all()
    alltype = All_type.objects.all()
    
    return render (request, 'category/mathpage.html',
                    context = {
                        'allbook' : allbook,
                        'publisher' : publisher,
                        'booktype' : booktype,
                        'alltype' : alltype
                    }
                )

def science(request):
    allbook = Book_info.objects.all()
    publisher = Publisher.objects.all()
    booktype = Book_type.objects.all()
    alltype = All_type.objects.all()
    
    return render (request, 'category/sciencepage.html',
                    context = {
                        'allbook' : allbook,
                        'publisher' : publisher,
                        'booktype' : booktype,
                        'alltype' : alltype
                    }
                )
                
def blogbook(request, num):
    book = Book_info.objects.get(pk=num)
    booktype = Book_type.objects.all()
    alltype = All_type.objects.all()
    allbook = Book_info.objects.all()

    amout_book = book.amount_book

    return render (request, 'category/book.html',
                    context={
                        'book' : book,
                        'booktype' : booktype,
                        'alltype' : alltype,
                        'allbook' : allbook,
                        'amount_book' : amout_book
                    }
    )

def computer(request):
    count = 0
    datenow = datetime.datetime.now()
    computer = Computer.objects.all()
    datenow = pytz.utc.localize(datenow)
    datenow = datenow.replace(tzinfo=pytz.utc)
    for i in computer:
        print("+++++++++++++++++++++++++++++", i.status_com, 'test1')
        if i.status_com == 'UNAVAILABLE':
            borrower_bomputer = Borrower_Computer.objects.filter(computer=i.id)
            if (borrower_bomputer[0].expire_date < datenow):
                i.status_com = 'AVAILABLE'
                print("+++++++++++++++++++++++++++++", i.status_com, 'test2')
                i.save()
        if i.status_com == 'AVAILABLE':
            count += 1
    return render (request, 'category/computerpage.html', 
                    context = {
                        'count' : count,
                        'computer' :computer
                    }
    )
    
def tutor(request):
    tutorroom = Tutor_room.objects.all()
    count = 0
    nubroom = Tutor_room.objects.filter(status_room='AVAILABLE')

    for i in nubroom:
        count += 1

    return render (request, 'category/tutorpage.html', 
                    context = {
                        'tutorroom' : tutorroom,
                        'count' : count
                    }
    )



