from django.shortcuts import render
from .forms import *
# Create your views here.
def return_book(request):
    return_form = ReturnNotesForm()
    return render(request, 'return-book.html', context={
        'form': return_form
    })