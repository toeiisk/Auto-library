from django.shortcuts import render
from .forms import *
# Create your views here.
def return_book(request,num):
    return_book = CalculateFines.objects.get(pk=num)
    return_form = ReturnBookForm()
    return render(request, 'return-book.html', context={
        'form': return_form,
        'return_book': return_book
    })