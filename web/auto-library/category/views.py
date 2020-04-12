from django.shortcuts import render
from mylibrary.models import *

# Create your views here.
def math(request):
    allbook = Book_info.objects.all()
    publisher = Publisher.objects.all()
    booktype = Book_type.objects.all()
    alltype = All_type.objects.all()
    
    return render (request, 'category/index.html',
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

    return render (request, 'category/book.html',
                    context={
                        'book' : book,
                        'booktype' : booktype,
                        'alltype' : alltype,
                        'allbook' : allbook
                    }
    
    
    )



