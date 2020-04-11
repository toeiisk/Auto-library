from django.shortcuts import render
from .forms import *
# Create your views here.
def borrow_notes(request):
    borrow_form = BorrowNotesForm()
    return render(request, 'borrow.html', context={
        'form': borrow_form
    })