from django.shortcuts import render
from .forms import *
# Create your views here.
def borrow_notes(request,num):
    book = Book_info.objects.get(pk=num)
    borrow_form = BorrowNotesForm()
    return render(request, 'borrow.html', context={
        'form': borrow_form,
        'book': book
    })

def borrow_com(request):
    borrow_form = BorrowComForm()
    return render(request, 'borrow-com.html', context={
        'form': borrow_form
    })