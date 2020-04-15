from django.shortcuts import render
from .forms import *
# Create your views here.
def borrow_book(request,num):
    book = Book_info.objects.get(pk=num)
    borrow_form = BorrowNotesForm()
    return render(request, 'borrow.html', context={
        'form': borrow_form,
        'book': book
    })

def borrow_com(request, num):
    computer = Computer.objects.get(pk=num)
    borrow_form = BorrowComForm()
    return render(request, 'borrow-com.html', context={
        'form': borrow_form,
        'computer': computer
    })

def borrow_tutor(request, num):
    tutorroom = Tutor_room.objects.get(pk=num)
    borrow_form = BorrowTutorForm()
    print(tutorroom)
    return render(request, 'borrow-tutor.html', context={
        'form': borrow_form,
        'tutorroom':  tutorroom
    })