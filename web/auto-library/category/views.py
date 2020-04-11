from django.shortcuts import render
from mylibrary.models import Book_info, Publisher, Book_type, All_type

# Create your views here.
def category(request):
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
    
def blogbook(request):
    return render (request, 'category/book.html')



