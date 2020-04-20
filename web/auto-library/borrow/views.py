from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import *


# Create your views here.
def borrow_book(request,num):
    book = Book_info.objects.get(pk=num)
    borrow_form = BorrowNotesForm()
    return render(request, 'borrow.html', context={
        'form': borrow_form,
        'book': book
    })

@login_required
def borrow_com(request, num):
    computer_id = Computer.objects.get(pk=num)
    if request.method == 'POST':
        form = BorrowComForm(request.POST)
        if form.is_valid():
            computer = computer_id
            date = form.cleaned_data['date']
            borrow_user = request.user.username
            form.save()
            print(borrow_user, computer, date)
    borrow_form = BorrowComForm()
    return render(request, 'borrow-com.html', context={
        'form': borrow_form,
        'computer': computer_id
    })

# def borrow_computer(request):
#     form = BorrowComForm(request.POST)
#     if form.is_valid():
#         new_form = form.save()
#     return redirect('index')


def borrow_tutor(request, num):
    tutorroom = Tutor_room.objects.get(pk=num)
    borrow_form = BorrowTutorForm()
    print(tutorroom)
    return render(request, 'borrow-tutor.html', context={
        'form': borrow_form,
        'tutorroom':  tutorroom
    })
